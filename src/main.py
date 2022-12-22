from distutils.log import debug
import speech_recognition as sr
import pyttsx3

listner = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[10].id)
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
            #if 'annie' in com:
            #    print(com)
    except Exception as expt:
        print(expt)
    return com

def run_annie():
    command = take_commmand()
    print(command)
    if 'play' in command:
        command = command.replace('hey','')
        command = command.replace('arnold', '')
        command = command.replace('play','')
        talk('Playing Now'+command)
        
        

run_annie()