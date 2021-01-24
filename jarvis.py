import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import psutil       # For Checking Battery life of System
import json         # For Getting news API
import requests
from urllib.request import urlopen
import time as sleep_time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

print(voices[0])
engine.setProperty('voice',voices[0].id)
# engine.setProperty('rate',150)

def wish_me():
    time = datetime.datetime.now()      # It Gives you Date and Time in Format YYYY-MM-DD Hr-Min-Sec.MicroSec
    hour = time.strftime('%H:%M:%S')    # %H for 24Hr (after 12-13,14) and %I for 12Hr(after 12-1,2) 

    if int(hour[:2]) >=0 and int(hour[:2])<12:
        speak("Good Morning Mr.Safe")

    elif int(hour[:2]) >=12 and int(hour[:2])<17:
        speak("Good Afternoon Mr.Safe")

    else :
        speak("Good Evening Mr.Safe")

    speak('Jarvis at your Service Sir, Please tell me how can I help You!!')

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def take_command():
    # The Function will allow Jarvis to take input from Microphone from user and returns a string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        # r.energy_threshold = 400
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language = 'en-in')
        print(f'User said: {query}')
    
    except Exception as e:
        print(e)
        print("Say that again plzz")
        return "None"
    return query


if __name__ == '__main__':
    wish_me()
    while True:
        command = take_command().lower()

        if 'wikipedia' in command:
            try: 
                speak("Searching on Wikipedia")
                command = command.split('search')
                command = str(command[1])
                command = command.replace("wikipedia","")
                print(command)
                result = wikipedia.summary(command,sentences=2)
                speak("According to Wikipedia..")
                print(result)
                speak(result)
            
            except Exception as e:
                speak("Say that again please")

        elif 'open google' in command:
            google_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(google_path)
        
        elif 'open youtube' in command:
            webbrowser.open('youtube.com')

        elif 'mail' in command:
            speak('Yes Sir, You have got mails')
            webbrowser.open('https://mail.google.com/mail/u/0/#inbox')

        elif 'search' and 'on youtube' in command:
            try:
                command = command.split('search')
                command = str(command[1])
                command = command.replace("youtube","")
                # print(type(command))
                speak("Okay Sir Searching......")
                webbrowser.open('https://www.youtube.com/results?search_query='+command)
            except Exception as e:
                print(e)
                speak("Say that again please...")

        elif 'search' and 'on google' in command: 
            try:
                command = command.split('search')
                command = str(command[1])
                command = command.replace("google","")
                speak("Okay Sir Searching......")
                webbrowser.open_new_tab('https://www.google.com/search?q='+command)
            
            except Exception as e:
                print(e)
                speak("Say that again please")

        elif 'who are you' in command:
            speak('Hello, I am JARVIS (Just A Rather Very Intelligent System), designed by Mr.Safe. I am a program. I am of without Form. I am able to Interact with human beings just as a living person')
            speak('I am Inspired by Mr.Stark Natural-language User Interface Computer System, Edwin Jarvis')
            # speak("I can control your System. I can open Google, Youtube . I can search anything for you on Wikipedia, Google, Youtube. I can tell you the latest news. I can also tell you time and date. I can tell you your system battery life. I can also Restart and Shutdown Your System. And If you want me to stop just tell me JARVIS Quit.")
            speak('I am always there for you Sir, Please tell me how may I help you!!')
            
            print("Hello, I am JARVIS (Just A Rather Very Intelligent System), designed by Mr.Safe. I am a program.")
            print("I can control your System.\nI can open Google, Youtube.\nI can search anything for you on Wikipedia, Google, Youtube.\nI can Check your mails.\nI can tell you the latest news. I can also tell you time and date.\nI can tell you your system battery life. I can also Restart and Shutdown Your System.\nAnd If you want me to stop just tell me JARVIS Quit.")
 
        elif 'play' and 'music' in command:
            music_dir = 'E:\\Songs'
            songs = os.listdir(music_dir)       # It Will list all songs in the directory
            pick_song = random.randint(1,60)
            print(pick_song)
            speak('Engoy the music Sir')
            os.startfile(os.path.join(music_dir,songs[pick_song]))      # It is used to start the file and it recieves the path as an argument (viz is music_path and random song picked in that dir)

        elif 'the time' in command:
            time = datetime.datetime.now().strftime('%I:%M:%S')
            time_speak = time[:2] + ' o clock '+ time[2:5] +' minute  and' + time[5:]+' second'
            print(time_speak)   
            speak(f"The time is {time_speak}")

        elif 'the date' in command:
            date = datetime.date.today()
            speak(date)

        elif 'open vs code' in command:
            code_path = "C:\\Users\\Saif\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            speak("Opening Visual Studio Code")
            os.startfile(code_path)


        elif 'news' in command :
            try:
                jsonObj = urlopen('http://newsapi.org/v2/top-headlines?country=in&apiKey=111e79bcc5ac460688ce02a134bcdf68')
                data = json.load(jsonObj)
                i=1

                speak("Here are some Top Headlines")
                print("-------------------------------TOP HEADLINES-------------------------")
                for item in data['articles'][:10]:
                    print(str(i)+'. '+item['title']+'\n')
                    print(item['description']+'\n')
                    speak(item['title'])
                    speak(item['description'])
                    i+=1

            except Exception as e:
                print(e)
                speak("Sorry Sir, Not found any data please try again")

        elif 'battery' in command:
            battery = psutil.sensors_battery()          # For Checking Battery of the System
            print(battery)
            speak(f"Battery is at {battery.percent} percent")
        
        elif 'logout' in command :
            os.system("shutdown 1")

        elif 'shutdown' and 'system' in command:
            speak("Ok Sir, System Shutting down, Good Bye, Have a Nice Day!!")
            os.system("shutdown /s /t 1")

        elif 'restart the system' in command:
            speak("Ok Sir, System Restarting, Good Bye, Have a Nice Day!!")
            os.system("shutdown /r /t 1")

        elif 'quit' in command:
            speak("Ok Sir, Thank You For your Time , Good Bye, Have a Nice Day!!")
            speak("Jarvis Quit")
            quit() 