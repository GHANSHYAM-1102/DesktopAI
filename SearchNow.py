import speech_recognition     #to fetchh the speech of ai 
import pyttsx3                # to fetch ai voice in our system
import pywhatkit              #for youtube videos and url in our system
import wikipedia             # to ope wikipedia
import webbrowser            # to open wbbrowser

def takeCommand():           
    r = speech_recognition.Recognizer()   
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1     # take time  1 second 
        r.energy_threshold = 300  # human specking frequancy normal
        audio = r.listen(source,0,4)
    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')  # convert ai language into english 
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query     # return your question

query = takeCommand().lower()  

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#for google search

def searchGoogle(query):
    if "google" in query:
        import wikipedia as googleScrap
        query = query.replace("jarvis","")
        query = query.replace("google search","")
        query = query.replace("google","")
        speak("This is what I found on google")

        try:
            pywhatkit.search(query)               # search your query in  
            result = googleScrap.summary(query,1)
            speak(result)

        except:
            speak("No speakable output available")

# for youtube search
def searchYoutube(query):
    if "youtube" in query:
        speak("This is what I found for your search!")
        query = query.replace("youtube search","")
        query = query.replace("youtube","")
        query = query.replace("jarvis","")
        web  = "https://www.youtube.com/results?search_query=" + query  #pass youtube link and add your question and add with this link
        webbrowser.open(web)
        pywhatkit.playonyt(query)  #play your video or etc
        speak("Done, Sir")

# for search wikipedia

def searchWikipedia(query):
    if "wikipedia" in query:
        speak("Searching from wikipedia....")
        query = query.replace("wikipedia","")
        query = query.replace("search wikipedia","")
        query = query.replace("jarvis","")
        results = wikipedia.summary(query,sentences = 2)  #only read 2 line in your search paragraph
        speak("According to wikipedia..")
        print(results)
        speak(results)