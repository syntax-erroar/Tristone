@echo off
REM Advanced SEC Excel Downloader
REM Generated on 2025-10-07 10:26:11

echo Starting automated SEC Excel download for AMZN 8-K...
echo.

REM Create download directory
if not exist "SEC_Excel_Downloads_AMZN_8-K" mkdir "SEC_Excel_Downloads_AMZN_8-K"
cd "SEC_Excel_Downloads_AMZN_8-K"

echo Download directory created: SEC_Excel_Downloads_AMZN_8-K
echo.

REM Filing #1: AMAZON COM INC
echo Downloading filing #1...
echo URL: https://www.sec.gov/Archives/edgar/data/1018724/000101872424000158/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "AMZN_8-K_8K_2024_10_31_0001018724_24_000158.xlsx" "https://www.sec.gov/Archives/edgar/data/1018724/000101872424000158/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded AMZN_8-K_8K_2024_10_31_0001018724_24_000158.xlsx
) else (
    echo ERROR: Curl failed for AMZN_8-K_8K_2024_10_31_0001018724_24_000158.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #2: AMAZON COM INC
echo Downloading filing #2...
echo URL: https://www.sec.gov/Archives/edgar/data/1018724/000101872424000128/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "AMZN_8-K_8K_2024_08_01_0001018724_24_000128.xlsx" "https://www.sec.gov/Archives/edgar/data/1018724/000101872424000128/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded AMZN_8-K_8K_2024_08_01_0001018724_24_000128.xlsx
) else (
    echo ERROR: Curl failed for AMZN_8-K_8K_2024_08_01_0001018724_24_000128.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #3: AMAZON COM INC
echo Downloading filing #3...
echo URL: https://www.sec.gov/Archives/edgar/data/1018724/000110465924065117/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "AMZN_8-K_8K_2024_05_22_0001104659_24_065117.xlsx" "https://www.sec.gov/Archives/edgar/data/1018724/000110465924065117/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded AMZN_8-K_8K_2024_05_22_0001104659_24_065117.xlsx
) else (
    echo ERROR: Curl failed for AMZN_8-K_8K_2024_05_22_0001104659_24_065117.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #4: AMAZON COM INC
echo Downloading filing #4...
echo URL: https://www.sec.gov/Archives/edgar/data/1018724/000110465924061143/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "AMZN_8-K_8K_2024_05_14_0001104659_24_061143.xlsx" "https://www.sec.gov/Archives/edgar/data/1018724/000110465924061143/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded AMZN_8-K_8K_2024_05_14_0001104659_24_061143.xlsx
) else (
    echo ERROR: Curl failed for AMZN_8-K_8K_2024_05_14_0001104659_24_061143.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #5: AMAZON COM INC
echo Downloading filing #5...
echo URL: https://www.sec.gov/Archives/edgar/data/1018724/000110465924057026/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "AMZN_8-K_8K_2024_05_03_0001104659_24_057026.xlsx" "https://www.sec.gov/Archives/edgar/data/1018724/000110465924057026/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded AMZN_8-K_8K_2024_05_03_0001104659_24_057026.xlsx
) else (
    echo ERROR: Curl failed for AMZN_8-K_8K_2024_05_03_0001104659_24_057026.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #6: AMAZON COM INC
echo Downloading filing #6...
echo URL: https://www.sec.gov/Archives/edgar/data/1018724/000101872424000081/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "AMZN_8-K_8K_2024_04_30_0001018724_24_000081.xlsx" "https://www.sec.gov/Archives/edgar/data/1018724/000101872424000081/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded AMZN_8-K_8K_2024_04_30_0001018724_24_000081.xlsx
) else (
    echo ERROR: Curl failed for AMZN_8-K_8K_2024_04_30_0001018724_24_000081.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #7: AMAZON COM INC
echo Downloading filing #7...
echo URL: https://www.sec.gov/Archives/edgar/data/1018724/000110465924045915/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "AMZN_8-K_8K_2024_04_11_0001104659_24_045915.xlsx" "https://www.sec.gov/Archives/edgar/data/1018724/000110465924045915/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded AMZN_8-K_8K_2024_04_11_0001104659_24_045915.xlsx
) else (
    echo ERROR: Curl failed for AMZN_8-K_8K_2024_04_11_0001104659_24_045915.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #8: AMAZON COM INC
echo Downloading filing #8...
echo URL: https://www.sec.gov/Archives/edgar/data/1018724/000101872424000006/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "AMZN_8-K_8K_2024_02_01_0001018724_24_000006.xlsx" "https://www.sec.gov/Archives/edgar/data/1018724/000101872424000006/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded AMZN_8-K_8K_2024_02_01_0001018724_24_000006.xlsx
) else (
    echo ERROR: Curl failed for AMZN_8-K_8K_2024_02_01_0001018724_24_000006.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #9: AMAZON COM INC
echo Downloading filing #9...
echo URL: https://www.sec.gov/Archives/edgar/data/1018724/000110465923113444/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "AMZN_8-K_8K_2023_11_01_0001104659_23_113444.xlsx" "https://www.sec.gov/Archives/edgar/data/1018724/000110465923113444/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded AMZN_8-K_8K_2023_11_01_0001104659_23_113444.xlsx
) else (
    echo ERROR: Curl failed for AMZN_8-K_8K_2023_11_01_0001104659_23_113444.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #10: AMAZON COM INC
echo Downloading filing #10...
echo URL: https://www.sec.gov/Archives/edgar/data/1018724/000101872423000016/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "AMZN_8-K_8K_2023_10_26_0001018724_23_000016.xlsx" "https://www.sec.gov/Archives/edgar/data/1018724/000101872423000016/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded AMZN_8-K_8K_2023_10_26_0001018724_23_000016.xlsx
) else (
    echo ERROR: Curl failed for AMZN_8-K_8K_2023_10_26_0001018724_23_000016.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #11: AMAZON COM INC
echo Downloading filing #11...
echo URL: https://www.sec.gov/Archives/edgar/data/1018724/000101872423000014/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "AMZN_8-K_8K_2023_09_13_0001018724_23_000014.xlsx" "https://www.sec.gov/Archives/edgar/data/1018724/000101872423000014/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded AMZN_8-K_8K_2023_09_13_0001018724_23_000014.xlsx
) else (
    echo ERROR: Curl failed for AMZN_8-K_8K_2023_09_13_0001018724_23_000014.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #12: AMAZON COM INC
echo Downloading filing #12...
echo URL: https://www.sec.gov/Archives/edgar/data/1018724/000101872423000010/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "AMZN_8-K_8K_2023_08_03_0001018724_23_000010.xlsx" "https://www.sec.gov/Archives/edgar/data/1018724/000101872423000010/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded AMZN_8-K_8K_2023_08_03_0001018724_23_000010.xlsx
) else (
    echo ERROR: Curl failed for AMZN_8-K_8K_2023_08_03_0001018724_23_000010.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #13: AMAZON COM INC
echo Downloading filing #13...
echo URL: https://www.sec.gov/Archives/edgar/data/1018724/000110465923065457/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "AMZN_8-K_8K_2023_05_24_0001104659_23_065457.xlsx" "https://www.sec.gov/Archives/edgar/data/1018724/000110465923065457/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded AMZN_8-K_8K_2023_05_24_0001104659_23_065457.xlsx
) else (
    echo ERROR: Curl failed for AMZN_8-K_8K_2023_05_24_0001104659_23_065457.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #14: AMAZON COM INC
echo Downloading filing #14...
echo URL: https://www.sec.gov/Archives/edgar/data/1018724/000101872423000006/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "AMZN_8-K_8K_2023_04_27_0001018724_23_000006.xlsx" "https://www.sec.gov/Archives/edgar/data/1018724/000101872423000006/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded AMZN_8-K_8K_2023_04_27_0001018724_23_000006.xlsx
) else (
    echo ERROR: Curl failed for AMZN_8-K_8K_2023_04_27_0001018724_23_000006.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #15: AMAZON COM INC
echo Downloading filing #15...
echo URL: https://www.sec.gov/Archives/edgar/data/1018724/000110465923044715/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "AMZN_8-K_8K_2023_04_13_0001104659_23_044715.xlsx" "https://www.sec.gov/Archives/edgar/data/1018724/000110465923044715/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded AMZN_8-K_8K_2023_04_13_0001104659_23_044715.xlsx
) else (
    echo ERROR: Curl failed for AMZN_8-K_8K_2023_04_13_0001104659_23_044715.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #16: AMAZON COM INC
echo Downloading filing #16...
echo URL: https://www.sec.gov/Archives/edgar/data/1018724/000101872423000002/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "AMZN_8-K_8K_2023_02_02_0001018724_23_000002.xlsx" "https://www.sec.gov/Archives/edgar/data/1018724/000101872423000002/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded AMZN_8-K_8K_2023_02_02_0001018724_23_000002.xlsx
) else (
    echo ERROR: Curl failed for AMZN_8-K_8K_2023_02_02_0001018724_23_000002.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #17: AMAZON COM INC
echo Downloading filing #17...
echo URL: https://www.sec.gov/Archives/edgar/data/1018724/000119312523003621/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "AMZN_8-K_8K_2023_01_05_0001193125_23_003621.xlsx" "https://www.sec.gov/Archives/edgar/data/1018724/000119312523003621/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded AMZN_8-K_8K_2023_01_05_0001193125_23_003621.xlsx
) else (
    echo ERROR: Curl failed for AMZN_8-K_8K_2023_01_05_0001193125_23_003621.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #18: AMAZON COM INC
echo Downloading filing #18...
echo URL: https://www.sec.gov/Archives/edgar/data/1018724/000119312523000849/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "AMZN_8-K_8K_2023_01_03_0001193125_23_000849.xlsx" "https://www.sec.gov/Archives/edgar/data/1018724/000119312523000849/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded AMZN_8-K_8K_2023_01_03_0001193125_23_000849.xlsx
) else (
    echo ERROR: Curl failed for AMZN_8-K_8K_2023_01_03_0001193125_23_000849.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.


echo.
echo Download complete! Check the SEC_Excel_Downloads folder.
pause
