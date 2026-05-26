@echo off
pyinstaller --onefile --name YellowPather --windowed --add-data "core;core" --add-data "icons;icons" --add-data "settings;settings" --add-data "screenshots;screenshots" main.py
pause