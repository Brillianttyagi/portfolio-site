from gtts import gTTS
import playsound
import speech_recognition as sr
import os

def speak(text):
    txt = gTTS(text = text,lang="en")
    file_name = "1.mp3"
    txt.save(file_name)
    playsound.playsound(file_name)

speak("Welcome to website")
