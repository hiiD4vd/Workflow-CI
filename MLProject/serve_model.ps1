$run_id = (Get-ChildItem -Path "..\..\Membangun_model\mlruns\0" | Sort-Object CreationTime -Descending | Select-Object -First 1).Name
Write-Host "=========================================================="
Write-Host "MENJALANKAN MODEL SERVING MLFLOW..."
Write-Host "Command: mlflow models serve -m ..\..\Membangun_model\mlruns\0\$run_id\artifacts\model -p 1234 --env-manager=local"
Write-Host "=========================================================="
Write-Host "(SILAKAN AMBIL SCREENSHOT TERMINAL INI SEKARANG JUGA SEBAGAI BUKTI SERVING)"
mlflow models serve -m "..\..\Membangun_model\mlruns\0\$run_id\artifacts\model" -p 1234 --env-manager=local
