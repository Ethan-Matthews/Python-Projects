@Echo off
Title NewUser

rem Author:    Ethan Matthews
rem Date:      Oct, 27th, 2018
rem Revised:   
rem Run this file as an Administrator!

rem Create new folder on C:\ named "Scripts"
rem Add Local user "Aisha Bruce" "ABruce"
rem Set password to "student"
rem Create new folder "ABruce" in E:\CompanyInc\Management 
rem Create ACE for "ABruce" with permissions Full Control
rem Copies Application cmd.exe C:\Windows\System32 to "ABruce Files" Folder
rem Add "ABruce" to Management group
rem Produce Icacls report for "ABruce Files" called "icaclsReport.txt" in root scripts
rem Moves "NewUser.bat" to root C:\Scripts

mkdir C:\Scripts
cd C:\Scripts
echo Scripts folder Created.
pause
net user ABruce student /Add
net user ABruce /active:YES
echo New User ABruce Created/Activated.
pause
cd /d E:\CompanyInc\Management
mkdir "ABruce Files"
echo ABruce folder created in E:\CompanyInc\Management.
pause
icacls "E:\CompanyInc\Management\ABruce Files" /grant S-1-5-21-2349814851-1339320263-2864709163-1005: (F), (OI), (CI)
echo Created ACE for ABruce to the ABruce Files folder with fullcontrol
echo and re-established inheritance permissions.
pause
cd /d E:\CompanyInc\Management\"ABruce Files"
copy C:\Windows\System32\cmd.exe
Echo Copied cmd.exe from C:\Windows\System32 to E:\CompanyInc\Management\ABruce Files
pause
net localgroup Management ABruce /Add
echo Added ABruce to securities group Management.
pause
cd /d C:\Scripts
icacls C:\Scripts > icaclsReport.txt
Echo created icacls report in C:\Scripts.
move F:\NewUser.bat C:\Scripts
echo Moved NewUser.bat from F:\ to C:\Scripts
echo This script has completed all operations.
echo GoodBye.
pause
exit