import speech_recognition as sr
import os
import datetime as dt
import pyttsx3 as pyt
import wikipedia as wiki
import requests as req
from googlesearch import search
from bs4 import BeautifulSoup as bs

engine=pyt.init()
voices=engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

def voice(query):
    engine.say(query)
    engine.runAndWait()

def takeCommand(): 
    r = sr.Recognizer()

    with sr.Microphone() as source: 
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")   
        query = r.recognize_google(audio, language =('en-in'))
        print(f"You said: {query}\n")

    except Exception as e:
        print(e)   
        print("Unable to Recognize your voice.") 
        return "None"  
     
    return query

def speak(s):
    print(s)
    s.replace(".","").replace(",","").replace("-","")
    voice(s)

def wish():
    hour = int(dt.datetime.now().hour)

    if hour>= 0 and hour<12:
        speak("Good Morning Sir !")

    elif hour>= 12 and hour<17:
        speak("Good Afternoon Sir !")  

    else:
        speak("Good Evening Sir !") 
    speak("I am your Assistant , Alpha")


os.system("cls")
wish()

while True: 
    
    print("Enter Your query ...")
    query=takeCommand().lower()

    if query=="nothing" or query=="exit" or query=="no" or query=="not":
        exit()

    elif 'the time' in query:
        time = dt.datetime.now().strftime("%H:%M:%S")
        s="Sir, the time is {}".format(time)   
        speak(s)

    elif 'the date' in query or query=="date":
        time = dt.datetime.now().date().today()
        s="Sir, the date is {}".format(time)   
        speak(s)

    elif 'how are you' in query:
        speak("I am fine, Thank you .... How are you, Sir")
        query=takeCommand().lower()

        if "not" in query or "sad" in query:
            speak("Want some suicide tips? if no then shut your mouth and be happy ")

        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")

    elif "what's your name" in query or "what is your name" in query :
        speak("My friends call me Alpha")

    elif "who are you" in query:
        speak("I am a voice assistant and my name is Alpha")

    elif "what is" in query or "what do you understand" in query or "what do" in query:
        try:
            num=10
            res=search(query,num)

            for i in res:
                url = i
                response = req.get(url)
                soup = bs(response.text,features="html.parser")
                metas = soup.find_all('meta')

                for m in metas:
                    if m.get ('name') == 'description':
                        desc = m.get('content')
                        d=desc.split(".")
                        speak(d[0]) if len(d[0].split())>30 else speak(d[0]+d[1])
                break
        except:
            speak("i am currently having trouble in getting search results sorry for the inconvinience")
            
    elif "none" not in query:
        try:
            s=query.split()
            query=s[-2]+s[-1]
            res=wiki.summary(query,sentences=3)
            s="According to wikipedia"+"\n"+res
            speak(s)
        except:
            speak("Keyword not found in wikipedia please check again or use any other keyword")
    
    speak("Do You want another help?")
    query=takeCommand().lower()
    
    if "no" in query or "not" in query:
        break
    os.system("cls")
