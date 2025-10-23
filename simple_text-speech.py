import pyttsx3              # A text-to-speech conversion library in Python working offline.
engine = pyttsx3.init()              #start the pyttsx3 engine
text = input("Enter the text you want to convert to speech: ")
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  #  # 0 = male, 1 = female (varies by system)
engine.setProperty('rate', 150)  # default ~200
engine.say(text)
engine.runAndWait()