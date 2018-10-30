@echo off
Title  batch8
rem author PMS
rem wirking with permissions
rem this has to be run as a an administrator
rem assign permissions to my practice directory
icacls c:\practice /grant BatchUser: (OI) (CL) RX
pause
