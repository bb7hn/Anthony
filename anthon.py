import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os
import sys
import urllib.request
import urllib.parse
import re
import selenium
from selenium import webdriver
import pyautogui
import time
from selenium.webdriver.firefox.options import Options
from termcolor import colored
import colorama
import requests

colorama.init()
engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 180)
client = wolframalpha.Client('5JJA44-V9T6LEVTEA')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)


name = "anthony"
driver = webdriver.Firefox()
driver.set_window_size(1, 1)

def speak(audio):
    print(colored(name.capitalize()+":",'red')+audio+ "\n")
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning Sir')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon Sir')

    if currentH >= 18 and currentH !=0:
        speak('Good Evening Sir')

greetMe()




def myCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print(colored("You: ", 'green') + query + "\n")

    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get that! Try tell it again please!')
        return '000'

    return query.lower()
    
def bglstn():

    rec = sr.Recognizer()
    with sr.Microphone() as source:
        rec.pause_threshold =  1
        audio = rec.listen(source)
    try:
        query = rec.recognize_google(audio, language='en-in')


    except sr.UnknownValueError:
       query="ok"
    return query.lower()
def netflix():
    speak("Which Movie?")
    fname = myCommand()
    while(fname=="000"):
        fname=myCommand()
    speak("From Netflix?")
    correcting=myCommand()
    while(correcting=="000"):
        correcting=myCommand()
    if "yes" in correcting:
        webbrowser.open("https://www.netflix.com/search?q=" + fname)
        speak("Here are the results from Netflix sir")
    elif "yep" in correcting:
        webbrowser.open("https://www.netflix.com/search?q=" + fname)
        speak("Here are the results from Netflix sir")
    elif "all right" in correcting:
        webbrowser.open("https://www.netflix.com/search?q=" + fname)
        speak("Here are the results from Netflix sir")
    elif "absolutely" in correcting:
        webbrowser.open("https://www.netflix.com/search?q=" + fname)
        speak("Here are the results from Netflix sir")
    elif "exactly" in correcting:
        webbrowser.open("https://www.netflix.com/search?q=" + fname)
        speak("Here are the results from Netflix sir")
    else:
        driver.set_window_size(600, 800)
        driver.get("https://www.fullhdfilmizlesene.net/arama/"+ fname)
        speak("Here are the results from a website sir")


def netsurf(url):
    speak('okay')
    webbrowser.open(url)
def music():
    print("""
                ____________#####
                _____________####
                _____________###
                _____________###
                _____________###
                _____________###
                _____________###
                _____________###
                _____________###__##
                _____________###__#__#
                _____________###___#__#
                _____________###___#___#
                _____________###___#____#
                _______##____###__#____#
                ______#__#__######____#
                ______#___##_____#____###
                _______#____#####____##
                ________#___________####
                _________#_________###
                _________##_______###
                ________##_________###
                _______##___________###
                ______##______##_____##
                _____##_____#_____#___##
                _____##______####_____##
                _____###________________##
                ______##_______________###
                _______###____________###
                _________####________###
                ___________#########
    """)
    speak('which music?')
    message = 'is this correct sir?'
    messageint = 0
    globals()['sayac'] = 0
    mname = myCommand()
    if "please yourself" in mname:
        speak("all right sir.")
        musiclist = open('confs/musics.txt', "r").readlines()
        mname = random.choice(musiclist)
        message = 'is this ok sir?'
        messageint=1
    elif "let it all hang out" in mname:
        speak("all right sir.")
        musiclist = open('confs/musics.txt', "r").readlines()
        mname = random.choice(musiclist)
        message = 'is this ok sir?'
        messageint = 1
    elif "go for it" in mname:
        speak("all right sir.")
        musiclist = open('confs/musics.txt', "r").readlines()
        mname = random.choice(musiclist)
        message = 'is this ok sir?'
        messageint = 1

    query_string = urllib.parse.urlencode({"search_query": mname})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
    driver.get("http://www.youtube.com/watch?v=" + search_results[sayac])
    globals()['a'] = 1
    while (globals()['a'] == 1):
        speak(message)
        correcting = myCommand()
        if 'yes' in correcting:
            speak('OK Then. Call me when you need sir.')
            globals()['sayac'] = globals()['a'] = 0
        elif 'yeah' in correcting:
            speak('OK Then. Call me when you need sir.')
            globals()['sayac'] = globals()['a'] = 0
        elif 'yep' in correcting:
            speak('OK Then. Call me when you need sir.')
            globals()['sayac'] = globals()['a'] = 0
        elif 'all right' in correcting:
            speak('OK Then. Call me when you need sir.')
            globals()['sayac'] = globals()['a'] = 0
        elif 'absolutely' in correcting:
            speak('OK Then. Call me when you need sir.')
            globals()['sayac'] = globals()['a'] = 0
        elif 'exactly' in correcting:
            speak('OK Then. Call me when you need sir.')
            globals()['sayac'] = globals()['a'] = 0
        elif 'no' in correcting:
            if messageint == 1:
                mname = random.choice(musiclist)
                query_string = urllib.parse.urlencode({"search_query": mname})
                html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
                search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
                driver.get("http://www.youtube.com/watch?v=" + search_results[sayac])
            else:
                globals()['sayac'] =globals()['sayac'] + 1
                driver.get("http://www.youtube.com/watch?v=" + search_results[sayac])
        elif 'change' in correcting:
            music()

