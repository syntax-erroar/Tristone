#!/usr/bin/env python3
"""
XBRL to JSON → Excel exporter

Uses SEC API's xbrl-to-json endpoint to fetch standardized JSON for a filing
and exports a multi-sheet Excel file:
- One sheet per statement (e.g., StatementsOfIncome, BalanceSheets, etc.)
- A CoverPage sheet with key cover fields

Authentication:
- Provide API key via env var SEC_API_KEY or --api-key argument.

Inputs (choose one):
- --accession-no  e.g. 0001564590-21-004599
- --htm-url       e.g. https://www.sec.gov/Archives/.../tsla-10k_20201231.htm
- --xbrl-url      e.g. https://www.sec.gov/Archives/.../tsla-10k_20201231_htm.xml

Optional:
- --ticker and --form-type for output folder naming consistent with existing scripts
- --output-dir to override destination directory
- --output-file to override Excel filename

Dependencies: requests, pandas, openpyxl
"""

import os
import sys
import json
import argparse
from datetime import datetime
from typing import Any, Dict, Iterable, List, Optional, Tuple, Union

import requests
import pandas as pd


API_BASE = "https://api.sec-api.io/xbrl-to-json"
QUERY_API = "https://api.sec-api.io"


def build_query_params(args: argparse.Namespace) -> Dict[str, str]:
    # Deprecated: minimal CLI no longer uses direct IDs/URLs
    return {}


def get_api_key(args: argparse.Namespace) -> str:
    # Default to same key used in automated_sec_downloader.py if not provided
    default_key = "62ff63ea351833fb6ad40b2f4becbf5539a91740ce09544e96b42600de5853c5"
    api_key = args.api_key or os.getenv("SEC_API_KEY") or os.getenv("SECAPI_TOKEN") or default_key
    if not api_key:
        raise ValueError("API key missing. Set SEC_API_KEY env var or pass --api-key.")
    return api_key


def fetch_xbrl_json(params: Dict[str, str], api_key: str, timeout: int = 60) -> Dict[str, Any]:
    headers = {"Authorization": api_key}
    resp = requests.get(API_BASE, params=params, headers=headers, timeout=timeout)
    if resp.status_code != 200:
        raise RuntimeError(f"HTTP {resp.status_code} - {resp.text[:500]}")
    try:
        data = resp.json()
    except json.JSONDecodeError:
        raise RuntimeError("Response is not valid JSON")
    if not isinstance(data, dict) or not data:
        raise RuntimeError("Empty or unexpected JSON structure from API")
    return data


def _normalize_form_types(form_type_input: Optional[str]) -> List[str]:
    if not form_type_input:
        return ["10-K"]
    raw = form_type_input.strip().lower()
    if raw == "all":
        return ["10-K", "10-Q", "8-K"]
    parts = [p.strip() for p in raw.replace(";", ",").split(",") if p.strip()]
    normalized: List[str] = []
    for p in parts:
        p_clean = p.replace(" ", "").replace("_", "-")
        if p_clean in ["10k", "10-k"]:
            normalized.append("10-K")
        elif p_clean in ["10q", "10-q"]:
            normalized.append("10-Q")
        elif p_clean in ["8k", "8-k"]:
            normalized.append("8-K")
        else:
            normalized.append(p.upper())
    out: List[str] = []
    seen = set()
    for f in normalized:
        if f not in seen:
            out.append(f); seen.add(f)
    return out or ["10-K"]


def _build_form_query(form_types: List[str]) -> str:
    if not form_types:
        return 'formType:"10-K"'
    if len(form_types) == 1:
        return f'formType:"{form_types[0]}"'
    ors = " OR ".join([f'formType:"{ft}"' for ft in form_types])
    return f"({ors})"


def search_filings_for_accession(api_key: str, ticker: str, form_type: str = "10-K", limit: int = 1) -> Optional[str]:
    form_types = _normalize_form_types(form_type)
    payload = {
        "query": f"ticker:{ticker} AND {_build_form_query(form_types)}",
        "from": "0",
        "size": str(min(max(limit, 1), 50)),
        "sort": [{"filedAt": {"order": "desc"}}]
    }
    url = f"{QUERY_API}?token={api_key}"
    try:
        r = requests.post(url, json=payload, timeout=30)
        r.raise_for_status()
        data = r.json()
        filings = data.get("filings", [])
        if not filings:
            return None
        return filings[0].get("accessionNo")
    except Exception:
        return None


