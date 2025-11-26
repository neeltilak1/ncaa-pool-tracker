@echo off
REM NCAA Basketball Pool Data Updater - Windows Batch File
REM Double-click this file to run the update script

echo ======================================================================
echo NCAA BASKETBALL POOL DATA UPDATER
echo ======================================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Python is not installed or not in PATH
    echo.
    echo Please install Python from: https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation
    echo.
    pause
    exit /b 1
)

echo Running update script...
echo.

REM Run the Python script
python update_pool_data.py

echo.
echo ======================================================================
echo.

if %errorlevel% equ 0 (
    echo SUCCESS! Your pool_data.json has been updated.
    echo.
    echo Next steps:
    echo 1. Upload the updated pool_data.json to GitHub
    echo 2. Or refresh your local tracker page in the browser
) else (
    echo UPDATE FAILED. Please check the error messages above.
    echo.
    echo If auto-fetch doesn't work, use the Manual Edit feature instead.
)

echo.
pause
