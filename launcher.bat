@echo off
:: On se place dans le dossier du projet
cd /d "%~dp0"

:: On active ton environnement virtuel
call .venv\Scripts\activate.bat

:: L'astuce magique : On utilise 'start' pour détacher le processus
:: et 'pythonw' pour ne pas générer de console noire.
start "" pythonw src\ProjetIAB2Q2\main.py

:: On ferme immédiatement le petit script .bat
exit