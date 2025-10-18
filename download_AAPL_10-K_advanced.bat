@echo off
REM Advanced SEC Excel Downloader
REM Generated on 2025-10-18 14:31:11

echo Starting automated SEC Excel download for AAPL 10-K...
echo.

REM Create download directory
if not exist "SEC_Excel_Downloads_AAPL_10-K" mkdir "SEC_Excel_Downloads_AAPL_10-K"
cd "SEC_Excel_Downloads_AAPL_10-K"

echo Download directory created: SEC_Excel_Downloads_AAPL_10-K
echo.

REM Filing #1: Apple Inc.
echo Downloading filing #1...
echo URL: https://www.sec.gov/Archives/edgar/data/320193/000032019324000123/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "AAPL_10-K_FY2024_0000320193_24_000123.xlsx" "https://www.sec.gov/Archives/edgar/data/320193/000032019324000123/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded AAPL_10-K_FY2024_0000320193_24_000123.xlsx
) else (
    echo ERROR: Curl failed for AAPL_10-K_FY2024_0000320193_24_000123.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #2: Apple Inc.
echo Downloading filing #2...
echo URL: https://www.sec.gov/Archives/edgar/data/320193/000032019323000106/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "AAPL_10-K_FY2023_0000320193_23_000106.xlsx" "https://www.sec.gov/Archives/edgar/data/320193/000032019323000106/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded AAPL_10-K_FY2023_0000320193_23_000106.xlsx
) else (
    echo ERROR: Curl failed for AAPL_10-K_FY2023_0000320193_23_000106.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #3: Apple Inc.
echo Downloading filing #3...
echo URL: https://www.sec.gov/Archives/edgar/data/320193/000032019322000108/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "AAPL_10-K_FY2022_0000320193_22_000108.xlsx" "https://www.sec.gov/Archives/edgar/data/320193/000032019322000108/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded AAPL_10-K_FY2022_0000320193_22_000108.xlsx
) else (
    echo ERROR: Curl failed for AAPL_10-K_FY2022_0000320193_22_000108.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #4: Apple Inc.
echo Downloading filing #4...
echo URL: https://www.sec.gov/Archives/edgar/data/320193/000032019321000105/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "AAPL_10-K_FY2021_0000320193_21_000105.xlsx" "https://www.sec.gov/Archives/edgar/data/320193/000032019321000105/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded AAPL_10-K_FY2021_0000320193_21_000105.xlsx
) else (
    echo ERROR: Curl failed for AAPL_10-K_FY2021_0000320193_21_000105.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #5: Apple Inc.
echo Downloading filing #5...
echo URL: https://www.sec.gov/Archives/edgar/data/320193/000032019320000096/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "AAPL_10-K_FY2020_0000320193_20_000096.xlsx" "https://www.sec.gov/Archives/edgar/data/320193/000032019320000096/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded AAPL_10-K_FY2020_0000320193_20_000096.xlsx
) else (
    echo ERROR: Curl failed for AAPL_10-K_FY2020_0000320193_20_000096.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.


echo.
echo Download complete! Check the SEC_Excel_Downloads folder.
pause
