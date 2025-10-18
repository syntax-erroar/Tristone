@echo off
REM Advanced SEC Excel Downloader
REM Generated on 2025-10-10 14:45:02

echo Starting automated SEC Excel download for EAF 10-Q...
echo.

REM Create download directory
if not exist "SEC_Excel_Downloads_EAF_10-Q" mkdir "SEC_Excel_Downloads_EAF_10-Q"
cd "SEC_Excel_Downloads_EAF_10-Q"

echo Download directory created: SEC_Excel_Downloads_EAF_10-Q
echo.

REM Filing #1: GRAFTECH INTERNATIONAL LTD
echo Downloading filing #1...
echo URL: https://www.sec.gov/Archives/edgar/data/931148/000093114825000117/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "EAF_10-Q_Q2_2025_Jun_0000931148_25_000117.xlsx" "https://www.sec.gov/Archives/edgar/data/931148/000093114825000117/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded EAF_10-Q_Q2_2025_Jun_0000931148_25_000117.xlsx
) else (
    echo ERROR: Curl failed for EAF_10-Q_Q2_2025_Jun_0000931148_25_000117.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #2: GRAFTECH INTERNATIONAL LTD
echo Downloading filing #2...
echo URL: https://www.sec.gov/Archives/edgar/data/931148/000093114825000073/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "EAF_10-Q_Q1_2025_Mar_0000931148_25_000073.xlsx" "https://www.sec.gov/Archives/edgar/data/931148/000093114825000073/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded EAF_10-Q_Q1_2025_Mar_0000931148_25_000073.xlsx
) else (
    echo ERROR: Curl failed for EAF_10-Q_Q1_2025_Mar_0000931148_25_000073.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #3: GRAFTECH INTERNATIONAL LTD
echo Downloading filing #3...
echo URL: https://www.sec.gov/Archives/edgar/data/931148/000093114824000121/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "EAF_10-Q_Q3_2024_Sep_0000931148_24_000121.xlsx" "https://www.sec.gov/Archives/edgar/data/931148/000093114824000121/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded EAF_10-Q_Q3_2024_Sep_0000931148_24_000121.xlsx
) else (
    echo ERROR: Curl failed for EAF_10-Q_Q3_2024_Sep_0000931148_24_000121.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #4: GRAFTECH INTERNATIONAL LTD
echo Downloading filing #4...
echo URL: https://www.sec.gov/Archives/edgar/data/931148/000093114824000101/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "EAF_10-Q_Q2_2024_Jun_0000931148_24_000101.xlsx" "https://www.sec.gov/Archives/edgar/data/931148/000093114824000101/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded EAF_10-Q_Q2_2024_Jun_0000931148_24_000101.xlsx
) else (
    echo ERROR: Curl failed for EAF_10-Q_Q2_2024_Jun_0000931148_24_000101.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #5: GRAFTECH INTERNATIONAL LTD
echo Downloading filing #5...
echo URL: https://www.sec.gov/Archives/edgar/data/931148/000093114824000065/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "EAF_10-Q_Q1_2024_Mar_0000931148_24_000065.xlsx" "https://www.sec.gov/Archives/edgar/data/931148/000093114824000065/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded EAF_10-Q_Q1_2024_Mar_0000931148_24_000065.xlsx
) else (
    echo ERROR: Curl failed for EAF_10-Q_Q1_2024_Mar_0000931148_24_000065.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #6: GRAFTECH INTERNATIONAL LTD
echo Downloading filing #6...
echo URL: https://www.sec.gov/Archives/edgar/data/931148/000093114823000158/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "EAF_10-Q_Q3_2023_Sep_0000931148_23_000158.xlsx" "https://www.sec.gov/Archives/edgar/data/931148/000093114823000158/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded EAF_10-Q_Q3_2023_Sep_0000931148_23_000158.xlsx
) else (
    echo ERROR: Curl failed for EAF_10-Q_Q3_2023_Sep_0000931148_23_000158.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #7: GRAFTECH INTERNATIONAL LTD
echo Downloading filing #7...
echo URL: https://www.sec.gov/Archives/edgar/data/931148/000093114823000139/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "EAF_10-Q_Q2_2023_Jun_0000931148_23_000139.xlsx" "https://www.sec.gov/Archives/edgar/data/931148/000093114823000139/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded EAF_10-Q_Q2_2023_Jun_0000931148_23_000139.xlsx
) else (
    echo ERROR: Curl failed for EAF_10-Q_Q2_2023_Jun_0000931148_23_000139.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #8: GRAFTECH INTERNATIONAL LTD
echo Downloading filing #8...
echo URL: https://www.sec.gov/Archives/edgar/data/931148/000093114823000076/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "EAF_10-Q_Q1_2023_Mar_0000931148_23_000076.xlsx" "https://www.sec.gov/Archives/edgar/data/931148/000093114823000076/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded EAF_10-Q_Q1_2023_Mar_0000931148_23_000076.xlsx
) else (
    echo ERROR: Curl failed for EAF_10-Q_Q1_2023_Mar_0000931148_23_000076.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #9: GRAFTECH INTERNATIONAL LTD
echo Downloading filing #9...
echo URL: https://www.sec.gov/Archives/edgar/data/931148/000093114822000143/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "EAF_10-Q_Q3_2022_Sep_0000931148_22_000143.xlsx" "https://www.sec.gov/Archives/edgar/data/931148/000093114822000143/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded EAF_10-Q_Q3_2022_Sep_0000931148_22_000143.xlsx
) else (
    echo ERROR: Curl failed for EAF_10-Q_Q3_2022_Sep_0000931148_22_000143.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #10: GRAFTECH INTERNATIONAL LTD
echo Downloading filing #10...
echo URL: https://www.sec.gov/Archives/edgar/data/931148/000093114822000111/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "EAF_10-Q_Q2_2022_Jun_0000931148_22_000111.xlsx" "https://www.sec.gov/Archives/edgar/data/931148/000093114822000111/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded EAF_10-Q_Q2_2022_Jun_0000931148_22_000111.xlsx
) else (
    echo ERROR: Curl failed for EAF_10-Q_Q2_2022_Jun_0000931148_22_000111.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #11: GRAFTECH INTERNATIONAL LTD
echo Downloading filing #11...
echo URL: https://www.sec.gov/Archives/edgar/data/931148/000093114822000070/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "EAF_10-Q_Q1_2022_Mar_0000931148_22_000070.xlsx" "https://www.sec.gov/Archives/edgar/data/931148/000093114822000070/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded EAF_10-Q_Q1_2022_Mar_0000931148_22_000070.xlsx
) else (
    echo ERROR: Curl failed for EAF_10-Q_Q1_2022_Mar_0000931148_22_000070.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #12: GRAFTECH INTERNATIONAL LTD
echo Downloading filing #12...
echo URL: https://www.sec.gov/Archives/edgar/data/931148/000093114821000161/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "EAF_10-Q_Q3_2021_Sep_0000931148_21_000161.xlsx" "https://www.sec.gov/Archives/edgar/data/931148/000093114821000161/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded EAF_10-Q_Q3_2021_Sep_0000931148_21_000161.xlsx
) else (
    echo ERROR: Curl failed for EAF_10-Q_Q3_2021_Sep_0000931148_21_000161.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #13: GRAFTECH INTERNATIONAL LTD
echo Downloading filing #13...
echo URL: https://www.sec.gov/Archives/edgar/data/931148/000093114821000131/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "EAF_10-Q_Q2_2021_Jun_0000931148_21_000131.xlsx" "https://www.sec.gov/Archives/edgar/data/931148/000093114821000131/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded EAF_10-Q_Q2_2021_Jun_0000931148_21_000131.xlsx
) else (
    echo ERROR: Curl failed for EAF_10-Q_Q2_2021_Jun_0000931148_21_000131.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #14: GRAFTECH INTERNATIONAL LTD
echo Downloading filing #14...
echo URL: https://www.sec.gov/Archives/edgar/data/931148/000093114821000091/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "EAF_10-Q_Q1_2021_Mar_0000931148_21_000091.xlsx" "https://www.sec.gov/Archives/edgar/data/931148/000093114821000091/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded EAF_10-Q_Q1_2021_Mar_0000931148_21_000091.xlsx
) else (
    echo ERROR: Curl failed for EAF_10-Q_Q1_2021_Mar_0000931148_21_000091.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.


echo.
echo Download complete! Check the SEC_Excel_Downloads folder.
pause
