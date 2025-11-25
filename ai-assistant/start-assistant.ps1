# AI Personal Assistant - PowerShell Startup Script

Write-Host "`n===================================" -ForegroundColor Cyan
Write-Host " AI Personal Assistant - Startup" -ForegroundColor Cyan
Write-Host "===================================" -ForegroundColor Cyan
Write-Host ""

# Check if Ollama is running
$ollamaRunning = Get-Process ollama -ErrorAction SilentlyContinue
if (-not $ollamaRunning) {
    Write-Host "⚠️  WARNING: Ollama is not running!" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "You need to start Ollama in a SEPARATE terminal window:" -ForegroundColor Yellow
    Write-Host "  ollama serve" -ForegroundColor Green
    Write-Host ""
    Write-Host "Then come back here." -ForegroundColor Yellow
    Write-Host ""
    Read-Host "Press Enter when Ollama is running"
} else {
    Write-Host "✓ Ollama is running" -ForegroundColor Green
}

# Navigate to project
Set-Location "c:\Users\Harshavardhan\Desktop\internship\ai-assistant"

# Create venv if it doesn't exist
if (-not (Test-Path "venv")) {
    Write-Host "`nCreating virtual environment..." -ForegroundColor Cyan
    python -m venv venv
}

# Activate venv
Write-Host "`nActivating virtual environment..." -ForegroundColor Cyan
& ".\venv\Scripts\Activate.ps1"

# Start backend
Write-Host "`nStarting AI Assistant Backend..." -ForegroundColor Green
Write-Host ""
Set-Location backend
python app.py

# If script reaches here, Flask crashed
Write-Host "`n⚠️  Backend stopped!" -ForegroundColor Yellow
Read-Host "Press Enter to exit"
