@echo off
:: Cambia la directory corrente in quella dove si trova questo script
cd /d "%~dp0"

:: Avvia l'assistente usando Python
python src\main.py

:: Mette in pausa per poter leggere eventuali errori se il programma si chiude di colpo
pause
