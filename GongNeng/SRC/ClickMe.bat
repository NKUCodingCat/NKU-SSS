@echo off
echo 按完选项别按enter！！！！！
echo ===================
choice /c 12 /M "请选择是自评还是互评，1是自评， 2是互评"
if errorlevel 2 goto a
if errorlevel 1 goto b
:a
%~dp0%prog\huping.exe
goto end
:b
%~dp0%prog\ziping.exe
goto end