if __name__ == '__main__':
    query=""
    speak('All Systems Available')
    print("""
     __________  _________  ________________     
  / ____/ __ \/ ____/   |/_  __/ ____/ __ \    
 / /   / /_/ / __/ / /| | / / / __/ / / / /    
/ /___/ _, _/ /___/ ___ |/ / / /___/ /_/ /     
\____/_/ |_/_____/_/  |_/_/ /_____/_____/      
                                               
       ______  __   
      / __ ) \/ /   
     / __  |\  /    
    / /_/ / / /     
   /_____/ /_/      
                    
         ____  ___  ________  ____  _____    _   __       ____  _____   _______   __
        / __ )/   |/_  __/ / / / / / /   |  / | / /      / __ \/__  /  / ____/ | / /
       / __  / /| | / / / / / / /_/ / /| | /  |/ /      / / / /  / /  / __/ /  |/ / 
      / /_/ / ___ |/ / / /_/ / __  / ___ |/ /|  /      / /_/ /  / /__/ /___/ /|  /  
     /_____/_/  |_/_/  \____/_/ /_/_/  |_/_/ |_/       \____/  /____/_____/_/ |_/   
                                                                                    

    """)
    time.sleep(4)
    print("""
888888888888888888888888888888888
88888888888888888____88888____888
8888888888888888______888_____888
8888888888888888______888_____888
8888888888888888______888_____888
8888888888888888______88_____8888
8888888888888888______88_____8888
8888888888888888______88_____8888
8888888888_____8______88_____8888
8888___88______8______8_____88888
888_____8______8______8_____88888
888_____8______8______8_____88888
888_____8______8______8_____88888
888_____8____88888888888888888888
8_8_____8___88________________888
8_8_____8__88__________________88
8__888888_888_________888_______8
8_________88________8___________8
8____________8888888____________8
88_____________88_______________8
88_______________88_____________8
888______________8_____________88
888_______________8___________888
88888_____________8__________8888
888888_____________________888888
888888____________________8888888

    """)
    time.sleep(2)
    print("""

888888888888888888888888888888888888888888888888
888888888888888888888888888888888888888888888888
888888888888888888888888888888888888888888888888
88888888888888888__________________________88888
88888888888888888__________________________88888
8888888888888____8888888___________________88888
888888888______88____8888888_______________88888
888888_____888888________88888_____________88888
8888____88888____888888____88888___________88888
88____8888____888___88888____8888__________88888
88____888____8888____888____8888___________88888
888____888____888_________8888_____88______88888
8888_____888___88_______8888_____888888____88888
888888____888____888888888_____88888888____88888
8888888_____888888888_______88888888_______88888
8888888888______8______888888888___________88888
8888888888888____8888888888________________88888
88888888888888888__________________________88888
88888888888888888__________________________88888
888888888888888888888888888888888888888888888888
888888888888888888888888888888888888888888888888
888888888888888888888888888888888888888888888888
888888888888888888888888888888888888888888888888
8_______88__8888__8__88______888__8888____888888
8________8___88___8__88__888__88__888__88__88888
8___888__88__88__88__88__8888__8__88__8888__8888
8___888___88____888__88__8888__8__88__8888__8888
8___888___88____888__88__888__88__88________8888
8___888___888__8888__88______888__88__8888__8888
888888888888888888888888888888888888888888888888
888888888888888888888888888888888888888888888888
888888888888888888888888888888888888888888888888
    """)
    time.sleep(2)
    print("""

$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$_$$$$$$$$$$$$$$$$_$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$__$$$$$$$$$$$$$$_$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$_______________$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$___________________$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$____$$$_________$$$____$$$$$$$$$$$$$
$$$$$$$$$$$$$_____$$$_________$$$_____$$$$$$$$$$$$
$$$$$$$$$$$$___________________________$$$$$$$$$$$
$$$$$$$$$$$$___________________________$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$_____$$$____________________________$$$____$$$
$$$$_____$$$____________________________$$______$$
$$$$_____$$$____________________________$$______$$
$$$$_____$$$____________________________$$______$$
$$$$_____$$$____________________________$$______$$
$$$$_____$$$____________________________$$______$$
$$$$_____$$$____________________________$$______$$
$$$$______$$____________________________$$______$$
$$$$_____$$$____________________________$$______$$
$$$$$___$$$$____________________________$$$___$$$$
$$$$$$$$$$$$____________________________$$$$$$$$$$
$$$$$$$$$$$$____________________________$$$$$$$$$$
$$$$$$$$$$$$___________________________$$$$$$$$$$$
$$$$$$$$$$$$$$$$$______$$$$$$_____$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$______$$$$$$_____$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$______$$$$$$_____$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$______$$$$$$_____$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$______$$$$$$_____$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    """) 
    time.sleep(1) 
    print("Listening... To activate Say Anthony")

    while True:
        if(query==""):
            situation=0
            while(situation==0):
                situation = 0
                breakword = bglstn();
                if breakword=='buddy' or breakword==name or breakword=='wake up' :
                    situation=1;
                    speak("yes sir")
                else:
                    situation=0;
        if(situation==1):
            if(query==""):
                query = myCommand();
                query = query.lower()
            if query=='000':
                query=myCommand()
                query=query.lower()
            if name in query:
                speak('I\'m listening ')
            elif "f***"in query:
                print("""
                ░░░░░░░░░░░░░░░▄▄░░░░░░░░░░░
                ░░░░░░░░░░░░░░█░░█░░░░░░░░░░
                ░░░░░░░░░░░░░░█░░█░░░░░░░░░░
                ░░░░░░░░░░░░░░█░░█░░░░░░░░░░
                ░░░░░░░░░░░░░░█░░█░░░░░░░░░░
                ██████▄███▄████░░███▄░░░░░░░
                ▓▓▓▓▓▓█░░░█░░░█░░█░░░███░░░░
                ▓▓▓▓▓▓█░░░█░░░█░░█░░░█░░█░░░
                ▓▓▓▓▓▓█░░░░░░░░░░░░░░█░░█░░░
                ▓▓▓▓▓▓█░░░░░░░░░░░░░░░░█░░░░
                ▓▓▓▓▓▓█░░░░░░░░░░░░░░██░░░░░
                ▓▓▓▓▓▓█████░░░░░░░░░██░░░░░░
                """)
                speak("Sorry sir i don't think i understood!")
            elif "tony stark" in query:
                print("""

____________________$$$$$$$$$$$
__________________$$$$$$$$$$$$$$
_________$$$$$$$$$$$$$$$$$$$$$$$
_____$$$$$$$$$$$$$$$$$$$$$$$$$$$$
____$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
___$$$_$$_$$$$$$$$$$$$$$$$$$$$$$
__$$$$$_$$$$$$$$$$$$$$$$$$$$$$
__$$$_$$_$$$$$$$$$$$$$$$$$_$$$
__$$$_$$_$$$$$$$$___________$$$$
_$$$$$_$$$$$$$$$$$___________$$$
_$$$_$$_$$$$$$$$$$
_$$$_$$_$$$$$$$$$$
_$$$_$$_$$$$$$$$$$$
$_$$$$$$__$$$$$$$$$
$_$$$$$$___$$$$$$$$
_$$$$$$$$$__$$$$$$$
$_$$$$$$$$___$$$$$$
$$_$$$$$$$$___$$$$$
$$$_$$$$$$$$__$$$$$$
_$$$_$$$$$$$$$_$$$$$
$$$$$ __$$$$$$$$_$$$$
$$$$$$$ __$$$$$$$$$__$
$_$_$$$$$__$$$$$$$$$_$$$$
$$$__$$$$$__$$_$$$$$$$_$$$$
$$$$$$_$$__$$$$$$$$$$$$$$$
_$$$$$$$__$$$$$$$$$$$$$$$$
__$$$$$__$$$$$$$$$$$$$$$$$$
$__$$$__$$$$$$$$$$$$$$$$$$$$
$____$$$$$$$$$$$$$$$$$$$$$$$$$
$____$$$$$$$$$$$$$$$$$$$$$$$$$$

                """)
                print("""
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░╔══╗░░░╔══╦╗░░░╔═╦═╗░░░░░░░░░░░╔═╦══╗░░
░╚║║╬═╦╗╚╗╔╣╚╦═╗║║║║╠═╦══╦═╦╦╦╦╗║║║═╦╝░░
░╔║║╣║║║░║║║║║╩╣║║║║║╩╣║║║╬║╔╣║║║║║╔╝░░░
░╚══╩╩═╝░╚╝╚╩╩═╝╚╩═╩╩═╩╩╩╩═╩╝╠╗║╚═╩╝░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░╚═╝░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░╔══╗░░░░░░░╔═╦╗░░░░░╔╗░░░░░░░░░░░░
░░░░░░╚╗╔╬═╦═╦╦╦╗║═╣╚╦═╗╔╦╣╠╗░░░░░░░░░░░
░░░░░░░║║║╬║║║║║║╠═║╔╣╬╚╣╔╣═╣░░░░░░░░░░░
░░░░░░░╚╝╚═╩╩═╬╗║╚═╩═╩══╩╝╚╩╝░░░░░░░░░░░
░░░░░░░░░░░░░░╚═╝░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░╔╗░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░╔╦╗╠╣╔═╗░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░║╔╬╣╠╣╬╠╗╔╦╦╦╦╦╦╦╦╦╗░
░░░░░░░░░░░░░░░░░░░╚╝╚╩╩╣╔╩╝╚╩╩╩╩╩╩╩╩╩╝░
░░░░░░░░░░░░░░░░░░░░░░░░╚╝░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
                """)
                time.sleep(3)
                speak("Rest In Peace Tony. We all miss you a lot!")
            elif "watch movie"in query:
                netflix()
            elif 'open youtube' in query:
                netsurf("https://www.youtube.com")
            elif 'open google' in query:
                netsurf("https://www.youtube.com")
            elif 'open gmail' in query:
                netsurf("https://www.youtube.com")
            elif "what\'s up" in query or 'how are you' in query:
                stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
                speak(random.choice(stMsgs))
            elif 'nothing' in query or 'abort' in query:
                speak("OK Then")
            elif 'hello' in query:
                speak('Hello')
            elif 'bye' in query:
                driver.quit()
                speak('Bye Sir, have a good day.')
                sys.exit()
            elif 'play music' in query:
                music()
            elif 'stop' in query:
                speak("Sorry sir this command is not working for now.")
            elif 'calculate' in query:
                input =query;
                # write your wolframalpha app_id here
                app_id = "Wolframalphaid"
                client = wolframalpha.Client(app_id)

                indx = input.lower().split().index('calculate')
                query = input.split()[indx + 1:]
                res = client.query(' '.join(query))
                answer = next(res.results).text
                speak("The answer is " + answer)
            elif "bored" in query:
                speak("for now , I can suggest you to watching movie , listening music , reading book, playing game , surfing on youtube or listening book sir.")
                correcting=myCommand()
                if "movie" or "first" or "watch" in correcting:
                    query="I want to watch movie"
                elif "listen" in correcting:
                    if "music" in query:
                        query="Play music"
                    if "book" in query:
                        query="Play music"
                elif "game" or "fourth" in correcting:
                    query="Play game"
                elif "youtube" or "fifth" or "surf" in correcting:
                    query="Read me a book"
                query = query.lower
            elif query=="read me a book" or query=="read me book" or query=="read book":
                d=open('books/test.txt',"r").readlines()
                i=0
                while(i<len(d)):
                 speak(d[i])
                 i+=1
            else:
                query = query
                try:
                    try:
                        res = client.query(query)
                        results = next(res.results).text
                        speak(results)

                    except:
                        results = wikipedia.summary(query, sentences=2)
                        speak('Got it.')
                        speak(results)

                except:
                    speak("couldn't find sir")
            query=""
