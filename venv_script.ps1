# 1. Якщо є venv — видаляємо
if (Test-Path "venv") {
    Write-Host ">>> Delete old venv..."
    Remove-Item -Recurse -Force "venv"
}

# 2. Створюємо нове
Write-Host ">>> Create nev inv venv..."
py -m venv venv

# 3. Активуємо
Write-Host ">>> Activate env..."
& .\venv\Scripts\Activate.ps1

# 4. Якщо є requirements.txt — встановлюємо
if (Test-Path "requirements.txt") {
    Write-Host ">>> Install pakages from requirements.txt..."
    pip install -r requirements.txt
}
else {
    Write-Host ">>> File requirements.txt not found"
}

# 5. Перевірка
python --version
pip list
Write-Host ">>> Deactivate inv..."
deactivate