def search_filings_for_accessions(api_key: str, ticker: str, form_type: str = "10-K", limit: int = 3) -> List[Dict[str, Any]]:
    """Return up to 'limit' recent filings with accessionNo, cik, filedAt."""
    form_types = _normalize_form_types(form_type)
    payload = {
        "query": f"ticker:{ticker} AND {_build_form_query(form_types)}",
        "from": "0",
        "size": str(min(max(limit, 1), 50)),
        "sort": [{"filedAt": {"order": "desc"}}]
    }
    url = f"{QUERY_API}?token={api_key}"
    try:
        r = requests.post(url, json=payload, timeout=30)
        r.raise_for_status()
        data = r.json()
        filings = data.get("filings", []) or []
        out: List[Dict[str, Any]] = []
        for f in filings[:limit]:
            out.append({
                "accessionNo": f.get("accessionNo"),
                "cik": f.get("cik"),
                "filedAt": f.get("filedAt"),
                "formType": f.get("formType"),
            })
        return out
    except Exception:
        return []


def normalize_segment(segment: Union[Dict[str, Any], List[Dict[str, Any]], None]) -> Tuple[str, str]:
    if segment is None:
        return "", ""
    if isinstance(segment, dict):
        return segment.get("dimension", ""), segment.get("value", "")
    if isinstance(segment, list) and segment:
        dims = []
        vals = []
        for s in segment:
            dims.append(str(s.get("dimension", "")))
            vals.append(str(s.get("value", "")))
        return "; ".join(dims), "; ".join(vals)
    return "", ""


def normalize_period(period: Dict[str, Any]) -> Tuple[Optional[str], Optional[str], Optional[str]]:
    if not isinstance(period, dict):
        return None, None, None
    # Income statement items usually have startDate/endDate; balance sheet has instant
    return (
        period.get("startDate"),
        period.get("endDate"),
        period.get("instant"),
    )


def flatten_statement(statement_name: str, statement_obj: Dict[str, Any]) -> pd.DataFrame:
    rows: List[Dict[str, Any]] = []
    for item_name, facts in statement_obj.items():
        if not isinstance(facts, list):
            # Some entries can be scalars or objects; coerce to list
            facts = [facts]
        for fact in facts:
            if not isinstance(fact, dict):
                rows.append({
                    "USGAAP_Item": item_name,
                    "Value": fact,
                })
                continue
            start_date, end_date, instant = normalize_period(fact.get("period", {}))
            dim, dim_val = normalize_segment(fact.get("segment"))
            row = {
                "Statement": statement_name,
                "USGAAP_Item": item_name,
                "StartDate": start_date,
                "EndDate": end_date,
                "Instant": instant,
                "UnitRef": fact.get("unitRef"),
                "Decimals": fact.get("decimals"),
                "SegmentDimension": dim,
                "SegmentValue": dim_val,
                "Value": fact.get("value"),
            }
            rows.append(row)
    df = pd.DataFrame(rows)
    # Order columns for readability
    preferred_cols = [
        "Statement", "USGAAP_Item", "StartDate", "EndDate", "Instant",
        "UnitRef", "Decimals", "SegmentDimension", "SegmentValue", "Value",
    ]
    other_cols = [c for c in df.columns if c not in preferred_cols]
    return df[preferred_cols + other_cols]


def extract_cover_page(cover: Dict[str, Any]) -> pd.DataFrame:
    # Flatten shallow key/values; nested arrays/objects are stringified for convenience
    rows: List[Dict[str, Any]] = []
    for key, value in cover.items():
        if isinstance(value, (dict, list)):
            safe_value = json.dumps(value)[:200000]  # avoid overly large cells
        else:
            safe_value = value
        rows.append({"Field": key, "Value": safe_value})
    return pd.DataFrame(rows)


def default_output_dir(ticker: Optional[str], form_type: Optional[str]) -> str:
    if ticker and form_type:
        return f"SEC_Excel_Downloads_{ticker}_{form_type}_XBRL_JSON"
    return "SEC_Excel_Downloads_XBRL_JSON"


def default_filename(ticker: Optional[str], form_type: Optional[str], accession_no: Optional[str]) -> str:
    time_tag = datetime.now().strftime("%Y%m%d_%H%M%S")
    base = "XBRL_JSON_Export"
    if ticker and form_type:
        base = f"{ticker}_{form_type}_{base}"
    if accession_no:
        acc_clean = accession_no.replace("-", "")
        base = f"{base}_{acc_clean}"
    return f"{base}_{time_tag}.xlsx"


def write_excel(output_path: str, sheets: Dict[str, pd.DataFrame]) -> None:
    # Use openpyxl engine implicitly through pandas
    with pd.ExcelWriter(output_path, engine="openpyxl") as writer:
        for name, df in sheets.items():
            safe_name = name[:31] if len(name) > 31 else name
            # Empty DataFrame guard
            if df is None or df.empty:
                empty_df = pd.DataFrame({"Info": ["No data"]})
                empty_df.to_excel(writer, index=False, sheet_name=safe_name)
            else:
                df.to_excel(writer, index=False, sheet_name=safe_name)


