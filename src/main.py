from distutils.log import debug
import speech_recognition as sr

listner = sr.Recognizer()
try:
    with sr.Microphone() as source:
        print('Listening...')
        voice = listner.listen(source)
        com = listner.recognize_google(voice)
        print(com)
except Exception as expt:
    print(expt)