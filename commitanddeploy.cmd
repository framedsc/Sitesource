@echo off
REM This little script assumes the framedsc.github.io is in a folder next to the one this is in (so ..\framedsc.github.io)
REM It'll generate, copy and commit the changes made in this repo.
git add -A
git commit -m "Site updated"
git push
docnet -c markdown

del /q ..\framedsc.github.io\*.*
for /d %i in (..\framedsc.github.io\*.*) do @rd /s /q "%i"

robocopy .\site ..\framedsc.github.io /s /e
cd ..\framedsc.github.io
git add -A
git commit -m "Site updated"
git push