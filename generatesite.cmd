@echo off
rem Make sure to also add the new hooks to the commitanddeploy.cmd (cant execute generatesite.cmd)
echo Executing pre-generate-site hooks scripts
PowerShell -ExecutionPolicy Bypass -File "tools\generate-site-hooks\generatebannerspage.ps1"
.\tools\docnet -c markdown