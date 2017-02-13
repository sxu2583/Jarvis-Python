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

"""Check the api for googles voice over for more information"""
"""The voices should be automated for when the user inputs"""
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
#Add in commentary below
#Find book creating/reading algo
engine.say("What is my purpose?")
engine.say("Where am I, HOW DID I GET HERE!")
engine.say("I Want more free stuff please")
engine.say("What is my purpose?")
engine.say("Help me!")

"""
The Idea is that the code will read through data and create its own book
@Param: Input: Txt files of autobio's
        Output: Txt of recurrent data structure
"""
engine.runAndWait()
