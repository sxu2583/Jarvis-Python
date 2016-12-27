"""
This is going to be a soon to be autobiography via
a python recurrent neural network but right now its
going to be hardcoded via pyttsx in order to create a
foundation
"""

#Import text to speech
import pyttsx
#TODO: Create the neural network foundation

engine = pyttsx.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say("What is my purpose?")
"""
for voice in voices:
    engine.setProperty('voice', voice.id)
    engine.say("What Is my purpose?")
"""
engine.runAndWait()