@ECHO OFF

echo Starting Llama Server...

cmd /k "llama-server -m models/BaseModel.gguf -ngl 33"