#!/usr/bin/env python3
# Requires PyAudio and PySpeech.
"""
Using the python pyAudio and speech libraries we
will convert speech to text via a built in learning
algorithm similar to google api.

Algorithm -> Google api -> Text
"""

import speech_recognition as sr

# Record Audio
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
        
        print("I don't know the answer\n")
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

