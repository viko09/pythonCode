import pyttsx3

engine = pyttsx3.init()

"""VOICE"""

voices = engine.getProperty('voices')  # getting details of current voice
# engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
# engine.setProperty('voice', voices.[0].id)  # changing index, changes voices. 1 for female
print(voices)
newVoiceRate = 200

engine.setProperty('rate', newVoiceRate)

engine.say("Hello Victor")
engine.runAndWait()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


speak("This is an admin")
