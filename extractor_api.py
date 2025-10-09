#!/usr/bin/env python3
"""
Extractor API tool

Extracts a specific section from 10-K/10-Q/8-K filings and returns text or HTML.
GET https://api.sec-api.io/extractor?url=...&item=...&type=text|html&token=API_KEY
"""

import os
import sys
import argparse
from typing import Optional

import requests


EXTRACTOR_API = "https://api.sec-api.io/extractor"


def get_api_key(cli_key: Optional[str]) -> str:
    default_key = "62ff63ea351833fb6ad40b2f4becbf5539a91740ce09544e96b42600de5853c5"
    api_key = cli_key or os.getenv("SEC_API_KEY") or os.getenv("SECAPI_TOKEN") or default_key
    if not api_key:
        raise ValueError("Missing API key. Set SEC_API_KEY or use --api-key")
    return api_key


def extract_item(api_key: str, sec_url: str, item: str, return_type: str) -> str:
    params = {
        "token": api_key,
        "url": sec_url,
        "item": item,
        "type": return_type,
    }
    r = requests.get(EXTRACTOR_API, params=params, timeout=120)
    r.raise_for_status()
    return r.text


def parse_args(argv=None):
    p = argparse.ArgumentParser(description="Extractor API tool for 10-K/10-Q/8-K sections")
    p.add_argument("--sec-url", required=True, help="SEC filing URL (.htm/.txt)")
    p.add_argument("--item", required=True, help="Item code, e.g. 1A, 7, part2item1a, 2-2, etc.")
    p.add_argument("--type", dest="return_type", default="text", choices=["text", "html"], help="Return type")
    p.add_argument("--api-key", dest="api_key")
    p.add_argument("--out", help="Optional output file to save content")
    return p.parse_args(argv)


def main(argv=None) -> int:
    args = parse_args(argv)
    try:
        api_key = get_api_key(args.api_key)
        content = extract_item(api_key, args.sec_url, args.item, args.return_type)
        if args.out:
            mode = 'wb' if args.return_type == 'html' else 'w'
            os.makedirs(os.path.dirname(args.out) or ".", exist_ok=True)
            with open(args.out, mode) as f:
                if args.return_type == 'html':
                    f.write(content.encode('utf-8'))
                else:
                    f.write(content)
            print(f"✅ Saved to {args.out}")
        else:
            print(content[:2000])
            if len(content) > 2000:
                print("\n... (truncated)")
        return 0
    except Exception as e:
        print(f"❌ Error: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())


