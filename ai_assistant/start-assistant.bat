@echo off
REM AI Assistant Startup Script for Windows

echo.
echo ====================================
echo  AI Personal Assistant - Startup
echo ====================================
echo.

REM Check if Ollama is running
tasklist | find /i "ollama" >nul
if errorlevel 1 (
    echo.
    echo ⚠️  WARNING: Ollama is not running!
    echo.
    echo You need to start Ollama in a separate terminal:
    echo   ollama serve
    echo.
    echo Then come back here.
    echo.
    pause
) else (
    echo ✓ Ollama is running
)

REM Navigate to project directory
cd /d "c:\Users\Harshavardhan\Desktop\internship\ai-assistant"

REM Check if venv exists
if not exist "venv\" (
    echo.
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate venv
echo.
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Start backend
echo.
echo Starting AI Assistant Backend...
echo.
cd backend
python app.py

REM If script reaches here, Flask crashed
echo.
echo ⚠️  Backend stopped. Press any key to exit...
pause
