import pyttsx3 # to fetch ai voice in our system
import datetime # for date and time 

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id) #voice starting with 0
engine.setProperty("rate",200)   #voice frequancy(rate)

def speak(audio): 
    engine.say(audio)
    engine.runAndWait() #take 1 second rest or say wait  (if when you are talking with ai)

def greetMe():  
    hour  = int(datetime.datetime.now().hour) #time releted work
    if hour>=0 and hour<=12:   #hour should be  1 to 12 
        speak("Good Morning ,sir")
    elif hour >12 and hour<=18: #hour should be  12 to 6
        speak("Good Afternoon ,sir")

    else:     #after 6 pm time
        speak("Good Evening,sir")

    speak("Please tell me, How can I help you ?")