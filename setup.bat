@ECHO off

echo.
echo Setting up Node.js dependencies...

REM Check if Node.js is installed
@node -v > nul 2>&1
if %errorlevel% neq 0 (
    echo.
    echo Node.js is not installed.
    exit /b 1
)

if exist "node_modules" (
    echo.
    echo The "node_modules" directory already exists.
    echo To force a fresh installation, delete the directory and run this script again.
) else (
    npm install
)

echo.
echo Node packages installed.
echo.

echo.
echo Installing Python dependencies..
echo.

pip install -r requirements.txt

echo.
echo Python dependencies installed.
echo.

echo.
where llama-server >nul
if %ERRORLEVEL% NEQ 0 (
    echo Installing llama-server...

    winget install llama.cpp
) else (
    echo llama-server already installed...
)