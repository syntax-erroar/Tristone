@echo off
REM Advanced SEC Excel Downloader
REM Generated on 2025-10-07 10:41:27

echo Starting automated SEC Excel download for AMZN 10-Q...
echo.

REM Create download directory
if not exist "SEC_Excel_Downloads_AMZN_10-Q" mkdir "SEC_Excel_Downloads_AMZN_10-Q"
cd "SEC_Excel_Downloads_AMZN_10-Q"

echo Download directory created: SEC_Excel_Downloads_AMZN_10-Q
echo.

REM Filing #1: AMAZON COM INC
echo Downloading filing #1...
echo URL: https://www.sec.gov/Archives/edgar/data/1018724/000101872425000086/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "AMZN_10-Q_Q2_2025_Jun_0001018724_25_000086.xlsx" "https://www.sec.gov/Archives/edgar/data/1018724/000101872425000086/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded AMZN_10-Q_Q2_2025_Jun_0001018724_25_000086.xlsx
) else (
    echo ERROR: Curl failed for AMZN_10-Q_Q2_2025_Jun_0001018724_25_000086.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #2: AMAZON COM INC
echo Downloading filing #2...
echo URL: https://www.sec.gov/Archives/edgar/data/1018724/000101872425000036/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "AMZN_10-Q_Q1_2025_Mar_0001018724_25_000036.xlsx" "https://www.sec.gov/Archives/edgar/data/1018724/000101872425000036/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded AMZN_10-Q_Q1_2025_Mar_0001018724_25_000036.xlsx
) else (
    echo ERROR: Curl failed for AMZN_10-Q_Q1_2025_Mar_0001018724_25_000036.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #3: AMAZON COM INC
echo Downloading filing #3...
echo URL: https://www.sec.gov/Archives/edgar/data/1018724/000101872424000161/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "AMZN_10-Q_Q3_2024_Sep_0001018724_24_000161.xlsx" "https://www.sec.gov/Archives/edgar/data/1018724/000101872424000161/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded AMZN_10-Q_Q3_2024_Sep_0001018724_24_000161.xlsx
) else (
    echo ERROR: Curl failed for AMZN_10-Q_Q3_2024_Sep_0001018724_24_000161.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #4: AMAZON COM INC
echo Downloading filing #4...
echo URL: https://www.sec.gov/Archives/edgar/data/1018724/000101872424000130/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "AMZN_10-Q_Q2_2024_Jun_0001018724_24_000130.xlsx" "https://www.sec.gov/Archives/edgar/data/1018724/000101872424000130/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded AMZN_10-Q_Q2_2024_Jun_0001018724_24_000130.xlsx
) else (
    echo ERROR: Curl failed for AMZN_10-Q_Q2_2024_Jun_0001018724_24_000130.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #5: AMAZON COM INC
echo Downloading filing #5...
echo URL: https://www.sec.gov/Archives/edgar/data/1018724/000101872424000083/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "AMZN_10-Q_Q1_2024_Mar_0001018724_24_000083.xlsx" "https://www.sec.gov/Archives/edgar/data/1018724/000101872424000083/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded AMZN_10-Q_Q1_2024_Mar_0001018724_24_000083.xlsx
) else (
    echo ERROR: Curl failed for AMZN_10-Q_Q1_2024_Mar_0001018724_24_000083.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #6: AMAZON COM INC
echo Downloading filing #6...
echo URL: https://www.sec.gov/Archives/edgar/data/1018724/000101872423000018/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "AMZN_10-Q_Q3_2023_Sep_0001018724_23_000018.xlsx" "https://www.sec.gov/Archives/edgar/data/1018724/000101872423000018/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded AMZN_10-Q_Q3_2023_Sep_0001018724_23_000018.xlsx
) else (
    echo ERROR: Curl failed for AMZN_10-Q_Q3_2023_Sep_0001018724_23_000018.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #7: AMAZON COM INC
echo Downloading filing #7...
echo URL: https://www.sec.gov/Archives/edgar/data/1018724/000101872423000012/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "AMZN_10-Q_Q2_2023_Jun_0001018724_23_000012.xlsx" "https://www.sec.gov/Archives/edgar/data/1018724/000101872423000012/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded AMZN_10-Q_Q2_2023_Jun_0001018724_23_000012.xlsx
) else (
    echo ERROR: Curl failed for AMZN_10-Q_Q2_2023_Jun_0001018724_23_000012.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #8: AMAZON COM INC
echo Downloading filing #8...
echo URL: https://www.sec.gov/Archives/edgar/data/1018724/000101872423000008/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "AMZN_10-Q_Q1_2023_Mar_0001018724_23_000008.xlsx" "https://www.sec.gov/Archives/edgar/data/1018724/000101872423000008/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded AMZN_10-Q_Q1_2023_Mar_0001018724_23_000008.xlsx
) else (
    echo ERROR: Curl failed for AMZN_10-Q_Q1_2023_Mar_0001018724_23_000008.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.


echo.
echo Download complete! Check the SEC_Excel_Downloads folder.
pause
