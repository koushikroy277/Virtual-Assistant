from __future__ import print_function
import datetime, pickle, os.path, pyttsx3
import os, time, webbrowser, pytz, wikipedia
from selenium import webdriver
import speech_recognition as sr
from gtts import gTTS
from selenium.webdriver.common.keys import Keys


def speak(audio):
    engine = pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")

        r.pause_threshold = 1
        audio = r.listen(source)
        text = ""

        try:

            print('Recognizing...')
            text = r.recognize_google(audio)
            print(f"SIR YOU SAID {text}")

        except Exception as e:
            print(e)
            speak("Please, say that again, sir")
            print("Please, repeat your command, Sir...")
            return "None"

    return text

def WishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("Hi, I'm your virtual assistant. How can I help you, sir")


if __name__ == "__main__":
    WishMe()

    while True:
        # Taking the commands and giving output

        text = take_command().lower()

        if "hello" in text:
            speak("Hello sir, how are you?")
        elif "what's your name" in text:
            speak("My name is Alva")
        elif "what do you do" in text:
            speak("I follow your order")
        elif "how to get a girlfriend" in text:
            speak("If your personality is charming then you can easily get a girlfriend and I know you very well. Every girl would be dying for you")

        elif "what about you" in text:
            speak("I am fine as always")

        elif "what do you think of myself" in text:
            speak("You are a good guy but sometimes you lose your cool. You are talented but need to be more patient and more persistent")

        elif "thank you" in text:
            speak("You're most welcome")

        if 'wikipedia' in text:
            speak('Searching wikipedia')
            text = text.replace('wikipedia', "")
            results = wikipedia.summary(text, sentences = 4)
            speak('According to your command...')
            print(results)
            speak(results)

        elif "open youtube find" in text:
            browser = webdriver.Chrome("/Users/mac/Downloads/chromedriver")
            browser.get("https://www.youtube.com/")
            find = browser.find_element_by_name("search_query")
            text = text.replace('open youtube find', "")
            find.send_keys(text)
            find.send_keys(Keys.RETURN)

            time.sleep(5)

        elif "open google find" in text:
            browser = webdriver.Chrome("/Users/mac/Downloads/chromedriver")
            browser.get("https://www.google.com/")
            find = browser.find_element_by_name("q")
            text = text.replace('open google find', "")
            find.send_keys(text)
            find.send_keys(Keys.RETURN)

            time.sleep(5)

        elif "open facebook" in text:
            webbrowser.open("https://www.facebook.com/")

        elif "search" in text:
            speak('Searching....')

            browser = webdriver.Chrome("/Users/mac/Downloads/chromedriver")
            browser.get("https://techwithtim.net/#google_vignette")
            find = browser.find_element_by_name("s")
            text = text.replace('search', "")
            find.send_keys(text)
            find.send_keys(Keys.RETURN)

            time.sleep(5)


        elif "quit" in text:
            speak("quitting the system")
            exit()

        elif "time" in text:
            DATE = datetime.datetime.today()
            index = DATE.time()
            print(index)

        elif "date" in text:
            DATE = datetime.datetime.today()
            index = DATE.date()
            print(index)
