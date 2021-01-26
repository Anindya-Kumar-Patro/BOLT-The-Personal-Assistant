import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = sr.Recognizer()
bolt = pyttsx3.init()
voices = bolt.getProperty('voices')
bolt.setProperty('voice',voices[1].id)

def talk(text):
    bolt.say(text)
    bolt.runAndWait()

def command_recieved():
    try:
        with sr.Microphone() as source:
            print("Speak Boss")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "bolt" in command:
                command = command.replace('bolte','')
                command = command.replace('bolt','')
                
                
    except:
        print("Please Speak again BOSS")
    return command

def bolt_msg():
    command = command_recieved()
    print(command)
    if 'play' in command:
        song = command.replace('play','')
        talk('playing'+song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk(time)
    elif 'search' in command:
        searching = command.replace('search','')
        info = wikipedia.summary(searching,2)
        talk('Searching' + searching + 'for you')
        talk('We got the result boss')
        talk('It is'+info)


bolt_msg()