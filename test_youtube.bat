@echo off
REM YouTube Download Test Script
echo ================================================
echo    YouTube Download Test (Desktop Version)
echo ================================================
echo.

REM Check if URL provided
if "%~1"=="" (
    echo Usage: test_youtube.bat "YOUTUBE_URL"
    echo.
    echo Example:
    echo   test_youtube.bat "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    echo.
    echo This will test if YouTube downloads work on your system.
    pause
    exit /b 1
)

echo Testing YouTube download with desktop version...
echo URL: %~1
echo.

REM Activate virtual environment
call .venv\Scripts\activate.bat

REM Test download
python main.py "%~1" --output test_output

echo.
echo ================================================
if exist "test_output" (
    echo ✅ SUCCESS: YouTube download works!
    echo Check the 'test_output' folder for your video.
) else (
    echo ❌ FAILED: Check error messages above.
)
echo ================================================
pause