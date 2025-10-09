@echo off
REM Advanced SEC Excel Downloader
REM Generated on 2025-10-09 11:39:00

echo Starting automated SEC Excel download for AMZN 10-K...
echo.

REM Create download directory
if not exist "SEC_Excel_Downloads_AMZN_10-K" mkdir "SEC_Excel_Downloads_AMZN_10-K"
cd "SEC_Excel_Downloads_AMZN_10-K"

echo Download directory created: SEC_Excel_Downloads_AMZN_10-K
echo.

REM Filing #1: AMAZON COM INC
echo Downloading filing #1...
echo URL: https://www.sec.gov/Archives/edgar/data/1018724/000101872425000004/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "AMZN_10-K_FY2024_0001018724_25_000004.xlsx" "https://www.sec.gov/Archives/edgar/data/1018724/000101872425000004/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded AMZN_10-K_FY2024_0001018724_25_000004.xlsx
) else (
    echo ERROR: Curl failed for AMZN_10-K_FY2024_0001018724_25_000004.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #2: AMAZON COM INC
echo Downloading filing #2...
echo URL: https://www.sec.gov/Archives/edgar/data/1018724/000101872424000008/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "AMZN_10-K_FY2023_0001018724_24_000008.xlsx" "https://www.sec.gov/Archives/edgar/data/1018724/000101872424000008/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded AMZN_10-K_FY2023_0001018724_24_000008.xlsx
) else (
    echo ERROR: Curl failed for AMZN_10-K_FY2023_0001018724_24_000008.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #3: AMAZON COM INC
echo Downloading filing #3...
echo URL: https://www.sec.gov/Archives/edgar/data/1018724/000101872423000004/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "AMZN_10-K_FY2022_0001018724_23_000004.xlsx" "https://www.sec.gov/Archives/edgar/data/1018724/000101872423000004/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded AMZN_10-K_FY2022_0001018724_23_000004.xlsx
) else (
    echo ERROR: Curl failed for AMZN_10-K_FY2022_0001018724_23_000004.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.


echo.
echo Download complete! Check the SEC_Excel_Downloads folder.
pause
