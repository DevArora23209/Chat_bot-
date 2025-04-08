import pyttsx3
import speech_recognition as sr
import wikipedia
import pyjokes
import random
import requests
import datetime
import os
from googlesearch import search
import webbrowser
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def speak(audio):
    engine.say(audio)   
    engine.runAndWait()
def command():
    r = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            print("Danta: Listening...")
            audio=r.listen(source)
            try:    
                query = r.recognize_google(audio)
                print(f"master:{query}")
                return query
                break
            except:
                print("Try Again")
while True:
    query = command().lower()  
    
    if 'name' in query:
        speak("Hello Machine! My  Name is Danta")
    elif 'hate' in query:
        speak("I hate when people called me a machine")
    elif 'love' in query:
        speak("I loves to chat with machines like you")
    elif 'time' in query:
        time = datetime.datetime.now().strftime('%I:%M %p')
        a=("It's", time ,"master")
        speak(a)
        print(a)
    elif 'who is' in query:
        query = query.replace('who is',"")
        speak(wikipedia.summary(query,2))
    elif 'joke' in query:
        for i in range(0,2,1):
            print(i + 1, pyjokes.get_joke())
            speak(pyjokes.get_joke())
    elif 'news' in query:
            def trndnews(): 
                url = "http://newsapi.org/v2/top-headlines?country=in&apiKey=59ff055b7c754a10a1f8afb4583ef1ab"
                page = requests.get(url).json() 
                article = page["articles"] 
                results = [] 
                for ar in article: 
                    results.append(ar["title"]) 
                for i in range(len(results)): 
                    print(i + 1, results[i]) 
                    speak(results[i])
                reply = command().lower()
                reply = str(reply)
                speak('ok master')
                pass
            trndnews() 
    elif 'music' in query:
        music_dir = ''//enter the drive location
        songs = os.listdir(music_dir)
        song = random.randint(0,len(songs)-1)
        print(songs[song])  
        speak(f"playing{songs[song]}")
        os.startfile(os.path.join(music_dir, songs[0]))
    elif "bye" in query:
        speak("Have a nice day ! ")
        break
    elif "search" in query:
        engine = pyttsx3.init('sapi5')
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        def speak(audio):
            engine.say(audio)   
            engine.runAndWait()
        x=0
        def command():
            r = sr.Recognizer()
            while True:
                with sr.Microphone() as source:
                    print("Danta: Listening.....")
                    audio=r.listen(source)
                    try:    
                        query = r.recognize_google(audio)
                        print(f"master:{query}")
                        return query
                        break
                    except:
                        print("Try Again")
                x+=1
                if x==1:
                    break
        while True:
            query = command().lower() 
            for i in search(query, num=1, stop=1, pause=2):
                print(search)
                print(i)
                webbrowser.open(i)
            x+=1
            if x==1:
                break
    else :
        speak("can not understand")
