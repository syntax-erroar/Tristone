#!/usr/bin/env python3
"""
Real-time Filing Stream listener

Connects to wss://stream.sec-api.io?apiKey=YOUR_API_KEY and prints filing metadata.
Can optionally write a rolling JSONL file.
"""

import os
import sys
import json
import argparse
from typing import Optional


def get_api_key(cli_key: Optional[str]) -> str:
    default_key = "62ff63ea351833fb6ad40b2f4becbf5539a91740ce09544e96b42600de5853c5"
    api_key = cli_key or os.getenv("SEC_API_KEY") or os.getenv("SECAPI_TOKEN") or default_key
    if not api_key:
        raise ValueError("Missing API key. Set SEC_API_KEY or use --api-key")
    return api_key


def listen_stream(api_key: str, out_jsonl: Optional[str] = None):
    try:
        import websocket  # websocket-client
    except Exception:
        print("Please install websocket-client: pip install websocket-client")
        return 1

    url = f"wss://stream.sec-api.io?apiKey={api_key}"
    ws = websocket.WebSocket()
    ws.connect(url, timeout=10)
    print("✅ Connected to Stream API. Press Ctrl+C to stop.")

    fp = open(out_jsonl, 'a', encoding='utf-8') if out_jsonl else None
    try:
        while True:
            msg = ws.recv()
            if not msg:
                continue
            # Message is a stringified JSON array
            try:
                data = json.loads(msg)
            except Exception:
                print(msg)
                if fp:
                    fp.write(msg + "\n")
                continue
            # Print compact summary
            for filing in data:
                accession = filing.get('accessionNo')
                form = filing.get('formType')
                ticker = filing.get('ticker')
                filed_at = filing.get('filedAt')
                link = filing.get('linkToHtml') or filing.get('linkToFilingDetails')
                print(f"[{filed_at}] {ticker} {form} {accession} -> {link}")
            if fp:
                fp.write(json.dumps(data) + "\n")
                fp.flush()
    except KeyboardInterrupt:
        print("\n🛑 Stopped by user")
    finally:
        try:
            ws.close()
        except Exception:
            pass
        if fp:
            fp.close()
    return 0


def parse_args(argv=None):
    p = argparse.ArgumentParser(description="Listen to SEC Stream API and print filings")
    p.add_argument("--api-key", dest="api_key", help="API key; else uses SEC_API_KEY env or default")
    p.add_argument("--out-jsonl", help="Path to append JSONL stream messages")
    return p.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)
    api_key = get_api_key(args.api_key)
    return listen_stream(api_key, args.out_jsonl)


if __name__ == "__main__":
    sys.exit(main())


