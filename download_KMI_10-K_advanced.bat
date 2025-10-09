@echo off
REM Advanced SEC Excel Downloader
REM Generated on 2025-10-07 17:52:23

echo Starting automated SEC Excel download for KMI 10-K...
echo.

REM Create download directory
if not exist "SEC_Excel_Downloads_KMI_10-K" mkdir "SEC_Excel_Downloads_KMI_10-K"
cd "SEC_Excel_Downloads_KMI_10-K"

echo Download directory created: SEC_Excel_Downloads_KMI_10-K
echo.

REM Filing #1: KINDER MORGAN, INC.
echo Downloading filing #1...
echo URL: https://www.sec.gov/Archives/edgar/data/1506307/000150630725000008/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "KMI_10-K_FY2024_0001506307_25_000008.xlsx" "https://www.sec.gov/Archives/edgar/data/1506307/000150630725000008/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded KMI_10-K_FY2024_0001506307_25_000008.xlsx
) else (
    echo ERROR: Curl failed for KMI_10-K_FY2024_0001506307_25_000008.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #2: KINDER MORGAN, INC.
echo Downloading filing #2...
echo URL: https://www.sec.gov/Archives/edgar/data/1506307/000150630724000011/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "KMI_10-K_FY2023_0001506307_24_000011.xlsx" "https://www.sec.gov/Archives/edgar/data/1506307/000150630724000011/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded KMI_10-K_FY2023_0001506307_24_000011.xlsx
) else (
    echo ERROR: Curl failed for KMI_10-K_FY2023_0001506307_24_000011.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #3: KINDER MORGAN, INC.
echo Downloading filing #3...
echo URL: https://www.sec.gov/Archives/edgar/data/1506307/000150630723000023/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "KMI_10-K_FY2022_0001506307_23_000023.xlsx" "https://www.sec.gov/Archives/edgar/data/1506307/000150630723000023/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded KMI_10-K_FY2022_0001506307_23_000023.xlsx
) else (
    echo ERROR: Curl failed for KMI_10-K_FY2022_0001506307_23_000023.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #4: KINDER MORGAN, INC.
echo Downloading filing #4...
echo URL: https://www.sec.gov/Archives/edgar/data/1506307/000150630722000018/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "KMI_10-K_FY2021_0001506307_22_000018.xlsx" "https://www.sec.gov/Archives/edgar/data/1506307/000150630722000018/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded KMI_10-K_FY2021_0001506307_22_000018.xlsx
) else (
    echo ERROR: Curl failed for KMI_10-K_FY2021_0001506307_22_000018.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #5: KINDER MORGAN, INC.
echo Downloading filing #5...
echo URL: https://www.sec.gov/Archives/edgar/data/1506307/000150630721000022/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "KMI_10-K_FY2020_0001506307_21_000022.xlsx" "https://www.sec.gov/Archives/edgar/data/1506307/000150630721000022/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded KMI_10-K_FY2020_0001506307_21_000022.xlsx
) else (
    echo ERROR: Curl failed for KMI_10-K_FY2020_0001506307_21_000022.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #6: KINDER MORGAN, INC.
echo Downloading filing #6...
echo URL: https://www.sec.gov/Archives/edgar/data/1506307/000150630720000022/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "KMI_10-K_FY2019_0001506307_20_000022.xlsx" "https://www.sec.gov/Archives/edgar/data/1506307/000150630720000022/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded KMI_10-K_FY2019_0001506307_20_000022.xlsx
) else (
    echo ERROR: Curl failed for KMI_10-K_FY2019_0001506307_20_000022.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.


echo.
echo Download complete! Check the SEC_Excel_Downloads folder.
pause
