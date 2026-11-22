@echo off
echo Starting CRC Code Simulator GUI...
cd /d "%~dp0"
python launch_gui.py
if errorlevel 1 (
    echo Error starting GUI. Please check Python installation.
    pause
)
