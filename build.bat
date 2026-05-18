@echo off
pyinstaller --onedir --name YellowPather --windowed --add-data "core;core" --add-data "icons;icons" --add-data "settings;settings" main.py