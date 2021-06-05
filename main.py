import pyttsx3
import speech_recognition as sr
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import os
import python_weather
import requests, json
import smtplib

t2sEngine = pyttsx3.init()  # for output(system voice)
recognizer = sr.Recognizer()  # for input


def talk(text):
    t2sEngine.say(text)
    t2sEngine.runAndWait()


def greet():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        talk("Good morning")
    elif hour >= 12 and hour < 17:
        talk("Good Afternoon")
    elif hour >= 16 and hour < 20:
        talk("Good evening")
    talk("I am jarvis what can i do for you")


greet()


def take_command():
    try:
        with sr.Microphone() as source:
            print("listening...")
            recognizer.pause_threshold = 0.8
            voice = recognizer.listen(source)
            command = recognizer.recognize_google(voice)
            command = command.lower()
            print("user said: " + command)
    except Exception:
        return "None"
    return command


def runJarvis():
    while True:
        command = take_command().lower() 

        if "play" in command:
            remove_play = command.replace("play", "")
            talk(f"playing {remove_play} on youtube")
            pywhatkit.playonyt(command)
        elif "date" in command:
            date = datetime.datetime.now().strftime("%d:%b:%Y")
            print(date)
            talk("Today's date is " + date)
        elif "time" in command:
            time = datetime.datetime.now().strftime("%#I :%#M %p")
            print(time)
            talk("The current time is" + time)
        elif "who" in command:
            try:
                remove_who = command.replace("who", "")
                wiki = wikipedia.summary(remove_who, 1)
                print(wiki)
                talk(wiki)
            except Exception:
                print("Sorry information not available in wikipedia")

        elif "day" in command:
            day = datetime.datetime.now().strftime("%A")
            print(day)
            talk("today is" + day)
        elif "joke" in command:
            jokes = pyjokes.get_joke()
            print(jokes)
            talk(jokes)
        elif "assalamu alaikum" in command:
            print("Walaikum salaam warahmathullaahi wabarakathuhu")
            talk("Walaikum salaam warahmathullaahi wabarakathuhu")
        elif "how are you" in command:
            print("Alhamdullilah i am pretty good")
            talk("Alhamdullillah i am pretty good")
        elif "hai" in command:
            print("Hello there")
            talk("Hello there")
        elif "open chrome" in command:
            talk("opening chrome")
            webbrowser.open("chrome")
        elif ("open pictures" in command) or ("open photos" in command):
            print("opening pictures")
            talk("opening pictures..")
            pic_dir = "C:\\Users\\Public\\Pictures"
            os.startfile(pic_dir)
        elif "open gmail" in command:
            print("opening gmail..")
            talk("opening gmail")
            webbrowser.open("https://www.google.com/gmail/")
        elif "open youtube" in command:
            print("opening youtube")
            talk("opening youtube")
            webbrowser.open("https://youtube.com/")
        elif "open vs code" in command:
            print("opening visual studio code..")
            talk("opening visual studio code")
            camera_path = "C:\\Users\\Irshathl\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(camera_path)
        elif "can i hear a song" in command:
            music_dir = "D:\\songs"
            talk("playing song")
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif "search" in command:
            remove_search = command.replace("search", "")
            talk("searching" + remove_search)
            pywhatkit.search(remove_search)
        elif "shutdown" in command:
            print(
                "Windows is shutting down if you want to stop shutdown give the command cancel shutdown"
            )
            talk("Windows is shutting down")
            pywhatkit.shutdown(20)
        elif "open notepad" in command:
            talk("opening notepad")
            os.system("Notepad")
        elif ("open word" in command) or ("open ms word" in command):
            talk("opening microsoft word")
            os.startfile(
                "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            )
        elif ("open excel" in command) or ("open ms excel" in command):
            talk("opening microsoft excel")
            os.startfile(
                "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
            )
        elif ("open excel" in command) or ("open ms excel" in command):
            talk("opening microsoft excel")
            os.startfile(
                "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
            )
        elif "what is the weather in" in command:
            location = command.replace("what is the weather in", "")
            # api key from openweathermap
            api_key = "b588879f1c8b5e59813816bf8ee9e788"
            # base_url variable to store url
            base_url = "http://api.openweathermap.org/data/2.5/weather?"
            city_name = location
            # complete url address
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            # return response object
            response = requests.get(complete_url)
            # json method of response object
            # convert json format data into
            # python format data
            x = response.json()
            # Now x contains list of nested dictionaries
            # Check the value of "cod" key is equal to
            # "404", means city is found otherwise,
            # city is not found
            if x["cod"] != "404":

                # store the value of "main"
                # key in variable y
                y = x["main"]

                # store the value corresponding
                # to the "temp" key of y
                current_temperature = y["temp"]

                # print following values
                print(
                    f"Weather in {location} is {str(int(current_temperature - 273.15))}C"
                )
                talk(
                    f"Weather in {location} is {str(int(current_temperature - 273.15))}degree Celsius"
                )
        elif "email" in command:

            talk("Enter the receiver's email id")
            receiver = input("Enter receiver email id: ")
            talk("speak the message you want to send")
            print("SPEAK THE MESSAGE...")
            # creates SMTP session
            s = smtplib.SMTP("smtp.gmail.com", 587)

            # start TLS for security
            s.starttls()

            # Authentication
            s.login("hello@gmail.com", "password1234")
            # message to be sent
            # message send through command
            # sending the mail
            content = take_command()
            filterCommand = content.replace("send email", "")
            s.sendmail("irshath700@gmail.com", receiver, filterCommand)

            # terminating the session
            s.quit()
            print("Email sent successfully")
            talk("your email is sent successfully")
        elif ("stop" in command) or ("bye" in command):
            talk("Okay bye have a good day")
            break
        elif "what is your name" in command:
            talk("I am jarvis  your voice assistant")
        else:
            print("Please say that again")


runJarvis()