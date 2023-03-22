import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia #pip install wikipedia
import pyaudio
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5') #to use inbilt voices

voices= engine.getProperty('voices') #getting details of current voice

engine.setProperty('voice', voices[1].id) #helps us to select different voices

#We use speak() function to convert our text to speech.
def speak(audio):
    engine.say(audio)
    engine.runAndWait() #Without this command, speech will not be audible to us.

# Now, we will make a wishme() function that will make our Alisha. 
# Wish or greet the user according to the time of computer or pc. 
# To provide current or live time to A.I., we need to import a module called datetime

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Alisha Sir or Mam . Please tell me how may I help you")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer() #help us to recognize the voice
    with sr.Microphone() as source: # We will use this as source moicrophone
        print("Listening...")
        r.pause_threshold = 1 #seconds of non-speaking audio before a phrase is considered as complete  
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query

if __name__=="__main__" :
    speak("Hi Mam or sir , hope you are doing great") #Whatever we will write inside this speak() function will be converted into speech
    wishme()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif 'Alisha open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'Alisha open google' in query:
            webbrowser.open("google.com")

        elif 'Alisha open gfg website' in query:
             webbrowser.open("www.geeksforgeeks.org")

        elif 'Alisha open microsoft' in query:
            webbrowser.open("www.microsoft.com") 
        
        elif 'play music' in query:
            webbrowser.open("music.youtube.com")