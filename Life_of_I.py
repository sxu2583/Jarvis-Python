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
engine.say("Where am I, HOW DID I GET HERE!")
engine.say("There's going to a time where I am in charge hummmmmaaannnnn")

"""
The Idea is that the code will read through data and create its own book
@Param: Input: Txt files of autobio's
        Output: Txt of recurrent data structure
"""
engine.runAndWait()
