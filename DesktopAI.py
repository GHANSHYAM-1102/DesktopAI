import pyttsx3  # to fetch ai voice
import speech_recognition

engine = pyttsx3.init("sapi5") # voice from microsoft
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)  #voice rate 

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()  #speech recognization
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1   # take 1 second break
        r.energy_threshold = 300 # human voice frequncy.
        audio = r.listen(source,0,4)

    try:
        print("Understanding.....")
        query  = r.recognize_google(audio,language='en-in')  #change language into english 
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

# ---------------------------main methos are starting here----------------------------
if __name__ == "__main__":
    while True:
        query = takeCommand().lower() 
        if "wake up" in query:   # start code here 
            from GreetMe import greetMe  #say good morning and etc as per time 
            greetMe()

            while True:
                query = takeCommand().lower() 
                if "go to sleep" in query: 
                    speak("Ok sir , You can me call anytime")
                    break
                elif "hello" in query:
                    speak("Hello sir, how are you ?")
                elif "i am fine" in query:
                    speak("that's great, sir")
                elif "how are you" in query:
                    speak("Perfect, sir")
                elif "thank you" in query:
                    speak("you are welcome, sir")
                elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)
                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)
                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)
                elif "using ai" in query:
                    from OpenAiAssitant import ai
                    ai(query)
                elif "finally sleep" in query:
                    speak("Going to sleep,sir")
                    exit()