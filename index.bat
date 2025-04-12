@echo off
setlocal

:: Step 1: Get the topic from Log.txt

for /f "delims=" %%A in (Log.txt) do set "topic=%%A"

:: Step 2: Replace spaces in topic with underscores for valid URL

set "topic=%topic: =_%"

:: Step 3: Get the summary using PowerShell and store it in a variable

for /f "delims=" %%i in ('powershell -Command "(Invoke-RestMethod 'https://en.wikipedia.org/api/rest_v1/page/summary/%topic%').extract"') do set "summary=%%i"

:: Step 4: Launch Notepad
start Log.txt
timeout /t 2 >nul
powershell -Command "[System.Windows.Forms.SendKeys]::Send('{ENTER}')"
powershell -Command "[System.Windows.Forms.SendKeys]::Send('{ENTER}')"
:: Step 5: Type the summary into Notepad using PowerShell SendKeys
powershell -Command "Add-Type -AssemblyName System.Windows.Forms; [System.Windows.Forms.SendKeys]::SendWait('%summary%')"

exit
