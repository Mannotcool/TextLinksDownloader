@echo off
echo Loading downloader and urls.txt.
timeout /t 3
cls
echo Loaded! Starting...
timeout /t 1
python download.py
timeout /t 1
cls
echo Finshed, please press any button to exit!
pause