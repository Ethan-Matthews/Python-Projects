@echo off
Title  batch8
rem author PMS
rem check permissions
icacls c:\practice > c:\scripts\icaclsReport.txt
icacls c:\practice
echo Created file: c:\scipts\icaclsReports.txt
pause 
