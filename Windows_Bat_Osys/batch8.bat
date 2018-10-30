@echo off
Title  batch8
rem author PMS
rem run this as a administrator
rem add user and groups
net user student2 password123 /add
rem user named student2 with password = password123
net local group BatchUser / comment:"Batch Fiel Users group" /add
net localgroup BatchUsers student2 /add
:pause

