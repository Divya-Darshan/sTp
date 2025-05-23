@echo off
:loop
echo _________________________________
echo Ask me something...
set /p in=You:

:: Replace spaces with underscores (Wikipedia expects underscores)
set "query=%in: =_%"

:: Call PowerShell to fetch and print the summary
powershell -Command ^
  "try { $res = Invoke-RestMethod 'https://en.wikipedia.org/api/rest_v1/page/summary/%query%'; Write-Host $res.extract } catch { Write-Host 'Page not found or error.' }"

echo _________________________________
goto loop 