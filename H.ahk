; Define the hotkey to press Win + H
Send, {LWin down}h{LWin up}

; Check if the desired window is open
IfWinExist, YourWindowTitle
{
    ; If window exists, focus it
    WinActivate
}
else
{
    ; If window doesn't exist, send Win + H again to open it
    Send, {LWin down}h{LWin up}
}

return
