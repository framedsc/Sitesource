@echo off
echo Executing pre-generate-site hooks scripts
PowerShell -ExecutionPolicy Bypass -File "tools\generate-site-hooks\generatebannerspage.ps1"
.\tools\docnet -c markdown