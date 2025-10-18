@echo off
REM Advanced SEC Excel Downloader
REM Generated on 2025-10-10 14:42:51

echo Starting automated SEC Excel download for EAF 10-K...
echo.

REM Create download directory
if not exist "SEC_Excel_Downloads_EAF_10-K" mkdir "SEC_Excel_Downloads_EAF_10-K"
cd "SEC_Excel_Downloads_EAF_10-K"

echo Download directory created: SEC_Excel_Downloads_EAF_10-K
echo.

REM Filing #1: GRAFTECH INTERNATIONAL LTD
echo Downloading filing #1...
echo URL: https://www.sec.gov/Archives/edgar/data/931148/000093114825000028/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "EAF_10-K_FY2024_0000931148_25_000028.xlsx" "https://www.sec.gov/Archives/edgar/data/931148/000093114825000028/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded EAF_10-K_FY2024_0000931148_25_000028.xlsx
) else (
    echo ERROR: Curl failed for EAF_10-K_FY2024_0000931148_25_000028.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #2: GRAFTECH INTERNATIONAL LTD
echo Downloading filing #2...
echo URL: https://www.sec.gov/Archives/edgar/data/931148/000093114824000021/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "EAF_10-K_FY2023_0000931148_24_000021.xlsx" "https://www.sec.gov/Archives/edgar/data/931148/000093114824000021/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded EAF_10-K_FY2023_0000931148_24_000021.xlsx
) else (
    echo ERROR: Curl failed for EAF_10-K_FY2023_0000931148_24_000021.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #3: GRAFTECH INTERNATIONAL LTD
echo Downloading filing #3...
echo URL: https://www.sec.gov/Archives/edgar/data/931148/000093114823000035/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "EAF_10-K_FY2022_0000931148_23_000035.xlsx" "https://www.sec.gov/Archives/edgar/data/931148/000093114823000035/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded EAF_10-K_FY2022_0000931148_23_000035.xlsx
) else (
    echo ERROR: Curl failed for EAF_10-K_FY2022_0000931148_23_000035.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #4: GRAFTECH INTERNATIONAL LTD
echo Downloading filing #4...
echo URL: https://www.sec.gov/Archives/edgar/data/931148/000093114822000027/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "EAF_10-K_FY2021_0000931148_22_000027.xlsx" "https://www.sec.gov/Archives/edgar/data/931148/000093114822000027/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded EAF_10-K_FY2021_0000931148_22_000027.xlsx
) else (
    echo ERROR: Curl failed for EAF_10-K_FY2021_0000931148_22_000027.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #5: GRAFTECH INTERNATIONAL LTD
echo Downloading filing #5...
echo URL: https://www.sec.gov/Archives/edgar/data/931148/000093114821000035/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "EAF_10-K_FY2020_0000931148_21_000035.xlsx" "https://www.sec.gov/Archives/edgar/data/931148/000093114821000035/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded EAF_10-K_FY2020_0000931148_21_000035.xlsx
) else (
    echo ERROR: Curl failed for EAF_10-K_FY2020_0000931148_21_000035.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.


echo.
echo Download complete! Check the SEC_Excel_Downloads folder.
pause
