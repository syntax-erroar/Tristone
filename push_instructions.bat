@echo off
echo ========================================
echo Pushing Code to GitHub Repository
echo ========================================
echo.
echo Repository: https://github.com/tristone-financial-spread/finance.git
echo.
echo Current status:
git status
echo.
echo Attempting to push...
git push -u origin main
echo.
echo If push fails, try:
echo 1. Check if repository exists on GitHub
echo 2. Authenticate with GitHub (use Personal Access Token)
echo 3. Wait a few minutes for repository to be fully created
echo.
pause
