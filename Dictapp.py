import os   # operating system
import pyautogui  
import webbrowser  # to open webbrowser 
import pyttsx3    # fetch ai voice
from time import sleep

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 200)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# this is dictionary to say ai what you want to open in your system with key and value

dictapp = {"commandprompt": "cmd", "paint": "paint", "word": "winword", "excel": "excel", "chrome": "chrome",  
           "vscode": "code", "powerpoint": "powerpnt","microsoftedge": "msedge", "netflix": "netflix.exe", "spotify": "spotify.exe"}


#for open webbrowser

def openappweb(query):
    speak("Launching, sir")  
    if ".com" in query or ".co.in" in query or ".org" in query:   #say .com and .in etc when you are say ai to open any webpage
        query = query.replace("open", "")
        query = query.replace("jarvis", "")
        query = query.replace("launch", "")
        query = query.replace(" ", "")
        webbrowser.open(f"https://www.{query}")  #add your query or say question here in (query)
    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                try:
                    os.system(f"start {dictapp[app]}") #start your query
                except Exception as e:
                    os.system(f"open {dictapp[app]}")  #else open any page 


#you want to close any page then you need to say below line to ai

def closeappweb(query):  
    speak("Closing,sir")
    if "one tab" in query or "1 tab" in query:
        pyautogui.hotkey("ctrl", "w")
        speak("All tabs closed")
    elif "2 tab" or "to tab" in query:
        pyautogui.hotkey("ctrl", "w")   # hotkey is a key to close any page this is a inbuilt method in python
        sleep(0.5)                      #take  sleep 0.5 second  after listening to close page
        pyautogui.hotkey("ctrl", "w")
        speak("All tabs closed")
    elif "3 tab" in query:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        speak("All tabs closed")

    elif "4 tab" in query:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        speak("All tabs closed")
    elif "5 tab" in query:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        speak("All tabs closed")

    else:                      
        keys = list(dictapp.keys())     
        for app in keys:        
            if app in query:                     
                os.system(f"taskkill /f /im {dictapp[app]}.exe")    # direclty close this tab with using of keys