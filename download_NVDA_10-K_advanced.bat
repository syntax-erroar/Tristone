@echo off
REM Advanced SEC Excel Downloader
REM Generated on 2025-10-07 17:25:40

echo Starting automated SEC Excel download for NVDA 10-K...
echo.

REM Create download directory
if not exist "SEC_Excel_Downloads_NVDA_10-K" mkdir "SEC_Excel_Downloads_NVDA_10-K"
cd "SEC_Excel_Downloads_NVDA_10-K"

echo Download directory created: SEC_Excel_Downloads_NVDA_10-K
echo.

REM Filing #1: NVIDIA CORP
echo Downloading filing #1...
echo URL: https://www.sec.gov/Archives/edgar/data/1045810/000104581025000023/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "NVDA_10-K_FY2025_0001045810_25_000023.xlsx" "https://www.sec.gov/Archives/edgar/data/1045810/000104581025000023/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded NVDA_10-K_FY2025_0001045810_25_000023.xlsx
) else (
    echo ERROR: Curl failed for NVDA_10-K_FY2025_0001045810_25_000023.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #2: NVIDIA CORP
echo Downloading filing #2...
echo URL: https://www.sec.gov/Archives/edgar/data/1045810/000104581024000029/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "NVDA_10-K_FY2024_0001045810_24_000029.xlsx" "https://www.sec.gov/Archives/edgar/data/1045810/000104581024000029/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded NVDA_10-K_FY2024_0001045810_24_000029.xlsx
) else (
    echo ERROR: Curl failed for NVDA_10-K_FY2024_0001045810_24_000029.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #3: NVIDIA CORP
echo Downloading filing #3...
echo URL: https://www.sec.gov/Archives/edgar/data/1045810/000104581023000017/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "NVDA_10-K_FY2023_0001045810_23_000017.xlsx" "https://www.sec.gov/Archives/edgar/data/1045810/000104581023000017/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded NVDA_10-K_FY2023_0001045810_23_000017.xlsx
) else (
    echo ERROR: Curl failed for NVDA_10-K_FY2023_0001045810_23_000017.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.


echo.
echo Download complete! Check the SEC_Excel_Downloads folder.
pause
