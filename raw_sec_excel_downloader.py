#!/usr/bin/env python3
"""
Raw SEC Excel Downloader (inspired by automated_sec_downloader.py)

- Uses curl/wget/advanced requests with proper headers
- Saves the RAW Excel file only (no processing)
- Verifies integrity (PK magic bytes, non-empty)
"""

import os
import subprocess
import random
import time
from typing import Optional
import requests


class RawSECDownloader:
    def __init__(self):
        self.sec_base_url = "https://www.sec.gov"
        self.user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/121.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Safari/605.1.15'
        ]

    def _is_valid_excel(self, file_path: str) -> bool:
        if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
            return False
        try:
            with open(file_path, 'rb') as f:
                magic = f.read(4)
            # XLSX files are zip files beginning with PK\x03\x04
            return magic.startswith(b'PK')
        except Exception:
            return False

    def download_with_curl(self, url: str, output_file: str) -> bool:
        try:
            print("🔄 Trying curl...")
            cmd = [
                'curl',
                '-L',
                '-H', 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
                '-H', 'Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet,application/vnd.ms-excel,*/*',
                '-H', 'Accept-Language: en-US,en;q=0.9',
                '-H', 'Accept-Encoding: gzip, deflate, br',
                '-H', 'Connection: keep-alive',
                '-H', 'Upgrade-Insecure-Requests: 1',
                '--compressed',
                '--retry', '3',
                '--retry-delay', '2',
                '-o', output_file,
                url
            ]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            if result.returncode == 0 and self._is_valid_excel(output_file):
                print("✅ curl succeeded and file looks like a valid Excel (PK)")
                return True
            else:
                print(f"❌ curl failed or file invalid. rc={result.returncode}")
                if result.stderr:
                    print(result.stderr)
                return False
        except Exception as e:
            print(f"❌ curl error: {e}")
            return False

    def download_with_wget(self, url: str, output_file: str) -> bool:
        try:
            print("🔄 Trying wget...")
            cmd = [
                'wget',
                '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
                '--header=Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                '--header=Accept-Language: en-US,en;q=0.9',
                '--retry=3',
                '--wait=2',
                '--random-wait',
                '-O', output_file,
                url
            ]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            if result.returncode == 0 and self._is_valid_excel(output_file):
                print("✅ wget succeeded and file looks like a valid Excel (PK)")
                return True
            else:
                print(f"❌ wget failed or file invalid. rc={result.returncode}")
                if result.stderr:
                    print(result.stderr)
                return False
        except Exception as e:
            print(f"❌ wget error: {e}")
            return False

    def download_with_requests_advanced(self, url: str, output_file: str) -> bool:
        try:
            print("🔄 Trying advanced requests...")
            session = requests.Session()
            ua = random.choice(self.user_agents)
            session.headers.update({
                'User-Agent': ua,
                'Accept': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet,application/vnd.ms-excel,application/octet-stream,*/*',
                'Accept-Language': 'en-US,en;q=0.9',
                'Accept-Encoding': 'gzip, deflate, br',
                'Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'none',
                'Cache-Control': 'max-age=0',
                'Referer': 'https://www.sec.gov/'
            })
            time.sleep(random.uniform(1, 3))
            resp = session.get(url, timeout=30, allow_redirects=True)
            if resp.status_code == 200:
                with open(output_file, 'wb') as f:
                    f.write(resp.content)
                if self._is_valid_excel(output_file):
                    print("✅ requests succeeded and file looks like a valid Excel (PK)")
                    return True
                else:
                    print("⚠️ requests wrote a file but it doesn't look like XLSX (no PK)")
                    return False
            else:
                print(f"❌ HTTP {resp.status_code}: {resp.reason}")
                return False
        except Exception as e:
            print(f"❌ requests error: {e}")
            return False

    def download_excel_raw(self, accession_no: str, cik: str, output_dir: str, filename: str) -> Optional[str]:
        clean_accession = accession_no.replace('-', '')
        url = f"{self.sec_base_url}/Archives/edgar/data/{cik}/{clean_accession}/Financial_Report.xlsx"
        os.makedirs(output_dir, exist_ok=True)
        out_path = os.path.join(output_dir, filename)

        print(f"\n📥 RAW download: {filename}")
        print(f"🔗 URL: {url}")

        methods = [
            ("curl", lambda: self.download_with_curl(url, out_path)),
            ("wget", lambda: self.download_with_wget(url, out_path)),
            ("requests", lambda: self.download_with_requests_advanced(url, out_path)),
        ]

        for name, fn in methods:
            try:
                if fn():
                    size = os.path.getsize(out_path) if os.path.exists(out_path) else 0
                    print(f"✅ RAW file saved: {out_path} ({size:,} bytes)")
                    return out_path
            except Exception as e:
                print(f"⚠️ {name} failed: {e}")
                continue

        print("❌ All methods failed for RAW download")
        return None


def main():
    # Example: AMZN 10-K 2024 (accession 0001018724-24-000008)
    cik = "0001018724"
    accession_no = "0001018724-24-000008"
    output_dir = "SEC_Excel_Downloads_AMZN_10-K_Raw"
    filename = "AMZN_10-K_2_0001018724_24_000008_RAW.xlsx"

    print("🤖 Raw SEC Excel Downloader")
    print("=" * 40)
    d = RawSECDownloader()
    path = d.download_excel_raw(accession_no, cik, output_dir, filename)
    if path and os.path.exists(path):
        # Final integrity note
        with open(path, 'rb') as f:
            magic = f.read(4)
        if magic.startswith(b'PK'):
            print("📦 File has valid XLSX magic bytes (PK)")
        else:
            print("⚠️ File does not have XLSX magic bytes. It might be an error page.")


if __name__ == "__main__":
    main()



