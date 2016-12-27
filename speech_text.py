#!/usr/bin/env python3
# Requires PyAudio and PySpeech.
"""
Using the python pyAudio and speech libraries we
will convert speech to text via a built in learning
algorithm similar to google api.

Algorithm -> Google api -> Text
"""

"""
You need to have your sound turned on otherwise an erorr occurs via the
exception error that wasn't converted from python 2.7 to 3.6
"""

#This is the speech to text
import pyttsx
#This is the text to speech
import speech_recognition as sr
engine = pyttsx.init()

# Record Audio
print("Hi my name is Tito")
engine.say("Hi my name is Tito el diablo")
name = input("What is your name?")
engine.say("You said your name was "+ name)

if name == "Shihab":
    engine.say("That's a beautiful name")
else:
    engine.say(name+"...That's a stupid name")

z = int(input("How many questions do you have? "))

for i in range(0, z):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I heard your question!!!!")
        audio = r.listen(source)
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        print("You said...: " + r.recognize_google(audio))
        engine.say('You said'+r.recognize_google(audio))
        engine.runAndWait()

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

