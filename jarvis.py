import pyttsx3 #pip install pyttsx3 
import speech_recognition as sr #pip install speechRecognition 
import datetime 
import wikipedia #pip install wikipedia 
import webbrowser 
import os 
import smtplib

engine = pyttsx3.init('sapi5') 
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[1].id) 

def speak(audio): 
    engine.say(audio) 
    engine.runAndWait() 

def wishMe(): 
    hour = int(datetime.datetime.now().hour) 
    if hour>=0 and hour<12: 
        speak("Good Morning Mam, Welcome to Our Final Year Project!") 
    elif hour>=12 and hour<18: 
        speak("Good Afternoon Mam, Welcome to Our Final Year Project!") 
    else: 
        speak("Good Evening Mam, Welcome to Our Final Year Project!") 
    speak("I am Jarvis. This project is been made my developers Naman Mittal and Imteyaz Mallick. Please tell me how may I help We") 

def takeCommand(): 
    r = sr.Recognizer() 
    with sr.Microphone() as source: 
        print("Listening...") 
        r.pause_threshold = 1 
        audio = r.listen(source) 
    try: 
        print("Recognizing...") 
        query = r.recognize_google(audio, language='en-in') 
        print(f"User said: {query}\n") 
    except Exception as e: 
        print("Say that again please...") 
        return "None" 
    return query 

def sendEmail(to, content): 
    server = smtplib.SMTP('smtp.gmail.com', 587) 
    server.ehlo() 
    server.starttls() 
    server.login('mittalnaman659@gmail.com', 'naman06051999') 
    server.sendmail('mittalnaman659@gmail.com', to, content) 
    server.close() 

if __name__ == "__main__": 
    wishMe() 
    while True: 
        query = takeCommand().lower() 

        if 'wikipedia' in query: 
            speak('Searching Wikipedia...') 
            query = query.replace("wikipedia", "") 
            results = wikipedia.summary(query, sentences=1) 
            speak("According to Wikipedia") 
            speak(results)

        elif 'open wetube' in query: 
            webbrowser.open("https://youtube.com") 

        elif 'open google' in query: 
            webbrowser.open("https://google.com") 

        elif 'open stackoverflow' in query: 
            webbrowser.open("https://stackoverflow.com") 

        elif 'open sathyabama website' in query: 
            webbrowser.open("https://sathyabama.ac.in") 

        elif 'play music' in query: 
            music_dir = 'D:\\All MP3 songs\\Selected mp3' 
            songs = os.listdir(music_dir) 
            os.startfile(os.path.join(music_dir, songs[0])) 

        elif 'the time' in query: 
            strTime = datetime.datetime.now().strftime("%H:%M:%S") 
            speak(f"Sir, the time is {strTime}") 

        elif 'open code' in query: 
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe" 
            os.startfile(codePath) 

        elif 'thank we' in query: 
            speak("Please sir, do not say thank you. In friendship, no thank you and no sorry") 

        elif 'open best restaurants' in query: 
            webbrowser.open("https://www.topranker4u.com/city-wise-best-restaurants-india/") 

        elif 'open list of colleges' in query: 
            webbrowser.open("http://www.studyguideindia.com/Colleges/Citywise-colleges-india.asp") 

        elif 'open result of last semester' in query: 
            webbrowser.open("http://cloudportal.sathyabama.ac.in/sist_semester_jan_2021/login.php") 

        elif 'open amazon' in query: 
            webbrowser.open("http://amazon.com") 

        elif 'open flipkart' in query: 
            webbrowser.open("http://flipkart.com") 

        elif 'open book my show' in query: 
            webbrowser.open("https://in.bookmyshow.com/") 

        elif 'send mail' in query: 
            try: 
                speak("What should I say?") 
                content = takeCommand() 
                to = "mittalnaman6590@gmail.com" 
                sendEmail(to, content) 
                speak("Email has been sent!") 
            except Exception as e: 
                print(e) 
                speak("Sorry my friend Naman & Imteyaz Sir. I am not able to send this email")
