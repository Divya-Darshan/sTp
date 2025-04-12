import pyttsx3
from SpeechCapture import speechcapture as sc

def  voiceto(content):
    engine = pyttsx3.init()
    engine.setProperty('rate',160)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(content)
    engine.runAndWait()




      
            