import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import pywhatkit
import os 
import pyautogui
import pyjokes
from PyDictionary import PyDictionary 
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    time = int(datetime.datetime.now().hour)
    if(time>=0 and time<12):
        speak("Good Morning")
    elif(time>12 and time<=16):
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am your personal assitant. You can call me Joy.")

def speak_date():
    current_date = datetime.date.today()
    current_day = str(current_date.day)
    current_month = str(current_date.month)
    current_year = str(current_date.year)
    if current_month == '1':
        current_month = "January"
    elif current_month == '2':
        current_month = "February"
    elif current_month == '3':
        current_month = "March"
    elif current_month == '4':
        current_month = "April"
    elif current_month == '5':
        current_month = "May"
    elif current_month == '6':
        current_month = "June"
    elif current_month == '7':
        current_month = "July"
    elif current_month == '8':
        current_month = "August"
    elif current_month == '9':
        current_month = "September"
    elif current_month == '10':
        current_month = "October"
    elif current_month == '11':
        current_month = "November"
    elif current_month == '12':
        current_month = "December"
    speak(f" Today is {current_day} {current_month} {current_year}. How may i help you?")

def takeCommand():
    #It takes microphone input from the user and returns string output.
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("You are ready to speak....")
            r.pause_threshold = 2
            r.energy_threshold = 200
            audio = r.listen(source)
    
        try:
            print("Recognising...please wait for a while...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except Exception as e:
            print(f"Ooops!!there is an error- {e}")
            print("Please speak it again... ")
        return query

def yes_or_no():
    #It takes microphone input from the user and returns string output.
    l = sr.Recognizer()
    with sr.Microphone() as source:
        print("Yes or no??")
        l.pause_threshold = 2
        l.energy_threshold = 200
        audio = l.listen(source)
    
    try:
        print("Recognising...please wait for a while...")
        decision = l.recognize_google(audio, language='en-in')
        print(f"User said: {decision}\n")
    except Exception as e:
        print(f"Ooops!!there is an error- {e}")
        print("Please speak it again... ")
    finally: 
        return decision


def sendEmail(to , msg):
    speak("Do you want to send email from a particular email address? If yes speak yes otherwise speak No")
    dec = takeCommand().lower()
    if dec == 'no':
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('voidme46@gmail.com','MeVoid@2056')
        server.sendmail('voidme46@gmail.com' , to , msg)
        server.close()
    if dec == 'yes':
        speak("Enter the email address and password")
        mail = input("Enter the email- ")
        password = input("Enter the password- ")
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(mail , password)
        server.sendmail(mail , to , msg)
        server.close()


def OpenApps():

    if 'instagram' in query:
        webbrowser.open(r'https://www.instagram.com/')

    elif 'facebook' in query:
        webbrowser.open(r'https://www.facebook.com/')

    elif 'whatsapp' in query:
        webbrowser.open(r'https://www.whatsapp.com/')

    elif 'whatsapp web' in query:
        webbrowser.open(r'https://web.whatsapp.com/')

    elif 'google play store' in query:
        webbrowser.open(r'https://play.google.com/store')

    elif "open visual studio code" in query:
        path = "C:\\Users\\Sai\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(path)

    elif 'dev c plus plus' in query:
        path = "C:\\Program Files (x86)\\Dev-Cpp\\devcpp.exe"
        os.startfile(path)

    elif 'firefox' in query:
        path = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
        os.startfile(path)

    elif 'google chrome' in query:
        path = "C:\\Users\\Sai\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe"
        os.startfile(path)

    elif 'microsoft teams' in query:
        path = 'C:\\Users\\Sai\\AppData\\Local\\Microsoft\\Teams\\Update.exe --processStart "Teams.exe"'
        os.startfile(path)

    elif 'turbo c plus plus' in query:
        path = "C:\\TURBOC3\\Turbo C++\\Turbo C++.exe"
        os.startfile(path)

    speak("Done!!")
         
if __name__ == "__main__":  
    wish()
    speak_date()
    t = True
    while t==True: 
        query = takeCommand()
        query = query.lower()
        if "wikipedia" in query:
            speak("Do you want to load a whole page, if yes the speak yes otherwise speak no!!")
            _decision = yes_or_no().lower()
            if _decision == "yes":
                speak("Searching wikipedia...")
                query = query.replace("wikipedia" , "")
                wikipedia.set_lang("en")    
                print(wikipedia.page(query).content)  
                
            elif _decision == "no":
                speak("Searching wikipedia...")
                query = query.replace("wikipedia" , "")
                wikipedia.set_lang("en")
                results = wikipedia.summary(query, sentences=2)
                speak("According to wikipedia")
                print(results)
                speak(results)

        elif 'youtube' in query:
            if "joy" in query:
                query = query.replace("joy" , " ")
            if "search" in query:
                query = query.replace("search" , " ")
            if "in youtube" in query:
                query = query.replace("in youtube" , " ")
            web = "https://www.youtube.com/results?search_query=" + query
            speak("Done!! This is what i found.")
            webbrowser.open(web)

        elif ("search in google" or "from google") in query:
            if 'search' in query:
                query = query.replace('search' , ' ')  
                if 'in google' in query:
                    query = query.replace('in google' , ' ')   
                    if 'joy' in query:
                        query = query.replace('joy' , ' ')   
                elif 'from google' in query:
                    query = query.replace('from google' , ' ')
                    if 'joy' in query:
                        query = query.replace('joy' , ' ')   

            pywhatkit.search(query)
            speak("Done!! This is what i found.")

        elif "play music" in query:
            music_dir = 'D:\\Fav Music'
            songs = os.listdir(music_dir)
            speak("Which song you want to play??")
            fav_song = takeCommand().lower()
            pywhatkit.playonyt(fav_song)

        elif 'screenshot' in query:
            snap = pyautogui.screenshot()  
            ss = 'yes'
            i = 1
            while ss=='yes':
                snap.save(f'E:\Screenshots\Screenshot{i}.png')
                speak("Screenshot Taken!!")
                speak("Do you want to take more screen shots?")
                ss = takeCommand()
                if ss == 'yes':
                    i = i+1
                    snap.save(f'E:\Screenshots\Screenshot{i}.png')
                elif ss == 'no':
                    break

        elif 'open instagram' in query:
            OpenApps()

        elif 'open facebook' in query:
            OpenApps()

        elif 'open google play store' in query:
            OpenApps()

        elif 'open whatsapp' in query:
            OpenApps()

        elif 'open whatsapp web' in query:
            OpenApps()

        elif 'open firefox' in query:
            OpenApps()

        elif 'open google chrome' in query:
            OpenApps()

        elif 'open microsoft teams' in query:
            OpenApps()

        elif 'open turbo c plus plus' in query:
            OpenApps()

        elif 'open dev c plus plus' in query:
            OpenApps()

        elif "open visual studio code" in query:
            OpenApps()

        elif 'joke' in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif 'meaning of' in query:
            if 'what is the meaning of' in query:
                query = query.replace('what is the meaning of',' ')
                if 'joy' in query:
                   query = query.replace('joy',' ') 
            elif 'tell me the meaning of' in query:
                query = query.replace('tell me the meaning of',' ')
                if 'joy' in query:
                   query = query.replace('joy',' ') 

            meaning = PyDictionary(query)
            print(meaning.getMeanings())
            speak(meaning.getMeanings())

        elif "time" in query:
                timing = datetime.datetime.now().strftime("%H : %M")
                speak(f"The time is {timing}")

        elif "send email" in query:
                try:
                    speak("What do you want to send as message??")
                    msg = takeCommand()
                    speak("Type the email address to which the address has to be sent")
                    to = input("Type the email address to which the address has to be sent- ")
                    sendEmail(to , msg)
                    speak("Email has been sent!!")
                except Exception as ex:
                    print(ex)
                    speak("Sorry!!I am not able to send email.")

        speak("Do you want more tasks to be performed?? If yes, speak yes otherwise speak no.")
        decide = takeCommand().lower()
        if decide=="yes":
            t = True
        elif decide=="no":
            t = False
            break


            

        



    
            
            

