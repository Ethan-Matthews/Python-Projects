echo
mkdir C:\Scripts
net user ABruce /add /comment:"COMMENT" /passwordchg:NO
wmic useraccount where "name='ABruce'" set passwordexpires = False
net localgroup management ABruce \add
mkdir E:/companyInc\management\ABruceFiles
icacls E:/ CompanyInc\management\ABruceFiles /grants ABruce:(OI)(CI)F /T
icacls E:/ CompanyInc\management\ABruceFiles /save C:\Scripts\icaclsreport.txt/T
cd C:\
xcopy C:\windows\system32\cmd.exe e:\companyInc\Management\ABruceFiles /O/X/E/H/K
Move F:\newuser.bat C:\Scripts
