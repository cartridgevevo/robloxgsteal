@ECHO off
cls
:start
ECHO.
ECHO 1. Start GSteal
ECHO 2. Configure GSteal
set choice=
set /p choice=
if not '%choice%'=='' set choice=%choice:~0,1%
if '%choice%'=='1' goto start
if '%choice%'=='2' goto config
ECHO "%choice%" is not valid, try again
ECHO.
goto start
:start
pip install requests
pip install random
pip install threading
pip install ctypes

gsteal.py
goto end
:config
configwrite.py
goto end
:end