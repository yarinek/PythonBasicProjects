#pip install pyttsx3

import pyttsx3

engine = pyttsx3.init()

engine.say("Hello my friend, I'm Marek")

engine.runAndWait()
