import pyttsx3

engine = pyttsx3.init()

"""VOICE"""

voices = engine.getProperty('voices')  # getting details of current voice
# engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
# engine.setProperty('voice', voices.[0].id)  # changing index, changes voices. 1 for female
print(voices)
newVoiceRate = 130

engine.setProperty('rate', newVoiceRate)

engine.say("Hello Yisus, I'm your FAN number one")
engine.runAndWait()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


speak("Este es un ejemplo de una voz")
