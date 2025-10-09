@echo off
REM Advanced SEC Excel Downloader
REM Generated on 2025-10-07 17:54:27

echo Starting automated SEC Excel download for KMI 10-Q...
echo.

REM Create download directory
if not exist "SEC_Excel_Downloads_KMI_10-Q" mkdir "SEC_Excel_Downloads_KMI_10-Q"
cd "SEC_Excel_Downloads_KMI_10-Q"

echo Download directory created: SEC_Excel_Downloads_KMI_10-Q
echo.

REM Filing #1: KINDER MORGAN, INC.
echo Downloading filing #1...
echo URL: https://www.sec.gov/Archives/edgar/data/1506307/000150630725000045/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "KMI_10-Q_Q2_2025_Jun_0001506307_25_000045.xlsx" "https://www.sec.gov/Archives/edgar/data/1506307/000150630725000045/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded KMI_10-Q_Q2_2025_Jun_0001506307_25_000045.xlsx
) else (
    echo ERROR: Curl failed for KMI_10-Q_Q2_2025_Jun_0001506307_25_000045.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #2: KINDER MORGAN, INC.
echo Downloading filing #2...
echo URL: https://www.sec.gov/Archives/edgar/data/1506307/000150630725000022/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "KMI_10-Q_Q1_2025_Mar_0001506307_25_000022.xlsx" "https://www.sec.gov/Archives/edgar/data/1506307/000150630725000022/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded KMI_10-Q_Q1_2025_Mar_0001506307_25_000022.xlsx
) else (
    echo ERROR: Curl failed for KMI_10-Q_Q1_2025_Mar_0001506307_25_000022.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #3: KINDER MORGAN, INC.
echo Downloading filing #3...
echo URL: https://www.sec.gov/Archives/edgar/data/1506307/000150630724000119/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "KMI_10-Q_Q3_2024_Sep_0001506307_24_000119.xlsx" "https://www.sec.gov/Archives/edgar/data/1506307/000150630724000119/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded KMI_10-Q_Q3_2024_Sep_0001506307_24_000119.xlsx
) else (
    echo ERROR: Curl failed for KMI_10-Q_Q3_2024_Sep_0001506307_24_000119.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #4: KINDER MORGAN, INC.
echo Downloading filing #4...
echo URL: https://www.sec.gov/Archives/edgar/data/1506307/000150630724000074/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "KMI_10-Q_Q2_2024_Jun_0001506307_24_000074.xlsx" "https://www.sec.gov/Archives/edgar/data/1506307/000150630724000074/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded KMI_10-Q_Q2_2024_Jun_0001506307_24_000074.xlsx
) else (
    echo ERROR: Curl failed for KMI_10-Q_Q2_2024_Jun_0001506307_24_000074.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #5: KINDER MORGAN, INC.
echo Downloading filing #5...
echo URL: https://www.sec.gov/Archives/edgar/data/1506307/000150630724000031/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "KMI_10-Q_Q1_2024_Mar_0001506307_24_000031.xlsx" "https://www.sec.gov/Archives/edgar/data/1506307/000150630724000031/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded KMI_10-Q_Q1_2024_Mar_0001506307_24_000031.xlsx
) else (
    echo ERROR: Curl failed for KMI_10-Q_Q1_2024_Mar_0001506307_24_000031.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #6: KINDER MORGAN, INC.
echo Downloading filing #6...
echo URL: https://www.sec.gov/Archives/edgar/data/1506307/000150630723000118/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "KMI_10-Q_Q3_2023_Sep_0001506307_23_000118.xlsx" "https://www.sec.gov/Archives/edgar/data/1506307/000150630723000118/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded KMI_10-Q_Q3_2023_Sep_0001506307_23_000118.xlsx
) else (
    echo ERROR: Curl failed for KMI_10-Q_Q3_2023_Sep_0001506307_23_000118.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #7: KINDER MORGAN, INC.
echo Downloading filing #7...
echo URL: https://www.sec.gov/Archives/edgar/data/1506307/000150630723000081/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "KMI_10-Q_Q2_2023_Jun_0001506307_23_000081.xlsx" "https://www.sec.gov/Archives/edgar/data/1506307/000150630723000081/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded KMI_10-Q_Q2_2023_Jun_0001506307_23_000081.xlsx
) else (
    echo ERROR: Curl failed for KMI_10-Q_Q2_2023_Jun_0001506307_23_000081.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #8: KINDER MORGAN, INC.
echo Downloading filing #8...
echo URL: https://www.sec.gov/Archives/edgar/data/1506307/000150630723000036/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "KMI_10-Q_Q1_2023_Mar_0001506307_23_000036.xlsx" "https://www.sec.gov/Archives/edgar/data/1506307/000150630723000036/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded KMI_10-Q_Q1_2023_Mar_0001506307_23_000036.xlsx
) else (
    echo ERROR: Curl failed for KMI_10-Q_Q1_2023_Mar_0001506307_23_000036.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #9: KINDER MORGAN, INC.
echo Downloading filing #9...
echo URL: https://www.sec.gov/Archives/edgar/data/1506307/000150630722000111/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "KMI_10-Q_Q3_2022_Sep_0001506307_22_000111.xlsx" "https://www.sec.gov/Archives/edgar/data/1506307/000150630722000111/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded KMI_10-Q_Q3_2022_Sep_0001506307_22_000111.xlsx
) else (
    echo ERROR: Curl failed for KMI_10-Q_Q3_2022_Sep_0001506307_22_000111.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #10: KINDER MORGAN, INC.
echo Downloading filing #10...
echo URL: https://www.sec.gov/Archives/edgar/data/1506307/000150630722000083/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "KMI_10-Q_Q2_2022_Jun_0001506307_22_000083.xlsx" "https://www.sec.gov/Archives/edgar/data/1506307/000150630722000083/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded KMI_10-Q_Q2_2022_Jun_0001506307_22_000083.xlsx
) else (
    echo ERROR: Curl failed for KMI_10-Q_Q2_2022_Jun_0001506307_22_000083.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #11: KINDER MORGAN, INC.
echo Downloading filing #11...
echo URL: https://www.sec.gov/Archives/edgar/data/1506307/000150630722000037/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "KMI_10-Q_Q1_2022_Mar_0001506307_22_000037.xlsx" "https://www.sec.gov/Archives/edgar/data/1506307/000150630722000037/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded KMI_10-Q_Q1_2022_Mar_0001506307_22_000037.xlsx
) else (
    echo ERROR: Curl failed for KMI_10-Q_Q1_2022_Mar_0001506307_22_000037.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #12: KINDER MORGAN, INC.
echo Downloading filing #12...
echo URL: https://www.sec.gov/Archives/edgar/data/1506307/000150630721000106/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "KMI_10-Q_Q3_2021_Sep_0001506307_21_000106.xlsx" "https://www.sec.gov/Archives/edgar/data/1506307/000150630721000106/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded KMI_10-Q_Q3_2021_Sep_0001506307_21_000106.xlsx
) else (
    echo ERROR: Curl failed for KMI_10-Q_Q3_2021_Sep_0001506307_21_000106.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #13: KINDER MORGAN, INC.
echo Downloading filing #13...
echo URL: https://www.sec.gov/Archives/edgar/data/1506307/000150630721000079/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "KMI_10-Q_Q2_2021_Jun_0001506307_21_000079.xlsx" "https://www.sec.gov/Archives/edgar/data/1506307/000150630721000079/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded KMI_10-Q_Q2_2021_Jun_0001506307_21_000079.xlsx
) else (
    echo ERROR: Curl failed for KMI_10-Q_Q2_2021_Jun_0001506307_21_000079.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #14: KINDER MORGAN, INC.
echo Downloading filing #14...
echo URL: https://www.sec.gov/Archives/edgar/data/1506307/000150630721000032/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "KMI_10-Q_Q1_2021_Mar_0001506307_21_000032.xlsx" "https://www.sec.gov/Archives/edgar/data/1506307/000150630721000032/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded KMI_10-Q_Q1_2021_Mar_0001506307_21_000032.xlsx
) else (
    echo ERROR: Curl failed for KMI_10-Q_Q1_2021_Mar_0001506307_21_000032.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #15: KINDER MORGAN, INC.
echo Downloading filing #15...
echo URL: https://www.sec.gov/Archives/edgar/data/1506307/000150630720000097/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "KMI_10-Q_Q3_2020_Sep_0001506307_20_000097.xlsx" "https://www.sec.gov/Archives/edgar/data/1506307/000150630720000097/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded KMI_10-Q_Q3_2020_Sep_0001506307_20_000097.xlsx
) else (
    echo ERROR: Curl failed for KMI_10-Q_Q3_2020_Sep_0001506307_20_000097.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #16: KINDER MORGAN, INC.
echo Downloading filing #16...
echo URL: https://www.sec.gov/Archives/edgar/data/1506307/000150630720000067/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "KMI_10-Q_Q2_2020_Jun_0001506307_20_000067.xlsx" "https://www.sec.gov/Archives/edgar/data/1506307/000150630720000067/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded KMI_10-Q_Q2_2020_Jun_0001506307_20_000067.xlsx
) else (
    echo ERROR: Curl failed for KMI_10-Q_Q2_2020_Jun_0001506307_20_000067.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.

REM Filing #17: KINDER MORGAN, INC.
echo Downloading filing #17...
echo URL: https://www.sec.gov/Archives/edgar/data/1506307/000150630720000041/Financial_Report.xlsx

REM Try curl first
curl -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" --retry 3 --retry-delay 2 -o "KMI_10-Q_Q1_2020_Mar_0001506307_20_000041.xlsx" "https://www.sec.gov/Archives/edgar/data/1506307/000150630720000041/Financial_Report.xlsx"
if %errorlevel% equ 0 (
    echo SUCCESS: Downloaded KMI_10-Q_Q1_2020_Mar_0001506307_20_000041.xlsx
) else (
    echo ERROR: Curl failed for KMI_10-Q_Q1_2020_Mar_0001506307_20_000041.xlsx
)

REM Add delay between downloads
timeout /t 3 /nobreak >nul
echo.


echo.
echo Download complete! Check the SEC_Excel_Downloads folder.
pause
