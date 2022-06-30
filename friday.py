import webbrowser
import pyttsx3
import datetime
import pyaudio
import speech_recognition as sr
import wikipedia
import os
import spotify
# like windows inbult voice type 
engine = pyttsx3.init('sapi5') 
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[1].id)  #male voice (total 3 voces exist)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning sir, the time is")
    elif hour>=12 and hour<18:
        speak("Good afternoon sir")
    else:
        speak("Good evening sir!")


def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=0.8
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")
    except Exception as e:
        print(e)
        return "None"
    return query

while 1:
   q1=takeCommand().lower()
   speak('taking command')
   query=takeCommand().lower()
   if ('wikipedia' in query):
       query= query.replace("wikipedia","")
       results=wikipedia.summary(query,sentences=3)
       speak(results)
   elif 'open YouTube' in query:
       speak("opening youtube")
       webbrowser.open("youtube.com")
   elif 'open stackoverflow' in query:
       speak("opening stack overflow")
       webbrowser.open("stackoverflow.com")
   elif 'open google' in query:
       speak("opening google")
       webbrowser.open("google.com")
   elif 'is time' in query:
       strtime=datetime.datetime.now().strftime("%H:%M:%S")
       wishme()
       speak(f"the time is {strtime}")
   elif 'open code' in query:
       speak("opening visual code")
       pypath="C:\\Users\\sandi\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
       os.startfile(pypath)
   elif ('open teams' in query) or ('open team' in query):
       speak("opening teams")
       n="\"Teams.exe\""
       teampath= "C:\\Users\\sandi\\AppData\\Local\\Microsoft\\Teams\\Update.exe --processStart {}".format(n)
       #--processStart \"Teams.exe\"
       os.system(teampath)
   elif ('open spotify' or 'spotify') in query:
       speak("opening spotify")
       os.system("spotify")
   elif ('hai' or 'hello') in query:
       speak("hello sir this is jarvis, how may i help you")
   elif ('stop' or 'end' or 'quit') in query:
       exit(0)
   else:
       speak("sorry i dont know that")


