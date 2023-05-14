@echo off

REM Set the path to the Python script
set PYTHON_SCRIPT="C:\path\to\python\script.py"

:loop
REM Check if the Python script is running
tasklist /fi "imagename eq python.exe" /fi "windowtitle eq %PYTHON_SCRIPT%" | find ":" > nul
if %errorlevel% neq 0 (
    REM If the Python script is not running, start it
    echo Starting Python script...
    start "" python %PYTHON_SCRIPT%
)

REM Wait for 5 minutes before checking again
timeout /t 300 > nul

goto loop

REM To stop the script, press Ctrl + C in the command prompt.