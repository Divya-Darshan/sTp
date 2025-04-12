from SpeechCapture import speechcapture as sc
from voiceTo import voiceto as vt
import os
import keyboard
from deepseek import call_deep as cd  

vt('Deepseek have initialised!.')

while True:  
    try:  
        if keyboard.is_pressed('ctrl') and keyboard.is_pressed('q'):
            cd()
            
    except:
        pass