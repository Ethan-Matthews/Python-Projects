@echo off
Title  batch7
rem author PMS
rem working "if not"
set /p pass=enter passowrds
if %pass% == welcome goto correct
:correct
cls
echo Well done - correct
pause
exit
:incorrect
echo opps, sorry wrong passoword
pause
:end