def export_to_excel(data: Dict[str, Any], output_path: str) -> None:
    sheets: Dict[str, pd.DataFrame] = {}

    # CoverPage
    cover = data.get("CoverPage")
    if isinstance(cover, dict) and cover:
        sheets["CoverPage"] = extract_cover_page(cover)

    # Known statement groups to flatten
    statement_keys = [
        "StatementsOfIncome",
        "StatementsOfIncomeParenthetical",
        "StatementsOfComprehensiveIncome",
        "StatementsOfComprehensiveIncomeParenthetical",
        "BalanceSheets",
        "BalanceSheetsParenthetical",
        "StatementsOfCashFlows",
        "StatementsOfCashFlowsParenthetical",
        "StatementsOfShareholdersEquity",
        "StatementsOfShareholdersEquityParenthetical",
    ]

    for key in statement_keys:
        obj = data.get(key)
        if isinstance(obj, dict) and obj:
            sheets[key] = flatten_statement(key, obj)

    # Any additional top-level sections (notes, tables, etc.) are written as raw JSON
    # in a separate sheet list to avoid exploding sheet count. We'll include a catalog.
    other_keys = [k for k in data.keys() if k not in sheets and k != "CoverPage"]
    catalog_rows = []
    for k in other_keys:
        try:
            size_hint = len(json.dumps(data.get(k, {})))
        except Exception:
            size_hint = None
        catalog_rows.append({"Section": k, "Type": type(data.get(k)).__name__, "SizeHint": size_hint})
    if catalog_rows:
        sheets["OtherSectionsCatalog"] = pd.DataFrame(catalog_rows)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    write_excel(output_path, sheets)


def export_batch_xbrl(
    api_key: str,
    filings: List[Dict[str, Any]],
    ticker: str,
    form_type: str,
    output_dir: str,
) -> List[str]:
    """Fetch XBRL JSON and write one Excel per filing; return file paths."""
    os.makedirs(output_dir, exist_ok=True)
    written: List[str] = []
    for idx, f in enumerate(filings, start=1):
        acc = (f.get("accessionNo") or "").strip()
        if not acc:
            continue
        params = {"accession-no": acc}
        data = fetch_xbrl_json(params, api_key)
        acc_clean = acc.replace("-", "")
        filename = f"{ticker}_{form_type}_{idx}_{acc_clean}_XBRL_JSON.xlsx"
        out_path = os.path.join(output_dir, filename)
        export_to_excel(data, out_path)
        written.append(out_path)
    return written


def write_batch_summary(file_paths: List[str], output_dir: str, ticker: str, form_type: str) -> Optional[str]:
    """Write a simple summary CSV listing generated files."""
    try:
        rows = []
        for p in file_paths:
            try:
                size = os.path.getsize(p)
            except Exception:
                size = None
            rows.append({"File": p, "SizeBytes": size})
        if not rows:
            return None
        df = pd.DataFrame(rows)
        out_csv = os.path.join(output_dir, f"{ticker}_{form_type}_XBRL_JSON_Files.csv")
        df.to_csv(out_csv, index=False)
        return out_csv
    except Exception:
        return None


def parse_args(argv: Optional[List[str]] = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(description="XBRL → Excel (minimal): provide ticker, optional form and limit")
    p.add_argument("--ticker", required=True, help="Ticker, e.g. AMZN")
    p.add_argument("--form-type", default="10-K", help="Form type: 10-K, 10-Q, 8-K (default 10-K)")
    p.add_argument("--limit", type=int, default=1, help="How many recent filings to export (default 1)")
    p.add_argument("--output-dir", help="Destination directory (default uses SEC_Excel_Downloads_{ticker}_{form}_XBRL_JSON)")
    return p.parse_args(argv)


def main(argv: Optional[List[str]] = None) -> int:
    args = parse_args(argv)
    try:
        api_key = get_api_key(args)
        ticker = args.ticker.strip().upper()
        form_type = (args.form_type or "10-K").strip()
        limit = max(1, int(args.limit or 1))
        out_dir = args.output_dir or default_output_dir(ticker, form_type)

        filings = search_filings_for_accessions(api_key, ticker, form_type, limit)
        if not filings:
            raise RuntimeError("Could not discover filings via Query API")
        written = export_batch_xbrl(api_key, filings, ticker, form_type, out_dir)
        summary = write_batch_summary(written, out_dir, ticker, form_type)
        print(f"✅ Batch completed: {len(written)} files")
        if summary:
            print(f"📄 Summary CSV: {summary}")
        return 0
    except Exception as e:
        print(f"❌ Error: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())


