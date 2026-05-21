Write-Host "=========================================================="
Write-Host "MEMULAI MLFLOW UI (VERSI LOCAL FOLDER)..."
Write-Host "Silakan buka http://127.0.0.1:5000 di browser Anda"
Write-Host "=========================================================="
mlflow ui --backend-store-uri file://$PWD/mlruns
