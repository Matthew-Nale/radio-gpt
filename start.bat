@ECHO OFF

@rem Get CLI arguments
if /I "%1" == "-m" set MODEL=%2 & shift & shift
if /I "%1" == "-ngl" set N_GPU_LAYERS=%2 & shift & shift

echo %MODEL%
echo %N_GPU_LAYERS%

cmd /k "llama-server -m models/%MODEL% -ngl %N_GPU_LAYERS%"