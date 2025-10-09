@echo off
REM Advanced SEC Excel Downloader
REM Generated on 2025-10-07 17:01:06

echo Starting automated SEC Excel download for TSLA 10-K...
echo.

REM Create download directory
if not exist "SEC_Excel_Downloads_TSLA_10-K" mkdir "SEC_Excel_Downloads_TSLA_10-K"
cd "SEC_Excel_Downloads_TSLA_10-K"

echo Download directory created: SEC_Excel_Downloads_TSLA_10-K
echo.

REM Filing #1: Tesla, Inc.
echo Downloading filing #1...
echo URL: https://www.sec.gov/Archives/edgar/data/1318605/000110465925042659/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "TSLA_10-K_FY2024_0001104659_25_042659.xlsx" "https://www.sec.gov/Archives/edgar/data/1318605/000110465925042659/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded TSLA_10-K_FY2024_0001104659_25_042659.xlsx
) else (
    echo ERROR: Curl failed for TSLA_10-K_FY2024_0001104659_25_042659.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #2: Tesla, Inc.
echo Downloading filing #2...
echo URL: https://www.sec.gov/Archives/edgar/data/1318605/000162828025003063/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "TSLA_10-K_FY2024_0001628280_25_003063.xlsx" "https://www.sec.gov/Archives/edgar/data/1318605/000162828025003063/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded TSLA_10-K_FY2024_0001628280_25_003063.xlsx
) else (
    echo ERROR: Curl failed for TSLA_10-K_FY2024_0001628280_25_003063.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #3: Tesla, Inc.
echo Downloading filing #3...
echo URL: https://www.sec.gov/Archives/edgar/data/1318605/000162828024002390/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "TSLA_10-K_FY2023_0001628280_24_002390.xlsx" "https://www.sec.gov/Archives/edgar/data/1318605/000162828024002390/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded TSLA_10-K_FY2023_0001628280_24_002390.xlsx
) else (
    echo ERROR: Curl failed for TSLA_10-K_FY2023_0001628280_24_002390.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #4: Tesla, Inc.
echo Downloading filing #4...
echo URL: https://www.sec.gov/Archives/edgar/data/1318605/000095017023001409/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "TSLA_10-K_FY2022_0000950170_23_001409.xlsx" "https://www.sec.gov/Archives/edgar/data/1318605/000095017023001409/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded TSLA_10-K_FY2022_0000950170_23_001409.xlsx
) else (
    echo ERROR: Curl failed for TSLA_10-K_FY2022_0000950170_23_001409.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.


echo.
echo Download complete! Check the SEC_Excel_Downloads folder.
pause
