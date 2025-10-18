@echo off
REM Advanced SEC Excel Downloader
REM Generated on 2025-10-10 15:58:25

echo Starting automated SEC Excel download for VENTURE GLOBAL LNG 10-K...
echo.

REM Create download directory
if not exist "SEC_Excel_Downloads_VENTURE GLOBAL LNG_10-K" mkdir "SEC_Excel_Downloads_VENTURE GLOBAL LNG_10-K"
cd "SEC_Excel_Downloads_VENTURE GLOBAL LNG_10-K"

echo Download directory created: SEC_Excel_Downloads_VENTURE GLOBAL LNG_10-K
echo.

REM Filing #1: Cheniere Energy, Inc.
echo Downloading filing #1...
echo URL: https://www.sec.gov/Archives/edgar/data/3570/000000357024000040/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "VENTURE GLOBAL LNG_10-K_FY2023_0000003570_24_000040.xlsx" "https://www.sec.gov/Archives/edgar/data/3570/000000357024000040/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded VENTURE GLOBAL LNG_10-K_FY2023_0000003570_24_000040.xlsx
) else (
    echo ERROR: Curl failed for VENTURE GLOBAL LNG_10-K_FY2023_0000003570_24_000040.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #2: Cheniere Energy, Inc.
echo Downloading filing #2...
echo URL: https://www.sec.gov/Archives/edgar/data/3570/000000357023000042/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "VENTURE GLOBAL LNG_10-K_FY2022_0000003570_23_000042.xlsx" "https://www.sec.gov/Archives/edgar/data/3570/000000357023000042/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded VENTURE GLOBAL LNG_10-K_FY2022_0000003570_23_000042.xlsx
) else (
    echo ERROR: Curl failed for VENTURE GLOBAL LNG_10-K_FY2022_0000003570_23_000042.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #3: Cheniere Energy, Inc.
echo Downloading filing #3...
echo URL: https://www.sec.gov/Archives/edgar/data/3570/000000357022000024/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "VENTURE GLOBAL LNG_10-K_FY2021_0000003570_22_000024.xlsx" "https://www.sec.gov/Archives/edgar/data/3570/000000357022000024/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded VENTURE GLOBAL LNG_10-K_FY2021_0000003570_22_000024.xlsx
) else (
    echo ERROR: Curl failed for VENTURE GLOBAL LNG_10-K_FY2021_0000003570_22_000024.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #4: Cheniere Energy, Inc.
echo Downloading filing #4...
echo URL: https://www.sec.gov/Archives/edgar/data/3570/000000357021000039/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "VENTURE GLOBAL LNG_10-K_FY2020_0000003570_21_000039.xlsx" "https://www.sec.gov/Archives/edgar/data/3570/000000357021000039/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded VENTURE GLOBAL LNG_10-K_FY2020_0000003570_21_000039.xlsx
) else (
    echo ERROR: Curl failed for VENTURE GLOBAL LNG_10-K_FY2020_0000003570_21_000039.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #5: Cheniere Energy, Inc.
echo Downloading filing #5...
echo URL: https://www.sec.gov/Archives/edgar/data/3570/000000357020000043/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "VENTURE GLOBAL LNG_10-K_FY2019_0000003570_20_000043.xlsx" "https://www.sec.gov/Archives/edgar/data/3570/000000357020000043/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded VENTURE GLOBAL LNG_10-K_FY2019_0000003570_20_000043.xlsx
) else (
    echo ERROR: Curl failed for VENTURE GLOBAL LNG_10-K_FY2019_0000003570_20_000043.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.


echo.
echo Download complete! Check the SEC_Excel_Downloads folder.
pause
