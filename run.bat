@ECHO off
cls
:start
ASCII.py
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
ECHO installing requests
pip install requests
cls
ECHO installing random
pip install random
cls
ECHO installing threading
pip install threading
cls
ECHO installing ctypes
pip install ctypes
cls
ASCII.py


gsteal.py
goto end
:config
configwrite.py
goto end
:end