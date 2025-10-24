#!/usr/bin/env python3
"""
Streamlit frontend for SEC tools

Provides tabs for:
- XBRL JSON → Excel
- Full-Text Search
- Filing Download / PDF Generator
- Extractor API
- Stream Listener (instructions)

Run: streamlit run app.py
"""

import os
import tempfile

import pandas as pd
import streamlit as st
import jwt
import sqlite3
import bcrypt
from datetime import datetime, timedelta
from typing import Optional, Tuple

from xbrl_json_to_excel import main as xbrl_main


st.set_page_config(page_title="SEC Tools", layout="wide")

# --- Simple JWT auth gate (email/password) ---
SECRET_KEY = os.environ.get("APP_SECRET_KEY", "change-this-secret-key")
ALGORITHM = "HS256"

DB_PATH = os.path.join(os.path.dirname(__file__), "tristone_auth.db")

# Optional admin seed from env
ENV_ADMIN_EMAIL = os.environ.get("ADMIN_EMAIL", "nishit.wadhwani@tristone-partners.com").strip().lower()
ENV_ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "Nishit@120304")  # plain text only used for initial seed if table empty

def create_token(email: str) -> str:
    payload = {
        "sub": email,
        "iat": int(datetime.utcnow().timestamp()),
        "exp": int((datetime.utcnow() + timedelta(hours=8)).timestamp()),
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token: str) -> bool:
    try:
        jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return True
    except Exception:
        return False

def is_authenticated() -> bool:
    token = st.session_state.get("auth_token")
    return bool(token) and verify_token(token)

def logout() -> None:
    if "auth_token" in st.session_state:
        del st.session_state["auth_token"]

def get_current_user_email() -> Optional[str]:
    token = st.session_state.get("auth_token")
    if not token:
        return None
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return str(decoded.get("sub")) if decoded.get("sub") else None
    except Exception:
        return None

# --- SQLite user management ---
def get_db() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA journal_mode=WAL;")
    return conn

