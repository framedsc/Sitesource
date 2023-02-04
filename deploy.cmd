@echo off
REM This little script assumes the framedsc.github.io is in a folder next to the one this is in (so ..\framedsc.github.io)
REM It'll generate, copy and commit the changes made to the repo where the site
REM is hosted.

echo Executing pre-generate-site hooks scripts
PowerShell -ExecutionPolicy Bypass -File "tools\generate-site-hooks\generatebannerspage.ps1"

del /q ..\framedsc.github.io\*.*
for /d %%i in (..\framedsc.github.io\*.*) do @rd /s /q "%%i"

copy /y theme\destination\favicon.ico .\site

robocopy .\site ..\framedsc.github.io /s /e
pushd.
cd ..\framedsc.github.io
git add -A
git commit -m %1
git push
popd
