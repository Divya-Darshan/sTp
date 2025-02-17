import pyautogui
import os
import time
import win32com.client

file_path = os.path.abspath(r'C:\Users\paruk\Documents\Python\STP\Log')  


shell = win32com.client.Dispatch("WScript.Shell")

def speechcapture():
    shell.Run(f'notepad.exe {file_path}', 1) 
    time.sleep(0.5) 
    pyautogui.hotkey('win', 'h')
    time.sleep(5)
    pyautogui.hotkey('ctrl', 's')
    time.sleep(0.1)
    with open('C:\\Users\\paruk\\Documents\\Python\\STP\\Log', 'r') as file:
        content = file.read()  
        print(content)
    pyautogui.hotkey('ctrl', 'w')
    