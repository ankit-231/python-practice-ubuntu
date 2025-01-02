import pyttsx3

engine = pyttsx3.init(driverName="sapi5")
engine.say("I will speak this text")
engine.runAndWait()
