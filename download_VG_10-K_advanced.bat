@echo off
REM Advanced SEC Excel Downloader
REM Generated on 2025-10-10 15:47:44

echo Starting automated SEC Excel download for VG 10-K...
echo.

REM Create download directory
if not exist "SEC_Excel_Downloads_VG_10-K" mkdir "SEC_Excel_Downloads_VG_10-K"
cd "SEC_Excel_Downloads_VG_10-K"

echo Download directory created: SEC_Excel_Downloads_VG_10-K
echo.

REM Filing #1: VONAGE HOLDINGS CORP
echo Downloading filing #1...
echo URL: https://www.sec.gov/Archives/edgar/data/1272830/000127283022000074/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "VG_10-K_FY2021_0001272830_22_000074.xlsx" "https://www.sec.gov/Archives/edgar/data/1272830/000127283022000074/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded VG_10-K_FY2021_0001272830_22_000074.xlsx
) else (
    echo ERROR: Curl failed for VG_10-K_FY2021_0001272830_22_000074.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #2: VONAGE HOLDINGS CORP
echo Downloading filing #2...
echo URL: https://www.sec.gov/Archives/edgar/data/1272830/000127283022000040/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "VG_10-K_FY2021_0001272830_22_000040.xlsx" "https://www.sec.gov/Archives/edgar/data/1272830/000127283022000040/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded VG_10-K_FY2021_0001272830_22_000040.xlsx
) else (
    echo ERROR: Curl failed for VG_10-K_FY2021_0001272830_22_000040.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #3: VONAGE HOLDINGS CORP
echo Downloading filing #3...
echo URL: https://www.sec.gov/Archives/edgar/data/1272830/000127283021000087/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "VG_10-K_FY2020_0001272830_21_000087.xlsx" "https://www.sec.gov/Archives/edgar/data/1272830/000127283021000087/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded VG_10-K_FY2020_0001272830_21_000087.xlsx
) else (
    echo ERROR: Curl failed for VG_10-K_FY2020_0001272830_21_000087.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #4: VONAGE HOLDINGS CORP
echo Downloading filing #4...
echo URL: https://www.sec.gov/Archives/edgar/data/1272830/000127283020000049/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "VG_10-K_FY2019_0001272830_20_000049.xlsx" "https://www.sec.gov/Archives/edgar/data/1272830/000127283020000049/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded VG_10-K_FY2019_0001272830_20_000049.xlsx
) else (
    echo ERROR: Curl failed for VG_10-K_FY2019_0001272830_20_000049.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.


echo.
echo Download complete! Check the SEC_Excel_Downloads folder.
pause
