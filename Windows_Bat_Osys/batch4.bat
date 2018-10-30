@echo off
title batch4
rem PMS (Author)
rem working with user input
echo press 1 if you are having fun
echo press 2 if you want more scripting
set/p press=
if %Press% == 1 goto 1
if %Press% == 2 goto 2
:1
echo Great!!!
pause
exit
:2

