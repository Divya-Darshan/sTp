import pyautogui
import os
import time
import win32com.client


file_path = os.path.abspath(r'C:\Users\paruk\Documents\Python\STP\Log')  


shell = win32com.client.Dispatch("WScript.Shell")



def speechcapture():
    iterate_time = True

    shell.Run(f'notepad.exe {file_path}', 1) 

    with open('C:\\Users\\paruk\\Documents\\Python\\STP\\Log', 'w') as file:
        pass
    time.sleep(1)
    pyautogui.hotkey('win', 'h')

    if iterate_time:
        time.sleep(5)
        iterate_time = False
    else:
        time.sleep(5)

    pyautogui.hotkey('ctrl', 's')
    time.sleep(0.1)
    with open('C:\\Users\\paruk\\Documents\\Python\\STP\\Log', 'r') as file:
        content = file.read()

    pyautogui.hotkey('ctrl', 'w')

    return content
    