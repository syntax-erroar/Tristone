@echo off
REM Advanced SEC Excel Downloader
REM Generated on 2025-10-18 13:56:37

echo Starting automated SEC Excel download for RUN 10-K...
echo.

REM Create download directory
if not exist "SEC_Excel_Downloads_RUN_10-K" mkdir "SEC_Excel_Downloads_RUN_10-K"
cd "SEC_Excel_Downloads_RUN_10-K"

echo Download directory created: SEC_Excel_Downloads_RUN_10-K
echo.

REM Filing #1: Sunrun Inc.
echo Downloading filing #1...
echo URL: https://www.sec.gov/Archives/edgar/data/1469367/000146936725000039/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "RUN_10-K_FY2024_0001469367_25_000039.xlsx" "https://www.sec.gov/Archives/edgar/data/1469367/000146936725000039/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded RUN_10-K_FY2024_0001469367_25_000039.xlsx
) else (
    echo ERROR: Curl failed for RUN_10-K_FY2024_0001469367_25_000039.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #2: Sunrun Inc.
echo Downloading filing #2...
echo URL: https://www.sec.gov/Archives/edgar/data/1469367/000146936724000024/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "RUN_10-K_FY2023_0001469367_24_000024.xlsx" "https://www.sec.gov/Archives/edgar/data/1469367/000146936724000024/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded RUN_10-K_FY2023_0001469367_24_000024.xlsx
) else (
    echo ERROR: Curl failed for RUN_10-K_FY2023_0001469367_24_000024.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #3: Sunrun Inc.
echo Downloading filing #3...
echo URL: https://www.sec.gov/Archives/edgar/data/1469367/000146936723000030/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "RUN_10-K_FY2022_0001469367_23_000030.xlsx" "https://www.sec.gov/Archives/edgar/data/1469367/000146936723000030/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded RUN_10-K_FY2022_0001469367_23_000030.xlsx
) else (
    echo ERROR: Curl failed for RUN_10-K_FY2022_0001469367_23_000030.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #4: Sunrun Inc.
echo Downloading filing #4...
echo URL: https://www.sec.gov/Archives/edgar/data/1469367/000146936722000033/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "RUN_10-K_FY2021_0001469367_22_000033.xlsx" "https://www.sec.gov/Archives/edgar/data/1469367/000146936722000033/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded RUN_10-K_FY2021_0001469367_22_000033.xlsx
) else (
    echo ERROR: Curl failed for RUN_10-K_FY2021_0001469367_22_000033.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #5: Sunrun Inc.
echo Downloading filing #5...
echo URL: https://www.sec.gov/Archives/edgar/data/1469367/000146936721000042/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "RUN_10-K_FY2020_0001469367_21_000042.xlsx" "https://www.sec.gov/Archives/edgar/data/1469367/000146936721000042/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded RUN_10-K_FY2020_0001469367_21_000042.xlsx
) else (
    echo ERROR: Curl failed for RUN_10-K_FY2020_0001469367_21_000042.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #6: Sunrun Inc.
echo Downloading filing #6...
echo URL: https://www.sec.gov/Archives/edgar/data/1469367/000146936720000061/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "RUN_10-K_FY2019_0001469367_20_000061.xlsx" "https://www.sec.gov/Archives/edgar/data/1469367/000146936720000061/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded RUN_10-K_FY2019_0001469367_20_000061.xlsx
) else (
    echo ERROR: Curl failed for RUN_10-K_FY2019_0001469367_20_000061.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #7: Sunrun Inc.
echo Downloading filing #7...
echo URL: https://www.sec.gov/Archives/edgar/data/1469367/000146936719000047/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "RUN_10-K_FY2018_0001469367_19_000047.xlsx" "https://www.sec.gov/Archives/edgar/data/1469367/000146936719000047/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded RUN_10-K_FY2018_0001469367_19_000047.xlsx
) else (
    echo ERROR: Curl failed for RUN_10-K_FY2018_0001469367_19_000047.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #8: Sunrun Inc.
echo Downloading filing #8...
echo URL: https://www.sec.gov/Archives/edgar/data/1469367/000146936719000041/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "RUN_10-K_FY2018_0001469367_19_000041.xlsx" "https://www.sec.gov/Archives/edgar/data/1469367/000146936719000041/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded RUN_10-K_FY2018_0001469367_19_000041.xlsx
) else (
    echo ERROR: Curl failed for RUN_10-K_FY2018_0001469367_19_000041.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #9: Sunrun Inc.
echo Downloading filing #9...
echo URL: https://www.sec.gov/Archives/edgar/data/1469367/000146936718000031/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "RUN_10-K_FY2017_0001469367_18_000031.xlsx" "https://www.sec.gov/Archives/edgar/data/1469367/000146936718000031/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded RUN_10-K_FY2017_0001469367_18_000031.xlsx
) else (
    echo ERROR: Curl failed for RUN_10-K_FY2017_0001469367_18_000031.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.


echo.
echo Download complete! Check the SEC_Excel_Downloads folder.
pause
