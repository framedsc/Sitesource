@echo off
REM This little script assumes the framedsc.github.io is in a folder next to the one this is in (so ..\framedsc.github.io)
REM It'll generate, copy and commit the changes made in this repo.
REM Pass a string for the commit message

git add -A
git commit -m %1
git push
start cmd.exe /c generatesite.cmd

del /q ..\framedsc.github.io\*.*
for /d %%i in (..\framedsc.github.io\*.*) do @rd /s /q "%%i"

copy /y theme\destination\favicon.ico .\site

robocopy .\site ..\framedsc.github.io /s /e
pushd.
cd ..\framedsc.github.io
rem git add -A
rem git commit -m %1
rem git push
popd