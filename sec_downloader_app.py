#!/usr/bin/env python3
"""
Streamlit UI for Advanced SEC Excel Downloader

This app wraps the AdvancedSECDownloader from `automated_sec_downloader.py` and provides:
- Inputs for API key, ticker, form type, and filing limit
- Live run with captured logs (stdout/stderr) displayed in the UI
- Summary of generated files with sizes and quick actions
"""

import io
import os
import time
import contextlib
from typing import List

import streamlit as st

# Local import of the downloader class
from automated_sec_downloader import AdvancedSECDownloader

# Use the embedded API key from your codebase
# This mirrors the hardcoded key used in automated_sec_downloader.py
API_KEY = "62ff63ea351833fb6ad40b2f4becbf5539a91740ce09544e96b42600de5853c5"


def get_default_download_dir(ticker: str, form_type: str) -> str:
    return f"SEC_Excel_Downloads_{ticker}_{form_type}"


def format_bytes(num_bytes: int) -> str:
    if num_bytes is None or num_bytes < 0:
        return "-"
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if num_bytes < 1024.0:
            return f"{num_bytes:3.1f} {unit}"
        num_bytes /= 1024.0
    return f"{num_bytes:.1f} PB"


def list_downloaded_files(dir_path: str) -> List[dict]:
    files = []
    if not os.path.isdir(dir_path):
        return files
    for root, _, filenames in os.walk(dir_path):
        for name in filenames:
            if name.lower().endswith((".xlsx", ".xls")):
                path = os.path.join(root, name)
                try:
                    size = os.path.getsize(path)
                except Exception:
                    size = 0
                files.append({
                    "name": name,
                    "path": path,
                    "size": size,
                    "type": ("Detailed" if "_Detailed.xlsx" in name else ("Individual" if "Individual_Financials" in name else "File"))
                })
    # Sort: Detailed first, then Individual, then others; then by name desc
    type_order = {"Detailed": 0, "Individual": 1, "File": 2}
    files.sort(key=lambda f: (type_order.get(f["type"], 3), f["name"].lower()))
    return files


st.set_page_config(page_title="SEC Excel Downloader", page_icon="📊", layout="wide")

st.title("📊 SEC Excel Downloader")
st.caption("Wraps SEC API and consolidates financial statements into Excel outputs.")

with st.sidebar:
    st.header("Settings")
    ticker = st.text_input("Ticker", value="MSFT").upper().strip()
    form_type = st.selectbox("Form Type", options=["10-K", "10-Q", "8-K"], index=0)
    limit = st.slider("Number of filings", min_value=1, max_value=10, value=3)
    add_delay = st.checkbox("Add polite delays between requests", value=True)
    st.divider()
    run_button = st.button("Run Downloader", type="primary")

tabs = st.tabs(["Run", "Results", "About"])

with tabs[0]:
    st.subheader("Run Console")
    placeholder_status = st.empty()
    log_area = st.empty()
    log_buffer = io.StringIO()

    if run_button:
        if not ticker:
            st.error("Please provide a ticker.")
        else:
            placeholder_status.info("Initializing downloader...")
            downloader = AdvancedSECDownloader(API_KEY)

            # Capture stdout/stderr while running the automated workflow
            with contextlib.redirect_stdout(log_buffer), contextlib.redirect_stderr(log_buffer):
                try:
                    start = time.time()
                    files = downloader.automated_download(ticker, form_type, limit)
                    duration = time.time() - start
                except Exception as e:
                    print(f"❌ Error: {e}")
                    files = []
                    duration = 0.0

            # Render logs
            logs = log_buffer.getvalue()
            if logs:
                log_area.code(logs)
            else:
                st.info("No logs captured.")

            # Summary
            placeholder_status.success(f"Completed in {duration:0.1f}s. Found {len(files)} file references.")

            # Display results in the Results tab automatically
            with tabs[1]:
                st.subheader("Generated Files")
                out_dir = get_default_download_dir(ticker, form_type)
                file_rows = list_downloaded_files(out_dir)
                if not file_rows:
                    st.info("No Excel files found yet in the expected output folder.")
                else:
                    st.dataframe(
                        {
                            "Type": [r["type"] for r in file_rows],
                            "Name": [r["name"] for r in file_rows],
                            "Size": [format_bytes(r["size"]) for r in file_rows],
                            "Path": [r["path"] for r in file_rows],
                        },
                        use_container_width=True,
                    )

                    enable_dl = st.checkbox("Enable inline download buttons (may be slow for large files)")
                    if enable_dl:
                        for r in file_rows:
                            try:
                                with open(r["path"], "rb") as fh:
                                    st.download_button(
                                        label=f"Download {r['name']}",
                                        data=fh,
                                        file_name=r["name"],
                                        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                                    )
                            except Exception as e:
                                st.warning(f"Could not create download for {r['name']}: {e}")

with tabs[1]:
    st.subheader("Browse Output Folder")
    expected_dir = get_default_download_dir(ticker, form_type)
    st.write(f"Expected output directory: `{expected_dir}`")
    rows = list_downloaded_files(expected_dir)
    if rows:
        st.dataframe(
            {
                "Type": [r["type"] for r in rows],
                "Name": [r["name"] for r in rows],
                "Size": [format_bytes(r["size"]) for r in rows],
                "Path": [r["path"] for r in rows],
            },
            use_container_width=True,
        )
    else:
        st.info("No Excel files found yet. Run the downloader from the Run tab.")

with tabs[2]:
    st.subheader("About")
    st.markdown(
        """
        - This UI wraps `AdvancedSECDownloader` from `automated_sec_downloader.py`.
        - It searches recent filings and downloads the SEC-provided `Financial_Report.xlsx` files.
        - The backend consolidates income statement, balance sheet, and cash flow statements into helpful Excel outputs.

        Tips:
        - Uses the embedded `sec-api.io` token from your code.
        - Start with a small filing limit, then increase as needed.
        - Check the Results tab for generated files and sizes.
        """
    )


