@echo off
REM Simple YouTube Downloader - No Setup Required!
echo ================================================
echo    YouTube Video Downloader (Desktop Version)
echo ================================================
echo.

REM Activate virtual environment
call .venv\Scripts\activate.bat

REM Check if URL provided as argument
if "%~1"=="" (
    echo Usage: download.bat "VIDEO_URL"
    echo.
    echo Example:
    echo   download.bat "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    echo.
    pause
    exit /b 1
)

REM Download the video
echo Downloading: %~1
echo.
python main.py "%~1"

echo.
echo ================================================
echo Download complete! Check the 'downloads' folder
echo ================================================
pause
