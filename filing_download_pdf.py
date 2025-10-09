#!/usr/bin/env python3
"""
Filing Download & PDF Generator tool

Download any original SEC EDGAR file via archive.sec-api.io or generate a PDF
via https://api.sec-api.io/filing-reader?token=...&url=...
"""

import os
import sys
import argparse
from typing import Optional

import requests


ARCHIVE_BASE = "https://archive.sec-api.io"
PDF_API = "https://api.sec-api.io/filing-reader"


def get_api_key(cli_key: Optional[str]) -> str:
    default_key = "62ff63ea351833fb6ad40b2f4becbf5539a91740ce09544e96b42600de5853c5"
    api_key = cli_key or os.getenv("SEC_API_KEY") or os.getenv("SECAPI_TOKEN") or default_key
    if not api_key:
        raise ValueError("Missing API key. Set SEC_API_KEY or use --api-key")
    return api_key


def download_original(api_key: str, sec_url_path: str, out_path: str) -> str:
    # sec_url_path should look like: 815094/000156459021006205/abmd-8k_20210211.htm
    url = f"{ARCHIVE_BASE}/{sec_url_path}?token={api_key}"
    r = requests.get(url, timeout=120)
    r.raise_for_status()
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    with open(out_path, 'wb') as f:
        f.write(r.content)
    return out_path


def download_pdf(api_key: str, sec_full_url: str, out_pdf: str) -> str:
    params = {"token": api_key, "url": sec_full_url}
    r = requests.get(PDF_API, params=params, timeout=180)
    r.raise_for_status()
    os.makedirs(os.path.dirname(out_pdf) or ".", exist_ok=True)
    with open(out_pdf, 'wb') as f:
        f.write(r.content)
    return out_pdf


def parse_args(argv=None):
    p = argparse.ArgumentParser(description="Download SEC files or generate PDFs")
    sub = p.add_subparsers(dest="cmd", required=True)

    p1 = sub.add_parser("orig", help="Download original file via archive.sec-api.io")
    p1.add_argument("--sec-url-path", required=True, help="Path after data/, e.g. 815094/000.../file.htm")
    p1.add_argument("--out", required=True, help="Output path for downloaded file")
    p1.add_argument("--api-key", dest="api_key")

    p2 = sub.add_parser("pdf", help="Generate PDF for a sec.gov/Archives URL")
    p2.add_argument("--sec-url", required=True, help="Full sec.gov/Archives URL of filing/exhibit")
    p2.add_argument("--out", required=True, help="Output PDF path")
    p2.add_argument("--api-key", dest="api_key")

    return p.parse_args(argv)


def main(argv=None) -> int:
    args = parse_args(argv)
    try:
        api_key = get_api_key(getattr(args, 'api_key', None))
        if args.cmd == 'orig':
            out = download_original(api_key, args.sec_url_path, args.out)
        else:
            out = download_pdf(api_key, args.sec_url, args.out)
        print(f"✅ Saved: {out}")
        return 0
    except Exception as e:
        print(f"❌ Error: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())


