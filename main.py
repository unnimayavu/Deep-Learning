import speech_recognition as sr 
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener=sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening....')
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()
            if 'nova' in command:
                command=command.replace('nova','')
                print(command)
    except:
        pass
    return command

def run_nova():
    command=take_command()
    #print(command)
    if 'play' in command:
        song=command.replace('play','')
        talk('Playing'+song)
        pywhatkit.playonyt('song')    
    elif 'time' in command:
        time=datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is '+ time)
        print(time)
    elif 'joke' in command:
        jokes=pyjokes.get_joke()
        talk('Here is a joke for you')
        talk(jokes)
        print(jokes)
    elif 'i love you' in command:
        talk('that is so sweet i dont have the feelings for the humans')     
    elif 'are you single' in command:
        rel='i am in a relationship with wifi ha ha ha'
        talk(rel)
    elif 'who' or 'what' in command:
        person=command.replace('who','')
        info=wikipedia.summary(person,1)
        print(info)
        talk(info)
    else:
        sorry_msg='Sorry Please explain it again'
        talk(sorry_msg)
        

while True:    
    run_nova()
        