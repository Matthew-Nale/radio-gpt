@ECHO OFF

echo.
echo Starting Llama Server...

start "Llama Server" llama-server -m gpt/models/BaseModel.gguf -ngl 33

echo Starting MySQL Docker...

start "MySQL Server" docker compose up --build

echo Starting Flask Backend...

echo Starting Flask Backend...

cd app
start "Flask Backend" flask run --debug
cd ..

echo Press any key to end all processes...
pause >nul

taskkill /IM llama-server.exe /F >nul

docker compose stop
taskkill /FI "WINDOWTITLE eq MySQL Server" >nul

taskkill /FI "WINDOWTITLE eq Flask Backend" >nul