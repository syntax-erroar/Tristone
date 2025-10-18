@echo off
REM Advanced SEC Excel Downloader
REM Generated on 2025-10-17 13:43:44

echo Starting automated SEC Excel download for AMZN 10-Q...
echo.

REM Create download directory
if not exist "SEC_Excel_Downloads_AMZN_10-Q" mkdir "SEC_Excel_Downloads_AMZN_10-Q"
cd "SEC_Excel_Downloads_AMZN_10-Q"

echo Download directory created: SEC_Excel_Downloads_AMZN_10-Q
echo.

REM Filing #1: AMAZON COM INC
echo Downloading filing #1...
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

REM Filing #2: AMAZON COM INC
echo Downloading filing #2...
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

REM Filing #3: AMAZON COM INC
echo Downloading filing #3...
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

REM Filing #4: AMAZON COM INC
echo Downloading filing #4...
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

REM Filing #5: AMAZON COM INC
echo Downloading filing #5...
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

REM Filing #6: AMAZON COM INC
echo Downloading filing #6...
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

REM Filing #7: AMAZON COM INC
echo Downloading filing #7...
echo URL: https://www.sec.gov/Archives/edgar/data/1018724/000101872422000023/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "AMZN_10-Q_Q3_2022_Sep_0001018724_22_000023.xlsx" "https://www.sec.gov/Archives/edgar/data/1018724/000101872422000023/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded AMZN_10-Q_Q3_2022_Sep_0001018724_22_000023.xlsx
) else (
    echo ERROR: Curl failed for AMZN_10-Q_Q3_2022_Sep_0001018724_22_000023.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #8: AMAZON COM INC
echo Downloading filing #8...
echo URL: https://www.sec.gov/Archives/edgar/data/1018724/000101872422000019/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "AMZN_10-Q_Q2_2022_Jun_0001018724_22_000019.xlsx" "https://www.sec.gov/Archives/edgar/data/1018724/000101872422000019/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded AMZN_10-Q_Q2_2022_Jun_0001018724_22_000019.xlsx
) else (
    echo ERROR: Curl failed for AMZN_10-Q_Q2_2022_Jun_0001018724_22_000019.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #9: AMAZON COM INC
echo Downloading filing #9...
echo URL: https://www.sec.gov/Archives/edgar/data/1018724/000101872422000013/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "AMZN_10-Q_Q1_2022_Mar_0001018724_22_000013.xlsx" "https://www.sec.gov/Archives/edgar/data/1018724/000101872422000013/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded AMZN_10-Q_Q1_2022_Mar_0001018724_22_000013.xlsx
) else (
    echo ERROR: Curl failed for AMZN_10-Q_Q1_2022_Mar_0001018724_22_000013.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #10: AMAZON COM INC
echo Downloading filing #10...
echo URL: https://www.sec.gov/Archives/edgar/data/1018724/000101872421000028/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "AMZN_10-Q_Q3_2021_Sep_0001018724_21_000028.xlsx" "https://www.sec.gov/Archives/edgar/data/1018724/000101872421000028/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded AMZN_10-Q_Q3_2021_Sep_0001018724_21_000028.xlsx
) else (
    echo ERROR: Curl failed for AMZN_10-Q_Q3_2021_Sep_0001018724_21_000028.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #11: AMAZON COM INC
echo Downloading filing #11...
echo URL: https://www.sec.gov/Archives/edgar/data/1018724/000101872421000020/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "AMZN_10-Q_Q2_2021_Jun_0001018724_21_000020.xlsx" "https://www.sec.gov/Archives/edgar/data/1018724/000101872421000020/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded AMZN_10-Q_Q2_2021_Jun_0001018724_21_000020.xlsx
) else (
    echo ERROR: Curl failed for AMZN_10-Q_Q2_2021_Jun_0001018724_21_000020.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #12: AMAZON COM INC
echo Downloading filing #12...
echo URL: https://www.sec.gov/Archives/edgar/data/1018724/000101872421000010/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "AMZN_10-Q_Q1_2021_Mar_0001018724_21_000010.xlsx" "https://www.sec.gov/Archives/edgar/data/1018724/000101872421000010/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded AMZN_10-Q_Q1_2021_Mar_0001018724_21_000010.xlsx
) else (
    echo ERROR: Curl failed for AMZN_10-Q_Q1_2021_Mar_0001018724_21_000010.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #13: AMAZON COM INC
echo Downloading filing #13...
echo URL: https://www.sec.gov/Archives/edgar/data/1018724/000101872420000030/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "AMZN_10-Q_Q3_2020_Sep_0001018724_20_000030.xlsx" "https://www.sec.gov/Archives/edgar/data/1018724/000101872420000030/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded AMZN_10-Q_Q3_2020_Sep_0001018724_20_000030.xlsx
) else (
    echo ERROR: Curl failed for AMZN_10-Q_Q3_2020_Sep_0001018724_20_000030.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #14: AMAZON COM INC
echo Downloading filing #14...
echo URL: https://www.sec.gov/Archives/edgar/data/1018724/000101872420000021/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "AMZN_10-Q_Q2_2020_Jun_0001018724_20_000021.xlsx" "https://www.sec.gov/Archives/edgar/data/1018724/000101872420000021/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded AMZN_10-Q_Q2_2020_Jun_0001018724_20_000021.xlsx
) else (
    echo ERROR: Curl failed for AMZN_10-Q_Q2_2020_Jun_0001018724_20_000021.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #15: AMAZON COM INC
echo Downloading filing #15...
echo URL: https://www.sec.gov/Archives/edgar/data/1018724/000101872420000010/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "AMZN_10-Q_Q1_2020_Mar_0001018724_20_000010.xlsx" "https://www.sec.gov/Archives/edgar/data/1018724/000101872420000010/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded AMZN_10-Q_Q1_2020_Mar_0001018724_20_000010.xlsx
) else (
    echo ERROR: Curl failed for AMZN_10-Q_Q1_2020_Mar_0001018724_20_000010.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.


echo.
echo Download complete! Check the SEC_Excel_Downloads folder.
pause