def init_db() -> None:
    with get_db() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT NOT NULL UNIQUE,
                password_hash TEXT NOT NULL,
                is_active INTEGER NOT NULL DEFAULT 1,
                role TEXT NOT NULL DEFAULT 'user',
                created_at TEXT NOT NULL
            );
            """
        )
        conn.execute("CREATE INDEX IF NOT EXISTS idx_users_email ON users(email);")
        # Lightweight migration for legacy DBs: ensure columns exist
        cur_cols = conn.execute("PRAGMA table_info(users);").fetchall()
        existing_cols = {row[1] for row in cur_cols}
        if "is_active" not in existing_cols:
            conn.execute("ALTER TABLE users ADD COLUMN is_active INTEGER NOT NULL DEFAULT 1;")
        if "role" not in existing_cols:
            conn.execute("ALTER TABLE users ADD COLUMN role TEXT NOT NULL DEFAULT 'user';")
        if "created_at" not in existing_cols:
            conn.execute("ALTER TABLE users ADD COLUMN created_at TEXT NOT NULL DEFAULT '';")

        # Helper: dynamic insert to satisfy legacy NOT NULL cols
        def insert_user_dynamic(email: str, password_hash: str, is_active_val: int, role_val: str, created_at_val: str) -> None:
            cols_info = conn.execute("PRAGMA table_info(users);").fetchall()
            col_names = [c[1] for c in cols_info]
            base_cols = ["email", "password_hash", "is_active", "role", "created_at"]
            insert_cols = []
            insert_vals = []
            for c in base_cols:
                if c in col_names:
                    insert_cols.append(c)
                    if c == "email":
                        insert_vals.append(email)
                    elif c == "password_hash":
                        insert_vals.append(password_hash)
                    elif c == "is_active":
                        insert_vals.append(is_active_val)
                    elif c == "role":
                        insert_vals.append(role_val)
                    elif c == "created_at":
                        insert_vals.append(created_at_val)
            # Satisfy any additional NOT NULL columns without defaults
            for cid, name, coltype, notnull, dflt_value, pk in cols_info:
                if name in insert_cols or name == "id":
                    continue
                if int(notnull) == 1 and dflt_value is None:
                    t = (coltype or "").upper()
                    if "INT" in t:
                        insert_cols.append(name)
                        insert_vals.append(0)
                    else:
                        insert_cols.append(name)
                        insert_vals.append("")
            placeholders = ",".join(["?"] * len(insert_cols))
            sql = f"INSERT INTO users({','.join(insert_cols)}) VALUES({placeholders})"
            conn.execute(sql, tuple(insert_vals))
        # Lightweight migration for legacy DBs: ensure columns exist
        cur_cols = conn.execute("PRAGMA table_info(users);").fetchall()
        existing_cols = {row[1] for row in cur_cols}
        if "is_active" not in existing_cols:
            conn.execute("ALTER TABLE users ADD COLUMN is_active INTEGER NOT NULL DEFAULT 1;")
        if "role" not in existing_cols:
            conn.execute("ALTER TABLE users ADD COLUMN role TEXT NOT NULL DEFAULT 'user';")
        if "created_at" not in existing_cols:
            conn.execute("ALTER TABLE users ADD COLUMN created_at TEXT NOT NULL DEFAULT '';")
        # Seed default admin only if table empty or admin doesn't exist
        cur = conn.execute("SELECT COUNT(1) FROM users WHERE lower(email) = lower(?);", (ENV_ADMIN_EMAIL,))
        admin_exists = cur.fetchone()[0]
        
        if admin_exists == 0:
            try:
                pw_hash = bcrypt.hashpw(ENV_ADMIN_PASSWORD.encode(), bcrypt.gensalt()).decode()
                insert_user_dynamic(
                    ENV_ADMIN_EMAIL,
                    pw_hash,
                    1,
                    "admin",
                    datetime.utcnow().isoformat(),
                )
            except sqlite3.IntegrityError:
                # Admin user already exists, skip creation
                pass

def get_user_by_email(email: str) -> Optional[Tuple[int, str, str, int, str, str]]:
    with get_db() as conn:
        cur = conn.execute(
            "SELECT id, email, password_hash, is_active, role, created_at FROM users WHERE lower(email)=lower(?) LIMIT 1;",
            (email,),
        )
        row = cur.fetchone()
        return row if row else None

def create_user(email: str, password: str, role: str = "user", is_active: bool = True) -> bool:
    try:
        with get_db() as conn:
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            cols_info = conn.execute("PRAGMA table_info(users);").fetchall()
            col_names = [c[1] for c in cols_info]
            base_cols = ["email", "password_hash", "is_active", "role", "created_at"]
            insert_cols = []
            insert_vals = []
            for c in base_cols:
                if c in col_names:
                    insert_cols.append(c)
                    if c == "email":
                        insert_vals.append(email.strip().lower())
                    elif c == "password_hash":
                        insert_vals.append(pw_hash)
                    elif c == "is_active":
                        insert_vals.append(1 if is_active else 0)
                    elif c == "role":
                        insert_vals.append(role)
                    elif c == "created_at":
                        insert_vals.append(datetime.utcnow().isoformat())
            for cid, name, coltype, notnull, dflt_value, pk in cols_info:
                if name in insert_cols or name == "id":
                    continue
                if int(notnull) == 1 and dflt_value is None:
                    t = (coltype or "").upper()
                    if "INT" in t:
                        insert_cols.append(name)
                        insert_vals.append(0)
                    else:
                        insert_cols.append(name)
                        insert_vals.append("")
            placeholders = ",".join(["?"] * len(insert_cols))
            sql = f"INSERT INTO users({','.join(insert_cols)}) VALUES({placeholders})"
            conn.execute(sql, tuple(insert_vals))
        return True
    except Exception as e:
        st.error(f"Failed to create user: {e}")
        return False

def verify_credentials(email: str, password: str) -> bool:
    user = get_user_by_email(email)
    if not user:
        return False
    _, _, password_hash, is_active, _, _ = user
    if int(is_active) != 1:
        return False
    try:
        return bcrypt.checkpw(password.encode(), password_hash.encode())
    except Exception:
        return False

# Initialize DB and ensure seed exists
init_db()

# Initialize test user account if needed
try:
    from init_user_account import init_test_user
    init_test_user()
except ImportError:
    pass  # init_user_account.py not available

# Gate the rest of the app until user logs in
if not is_authenticated():
    st.markdown(
        "<h1 style=\"color:#10B981; text-align:center; margin-bottom:0.25rem;\">Tristone Partners</h1>",
        unsafe_allow_html=True,
    )
    st.title("Login")
    st.caption("Access to the SEC Tools Suite is restricted. Please sign in.")
    login_email = st.text_input("Email", key="login_email")
    login_password = st.text_input("Password", type="password", key="login_password")
    if st.button("Login"):
        if verify_credentials(login_email.strip().lower(), login_password):
            st.session_state["auth_token"] = create_token(login_email.strip().lower())
            st.rerun()
        else:
            st.error("Invalid email or password")
    st.stop()

# Logout button bottom-right for easy access
# Placed after auth gate so it only renders for authenticated users

# Show admin tools if current user is admin (by role) or matches ENV admin email
current_user = get_current_user_email()
user_row = get_user_by_email(current_user) if current_user else None
current_role = user_row[4] if user_row else None
is_admin = (current_role == "admin") or (current_user and current_user == ENV_ADMIN_EMAIL)

if is_admin:
    with st.sidebar.expander("Admin: Add User", expanded=False):
        new_email = st.text_input("New user email", key="admin_new_email")
        new_password = st.text_input("Password", type="password", key="admin_new_password")
        new_role = st.selectbox("Role", ["user", "admin"], index=0, key="admin_new_role")
        if st.button("Create User", key="admin_create_user_btn"):
            if new_email.strip() and new_password:
                if create_user(new_email.strip().lower(), new_password, role=new_role):
                    st.success(f"User created: {new_email.strip().lower()}")
            else:
                st.warning("Provide email and password")

# Minimal green/white dashboard styling
st.markdown(
    """
    <style>
      /* Base typography and spacing */
      .stApp { background: #FFFFFF; }
      h1, h2, h3 { color: #064E3B; }
      .block-container { padding-top: 1.5rem; padding-bottom: 2rem; }

      /* Tabs */
      .stTabs [data-baseweb="tab-list"] { gap: 0.25rem; }
      .stTabs [data-baseweb="tab"] {
        background: #F0FDF4;
        border: 1px solid #D1FAE5;
        color: #065F46;
        border-radius: 8px 8px 0 0;
        padding: 0.5rem 0.75rem;
      }
      .stTabs [aria-selected="true"] {
        background: #FFFFFF !important;
        border-bottom-color: #FFFFFF !important;
        color: #065F46 !important;
        box-shadow: 0 -2px 0 #10B981 inset;
      }

      /* Buttons */
      .stButton>button {
        background: #10B981;
        color: #FFFFFF;
        border: none;
        border-radius: 8px;
        padding: 0.6rem 1rem;
      }
      .stButton>button:hover { background: #059669; }

      /* Info/success states */
      .stAlert { border-radius: 8px; }

      /* Inputs */
      .stTextInput>div>div>input,
      .stTextArea>div>div>textarea,
      .stSelectbox>div>div,
      .stNumberInput>div>div>input {
        border-radius: 8px;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

header_cols = st.columns([8, 1])
with header_cols[0]:
    st.title("SEC Tools Suite")
with header_cols[1]:
    st.markdown("<div style=\"height: 1.75rem;\"></div>", unsafe_allow_html=True)
    if st.button("Logout"):
        logout()
        st.rerun()
st.caption("Unified tools to search, download, and transform SEC EDGAR filings. Your default workflow starts below.")


def run_xbrl_tool():
    st.header("XBRL to Excel")
    st.caption("Fetch XBRL JSON by accession or discover via ticker → export Excel")
    col1, col2, col3 = st.columns(3)
    with col1:
        ticker = st.text_input("Ticker (for discovery)", key="xbrl_ticker")
        accession_no = st.text_input("Accession No (optional)", key="xbrl_accession")
    with col2:
        form_type = st.text_input("Form Type", value="10-K", key="xbrl_form_type")
        htm_url = st.text_input("Filing HTML URL (optional)", key="xbrl_htm_url")
    with col3:
        xbrl_url = st.text_input("XBRL XML URL (optional)", key="xbrl_xbrl_url")
        out_dir = st.text_input("Output Dir (optional)", key="xbrl_out_dir")
    output_file = st.text_input("Output filename (optional)", key="xbrl_output_file")
    limit = st.number_input("Discovery limit", min_value=1, value=1, key="xbrl_limit")
    if st.button("Run XBRL Export"):
        args = []
        if accession_no:
            args += ["--accession-no", accession_no]
        if htm_url:
            args += ["--htm-url", htm_url]
        if xbrl_url:
            args += ["--xbrl-url", xbrl_url]
        if ticker:
            args += ["--ticker", ticker]
        if form_type:
            args += ["--form-type", form_type]
        if out_dir:
            args += ["--output-dir", out_dir]
        if output_file:
            args += ["--output-file", output_file]
        if limit:
            args += ["--limit", str(int(limit))]
        code = xbrl_main(args)
        if code == 0:
            st.success("XBRL Excel export completed. Check output folder.")
        else:
            st.error("XBRL export failed. See terminal logs.")


def run_full_text_tab():
    st.header("Full-Text Search")
    st.caption("Search filings and exhibits by text, with filters")
    # Query Builder
    with st.expander("Query builder (optional)", expanded=False):
        qb_col1, qb_col2 = st.columns(2)
        with qb_col1:
            qb_ticker = st.text_input("Ticker (ticker:AMZN)", key="fts_qb_ticker")
            qb_company = st.text_input("Company name (companyName:\"Amazon.com, Inc.\")", key="fts_qb_company")
            qb_must = st.text_input("Must include all words (AND)", key="fts_qb_must")
            qb_exact = st.text_input("Exact phrase (\"...\")", key="fts_qb_exact")
        with qb_col2:
            qb_any = st.text_input("Include any words (OR)", key="fts_qb_any")
            qb_none = st.text_input("Exclude words (-word)", key="fts_qb_none")
            qb_prefix = st.text_input("Prefix match (e.g., revenue*)", key="fts_qb_prefix")
            qb_custom = st.text_input("Custom additions", key="fts_qb_custom")

        def _build_query() -> str:
            parts = []
            if qb_ticker.strip():
                parts.append(f"ticker:{qb_ticker.strip()}")
            if qb_company.strip():
                parts.append(f"companyName:\"{qb_company.strip()}\"")
            if qb_must.strip():
                parts.extend([w for w in qb_must.strip().split()])
            if qb_exact.strip():
                parts.append(f'"{qb_exact.strip()}"')
            if qb_any.strip():
                any_parts = [w for w in qb_any.strip().split()]
                if any_parts:
                    parts.append("(" + " OR ".join(any_parts) + ")")
            if qb_none.strip():
                parts.extend([f"-{w}" for w in qb_none.strip().split()])
            if qb_prefix.strip():
                parts.append(qb_prefix.strip())
            if qb_custom.strip():
                parts.append(qb_custom.strip())
            return " AND ".join([p for p in parts if p])

        if st.button("Build query from fields"):
            st.session_state["fts_query"] = _build_query()

    query = st.text_area("Query", help="Supports quotes, OR, -, and * suffix", key="fts_query")

    # Filters
    ft_options = ["10-K", "10-Q", "8-K", "S-1", "S-3", "20-F", "6-K", "13D", "13G"]
    form_types_multi = st.multiselect("Form Types", options=ft_options, default=[], key="fts_form_types_multi")

    date_col1, date_col2 = st.columns(2)
    with date_col1:
        start_date_val = st.date_input("Start Date", key="fts_start_date_date", value=None)
    with date_col2:
        end_date_val = st.date_input("End Date", key="fts_end_date_date", value=None)

    ciks = st.text_input("CIKs (comma-separated)", key="fts_ciks")

    # Pagination controls
    if "fts_page" not in st.session_state:
        st.session_state["fts_page"] = 1
    pag_col1, pag_col2, pag_col3 = st.columns([1,1,2])
    with pag_col1:
        if st.button("Prev page"):
            st.session_state["fts_page"] = max(1, int(st.session_state["fts_page"]) - 1)
    with pag_col2:
        if st.button("Next page"):
            st.session_state["fts_page"] = int(st.session_state["fts_page"]) + 1
    with pag_col3:
        page = st.number_input("Page", min_value=1, value=int(st.session_state["fts_page"]), key="fts_page_input")
        st.session_state["fts_page"] = int(page)

    if st.button("Run Search"):
        import full_text_search as fts
        args = ["--query", query, "--page", str(int(st.session_state["fts_page"]))]
        form_types = ",".join(form_types_multi) if form_types_multi else ""
        if form_types:
            args += ["--form-types", form_types]
        start_date = start_date_val.isoformat() if start_date_val else ""
        end_date = end_date_val.isoformat() if end_date_val else ""
        if start_date:
            args += ["--start-date", start_date]
        if end_date:
            args += ["--end-date", end_date]
        if ciks:
            args += ["--ciks", ciks]
        # Capture results by calling underlying functions
        key = fts.get_api_key(None)
        res = fts.run_search(
            key,
            query,
            [ft.strip() for ft in form_types.split(',')] if form_types else None,
            start_date or None,
            end_date or None,
            [c.strip() for c in ciks.split(',')] if ciks else None,
            int(st.session_state["fts_page"]),
        )
        df = fts.to_dataframe(res)
        st.write(f"Returned {len(df)} rows (page {int(st.session_state['fts_page'])})")
        if not df.empty:
            # Column selector for display
            default_cols = [c for c in ["filingId", "formType", "ticker", "companyName", "filedAt", "linkToFilingDetails"] if c in df.columns]
            selected_cols = st.multiselect("Columns to show", options=list(df.columns), default=default_cols or list(df.columns)[:10])
            st.dataframe(df[selected_cols] if selected_cols else df)
        else:
            st.info("No results for the current query/filters.")
        if not df.empty:
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button("Download CSV", csv, file_name="full_text_results.csv", mime="text/csv")


def run_search_tab():
    st.header("Search")
    st.info("This tab is a placeholder. Please use the 'Full-Text Search' tab for advanced querying.")


def run_download_pdf_tab():
    st.header("Filing Download / PDF")
    mode = st.radio("Mode", ["Download original", "Generate PDF"], horizontal=True)
    if mode == "Download original":
        path = st.text_input("SEC URL path (after data/)", key="dl_path")
        out = st.text_input("Output file path", key="dl_out")
        if st.button("Download"):
            import filing_download_pdf as fdp
            key = fdp.get_api_key(None)
            outp = fdp.download_original(key, path, out)
            st.success(f"Saved: {outp}")
    else:
        url = st.text_input("Full sec.gov/Archives URL", key="pdf_url")
        out = st.text_input("Output PDF file path", key="pdf_out")
        if st.button("Generate PDF"):
            import filing_download_pdf as fdp
            key = fdp.get_api_key(None)
            outp = fdp.download_pdf(key, url, out)
            st.success(f"Saved: {outp}")


def run_extractor_tab():
    st.header("Extractor (10-K/10-Q/8-K)")
    sec_url = st.text_input("Filing URL (.htm or .txt)", key="ex_sec_url")
    item = st.text_input("Item code (e.g., 1A, 7, part2item1a, 2-2)", key="ex_item")
    rtype = st.selectbox("Return type", ["text", "html"], index=0, key="ex_type")
    if st.button("Extract"):
        import extractor_api as ex
        key = ex.get_api_key(None)
        content = ex.extract_item(key, sec_url, item, rtype)
        if rtype == 'html':
            st.components.v1.html(content, height=600, scrolling=True)
        else:
            st.text_area("Extracted Text", content, height=400)


def run_stream_tab():
    st.header("Stream Listener")
    st.write("Run in terminal to keep the socket open:")
    st.code("""pip install websocket-client
python stream_listener.py --out-jsonl stream.jsonl""", language="bash")


def run_automated_downloader_tab():
    st.header("Automated SEC Excel Downloader")
    st.markdown(
        "Enter the minimal details and click Run. We'll find filings within your date range, download Excel, extract Income/Balance/Cash Flow, and build consolidated workbooks."
    )
    with st.expander("What will this do?", expanded=False):
        st.markdown("- Finds filings for your ticker and form type within the specified date range.\n- Downloads Excel files and extracts the 3 main statements.\n- Creates detailed and cleaned consolidated workbooks in the appropriate `SEC_Excel_Downloads_{ticker}_{form}` folder.")

    default_ticker = "AMZN"
    default_form = "10-K"

    col1, col2, col3 = st.columns(3)
    with col1:
        ticker = st.text_input("Ticker", value=default_ticker, placeholder="e.g., AMZN, AAPL, TSLA", key="auto_ticker")
        form_options = ["10-K", "10-Q"]
        form_index = form_options.index(default_form) if default_form in form_options else 0
        form_type = st.selectbox("Form Type", form_options, index=form_index, key="auto_form_type")
        download_both = st.checkbox("Download both 10-K and 10-Q", value=False, key="auto_download_both")
        if download_both:
            st.info("Will download both 10-K and 10-Q filings")
    with col2:
        st.empty()
    with col3:
        st.empty()

    d1, d2 = st.columns(2)
    with d1:
        start_date_val = st.date_input("Start date", key="auto_start_date", value=None)
    with d2:
        end_date_val = st.date_input("End date", key="auto_end_date", value=None)

    st.divider()
    run_col, _ = st.columns([1,3])
    if run_col.button("Run Automated Download", use_container_width=True):
        try:
            import automated_sec_downloader as asd
            key = "62ff63ea351833fb6ad40b2f4becbf5539a91740ce09544e96b42600de5853c5"
            downloader = asd.AdvancedSECDownloader(key)
            sd = start_date_val.isoformat() if start_date_val else None
            ed = end_date_val.isoformat() if end_date_val else None
            
            if download_both:
                # Download both 10-K and 10-Q
                files = downloader.automated_download_with_range(
                    ticker.strip().upper(),
                    "10-K",
                    start_date=sd,
                    end_date=ed,
                    download_both=True,
                )
            else:
                # Download single form type
                files = downloader.automated_download_with_range(
                    ticker.strip().upper(),
                    form_type.strip() or "10-K",
                    start_date=sd,
                    end_date=ed,
                )
            if files:
                st.success(f"Completed. {len(files)} outputs produced.")
                st.subheader("Outputs")
                
                # Create a temporary directory for downloads
                import tempfile
                import zipfile
                import shutil
                
                for f in files:
                    try:
                        size = os.path.getsize(f)
                        filename = os.path.basename(f)
                        
                        # Display file info
                        st.markdown(f"- `{filename}` ({size:,} bytes)")
                        
                        # Add download button for each file
                        if os.path.exists(f):
                            with open(f, 'rb') as file:
                                st.download_button(
                                    label=f"📥 Download {filename}",
                                    data=file.read(),
                                    file_name=filename,
                                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                                    key=f"download_{filename}"
                                )
                    except Exception as e:
                        st.error(f"Error processing {f}: {e}")
                
                # Add download all button
                if len(files) > 1:
                    try:
                        # Create a zip file with all outputs
                        zip_buffer = tempfile.NamedTemporaryFile(delete=False, suffix='.zip')
                        with zipfile.ZipFile(zip_buffer.name, 'w', zipfile.ZIP_DEFLATED) as zip_file:
                            for f in files:
                                if os.path.exists(f):
                                    zip_file.write(f, os.path.basename(f))
                        
                        # Read the zip file
                        with open(zip_buffer.name, 'rb') as zip_file:
                            zip_data = zip_file.read()
                        
                        # Clean up
                        os.unlink(zip_buffer.name)
                        
                        # Download button for all files
                        st.download_button(
                            label="📦 Download All Files (ZIP)",
                            data=zip_data,
                            file_name=f"{ticker}_{form_type}_all_files.zip",
                            mime="application/zip",
                            key="download_all"
                        )
                    except Exception as e:
                        st.warning(f"Could not create zip file: {e}")
            else:
                st.error("⚠️ 0 files found. Please check your ticker symbol and try again.")
        except Exception as e:
            st.error(f"Error: {e}")


tabs = st.tabs(["Automated Downloader", "Search", "XBRL JSON → Excel", "Full-Text Search", "Download/PDF", "Extractor", "Stream"])
with tabs[0]:
    run_automated_downloader_tab()
with tabs[1]:
    run_search_tab()
with tabs[2]:
    run_xbrl_tool()
with tabs[3]:
    run_full_text_tab()
with tabs[4]:
    run_download_pdf_tab()
with tabs[5]:
    run_extractor_tab()
with tabs[6]:
    run_stream_tab()

