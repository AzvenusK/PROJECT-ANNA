from distutils.log import debug
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime

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
            command = command.replace('hey','')
            command = command.replace('annie', '')
            command = command.replace('play','')
            talk('Playing Now'+command)
            pywhatkit.playonyt(command)
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Right now it is'+time)
    else:
        exit

run_annie()
