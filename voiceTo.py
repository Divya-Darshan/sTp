import pyttsx3

def  voiceto(txt):
    
    engine = pyttsx3.init()
    engine.setProperty('rate',190)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(txt)
    engine.runAndWait()




      
            