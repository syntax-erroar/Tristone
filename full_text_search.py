#!/usr/bin/env python3
"""
Full-Text Search tool

POSTs to https://api.sec-api.io/full-text-search to find filings/exhibits by text.
Outputs results to console and optionally saves to CSV/Excel.
"""

import os
import sys
import json
import argparse
from typing import Any, Dict, List, Optional

import requests
import pandas as pd


API_URL = "https://api.sec-api.io/full-text-search"


def get_api_key(cli_key: Optional[str]) -> str:
    default_key = "62ff63ea351833fb6ad40b2f4becbf5539a91740ce09544e96b42600de5853c5"
    api_key = cli_key or os.getenv("SEC_API_KEY") or os.getenv("SECAPI_TOKEN") or default_key
    if not api_key:
        raise ValueError("Missing API key. Set SEC_API_KEY or use --api-key")
    return api_key


def run_search(api_key: str, query: str, form_types: Optional[List[str]], start_date: Optional[str], end_date: Optional[str], ciks: Optional[List[str]], page: int) -> Dict[str, Any]:
    headers = {"Authorization": api_key}
    payload: Dict[str, Any] = {
        "query": query,
        "page": str(max(page, 1)),
    }
    if form_types:
        payload["formTypes"] = form_types
    if start_date:
        payload["startDate"] = start_date
    if end_date:
        payload["endDate"] = end_date
    if ciks:
        payload["ciks"] = ciks

    resp = requests.post(API_URL, headers=headers, json=payload, timeout=60)
    resp.raise_for_status()
    return resp.json()


def to_dataframe(result: Dict[str, Any]) -> pd.DataFrame:
    filings = result.get("filings", []) or []
    df = pd.json_normalize(filings)
    return df


def parse_args(argv: Optional[List[str]] = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(description="SEC Full-Text Search tool")
    p.add_argument("--query", required=True, help="Search query string; supports quotes, OR, -, and * suffix")
    p.add_argument("--form-types", help="Comma-separated form types, e.g. 8-K,10-Q")
    p.add_argument("--start-date", help="yyyy-mm-dd")
    p.add_argument("--end-date", help="yyyy-mm-dd")
    p.add_argument("--ciks", help="Comma-separated CIKs")
    p.add_argument("--page", type=int, default=1, help="Page number (100 results per page)")
    p.add_argument("--api-key", dest="api_key", help="API key; else uses SEC_API_KEY env or default")
    p.add_argument("--output", help="Output file path (.csv or .xlsx)")
    return p.parse_args(argv)


def main(argv: Optional[List[str]] = None) -> int:
    args = parse_args(argv)
    try:
        api_key = get_api_key(args.api_key)
        form_types = [ft.strip() for ft in args.form_types.split(',')] if args.form_types else None
        ciks = [c.strip() for c in args.ciks.split(',')] if args.ciks else None
        res = run_search(api_key, args.query, form_types, args.start_date, args.end_date, ciks, args.page)
        df = to_dataframe(res)
        print(f"Total returned: {len(df)} rows (page {args.page})")
        if args.output:
            if args.output.lower().endswith('.xlsx'):
                with pd.ExcelWriter(args.output, engine='openpyxl') as w:
                    df.to_excel(w, index=False, sheet_name='Results')
            else:
                df.to_csv(args.output, index=False)
            print(f"✅ Saved to {args.output}")
        else:
            print(df.head(20).to_string(index=False))
        return 0
    except Exception as e:
        print(f"❌ Error: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())


