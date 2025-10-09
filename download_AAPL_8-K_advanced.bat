@echo off
REM Advanced SEC Excel Downloader
REM Generated on 2025-10-05 18:29:42

echo Starting automated SEC Excel download for AAPL 8-K...
echo.

REM Create download directory
if not exist "SEC_Excel_Downloads_AAPL_8-K" mkdir "SEC_Excel_Downloads_AAPL_8-K"
cd "SEC_Excel_Downloads_AAPL_8-K"

echo Download directory created: SEC_Excel_Downloads_AAPL_8-K
echo.

REM Filing #1: Apple Inc.
echo Downloading filing #1...
echo URL: https://www.sec.gov/Archives/edgar/data/320193/000032019325000071/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "AAPL_8-K_1_0000320193_25_000071.xlsx" "https://www.sec.gov/Archives/edgar/data/320193/000032019325000071/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded AAPL_8-K_1_0000320193_25_000071.xlsx
) else (
    echo ERROR: Curl failed for AAPL_8-K_1_0000320193_25_000071.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #2: Apple Inc.
echo Downloading filing #2...
echo URL: https://www.sec.gov/Archives/edgar/data/320193/000114036125027340/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "AAPL_8-K_2_0001140361_25_027340.xlsx" "https://www.sec.gov/Archives/edgar/data/320193/000114036125027340/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded AAPL_8-K_2_0001140361_25_027340.xlsx
) else (
    echo ERROR: Curl failed for AAPL_8-K_2_0001140361_25_027340.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #3: Apple Inc.
echo Downloading filing #3...
echo URL: https://www.sec.gov/Archives/edgar/data/320193/000114036125025275/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "AAPL_8-K_3_0001140361_25_025275.xlsx" "https://www.sec.gov/Archives/edgar/data/320193/000114036125025275/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded AAPL_8-K_3_0001140361_25_025275.xlsx
) else (
    echo ERROR: Curl failed for AAPL_8-K_3_0001140361_25_025275.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #4: Apple Inc.
echo Downloading filing #4...
echo URL: https://www.sec.gov/Archives/edgar/data/320193/000114036125018400/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "AAPL_8-K_4_0001140361_25_018400.xlsx" "https://www.sec.gov/Archives/edgar/data/320193/000114036125018400/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded AAPL_8-K_4_0001140361_25_018400.xlsx
) else (
    echo ERROR: Curl failed for AAPL_8-K_4_0001140361_25_018400.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #5: Apple Inc.
echo Downloading filing #5...
echo URL: https://www.sec.gov/Archives/edgar/data/320193/000032019325000055/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "AAPL_8-K_5_0000320193_25_000055.xlsx" "https://www.sec.gov/Archives/edgar/data/320193/000032019325000055/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded AAPL_8-K_5_0000320193_25_000055.xlsx
) else (
    echo ERROR: Curl failed for AAPL_8-K_5_0000320193_25_000055.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.


echo.
echo Download complete! Check the SEC_Excel_Downloads folder.
pause
