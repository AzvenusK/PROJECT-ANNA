import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
from distutils.log import debug
from googlesearch import search

listner = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', 'english_rp+f4')

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_commmand():       
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listner.listen(source)
            com = listner.recognize_google(voice)   
            com = com.lower()
    except Exception as expt:
        print(expt)
    return com

def run_annie():
    com = take_commmand()
    if 'annie' in com:
        print(com)
        talk('Yeah how can I help?')
        command = take_commmand()
        if 'play' in command:
            command = command.replace('play','')
            talk('Playing Now'+command)
            pywhatkit.playonyt(command)
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Right now it is'+time)
        elif 'wiki' or 'wikipedia' or 'info' or 'information' or 'tell me about' or 'who is' in command:
            if 'of' in command:
                command[command.find('of'):]
                command = command.replace('of','')
            elif 'on' in command:
                command[command.find('on'):]
                command = command.replace('on','')
            elif 'about' in command:
                command[command.find('about'):]
                command = command.replace('about','')
            elif 'who is' in command:
                command[command.find('is'):]
                command = command.replace('is','')
            print(command)
            info = wikipedia.summary(command, 2)
            print(info)
            talk(info)
            
        else:
            talk('Here is what I found on the internet')
            for searchresults in search(command, tld="co.uk", num = 10, stop = 10, pause = 2):
                print(searchresults)
    else:
        exit

run_annie()
