import speech_recognition as sr 
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()
    
def introduction():
    talk('Hey I am your virtual assistant Nova, how can I help you?')
introduction()

def stop_nova():
    print("Goodbye..")
    talk("Goodbye")
    raise SystemExit

def take_command():
    command = ""
    try:
        with sr.Microphone() as source:
            print('Listening....')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'nova' in command:
                command = command.replace('nova', '')
                print(command)
    except sr.UnknownValueError:
        pass
    except sr.RequestError:
        print("Sorry, I could not request results from Google Speech Recognition service")
    return command

def run_nova():
    command = take_command()
    print(command)
    if command:
        # Check for stop or bye command first
        if 'stop' in command or 'bye' in command:
            stop_nova()
        elif 'play' in command:
            song = command.replace('play', '')
            talk('Playing ' + song)
            pywhatkit.playonyt(song)    
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is ' + time)
            print(time)
        elif 'joke' in command:
            jokes = pyjokes.get_joke()
            talk('Here is a joke for you')
            talk(jokes)
            print(jokes)
        elif 'i love you' in command:
            talk('That is so sweet, but I don’t have feelings for humans.')     
        elif 'are you single' in command:
            rel = 'I am in a relationship with Wi-Fi, ha ha ha'
            talk(rel)
        elif 'who' in command or 'what' in command:
            person = command.replace('who', '').replace('what', '')
            info = wikipedia.summary(person, 1)
            print(info)
            talk(info)
        else:
            sorry_msg = 'Sorry, please explain it again.'
            print(sorry_msg)
            talk(sorry_msg)
    else:
        print("No command received.")

while True:
    run_nova()
