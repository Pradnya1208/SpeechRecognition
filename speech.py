import speech_recognition as sr
from time import ctime
import webbrowser
import time
import os
import random
from gtts import gTTS
import playsound



r = sr.Recognizer()    #for recognizing the speech

def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            speak (ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            speak("I did not get that")
        except sr.RequestError:
            speak("Speech service is down")
        return voice_data


def speak(audio_string):
    tts = gTTS(text = audio_string, lang = 'en')
 
    r  = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

    
# demo 
def respond(voice_data):
    if 'what is your name' in voice_data:
        speak('My name is Khaleesi')
    
    if 'what time is it' in voice_data:
        speak(ctime())
        
    if 'search' in voice_data:
        search = record_audio('what do you want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        speak('Here is what I found for ' + search)
        
    if 'find location' in voice_data:
        location = record_audio('All right, tell me the location')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        speak('Here is the location ' + location)

    if 'exit' in voice_data:
        speak('Okay, Good bye!')
        exit()



time.sleep(1)     
speak('How can I help you?')

while 1:
    voice_data = record_audio()
    #print(voice_data)
    respond(voice_data)
