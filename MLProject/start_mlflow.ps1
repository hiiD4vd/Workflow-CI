Write-Host "=========================================================="
Write-Host "MEMULAI MLFLOW UI DENGAN DATABASE LOKAL..."
Write-Host "Silakan buka http://127.0.0.1:5000 di browser Anda"
Write-Host "=========================================================="
mlflow ui --backend-store-uri sqlite:///mlflow.db
