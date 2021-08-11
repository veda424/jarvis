import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import os
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty('voice' , voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def takeVoice():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("LISTENING....")
        print("LISTENING....")
        r.pause_threshold = 1
        r.energy_threshold = 400
        audio = r.listen(source)
    try:
        print("recognizing Your voice....")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said:{query}")
    except Exception as e:
        print("cant recognize ur voice Please try  again")
        return "None"
    return query
def playmusic(path):
    import random
    randno = random.randint(1, 10)
    songs = os.listdir(path)
    os.startfile(os.path.join(path, songs[randno]))
    
def greetme():
    hrs = int(datetime.datetime.now().hour)
    if hrs >= 0 and hrs <= 12:
        speak("Good Moring..")
    elif hrs > 12 and hrs <=18:
        speak("Good Afternoon..")
    else:
        speak("Good Evening...")

if __name__ == '__main__':
    greetme()
    greet = "Hello!!! im Shrishti how can i help you..."
    speak(greet)
    print(greet)
    userSaid = takeVoice().lower()
    if "open google" or "google" in userSaid:
        webbrowser.open("www.google.com")
    elif "open youtube" or "youtube" in userSaid:
        webbrowser.open("www.youtube.com")
    elif "open instagram" or "instagram" in userSaid:
        webbrowser.open("www.instagram.com")
    elif "open facebook" or "facebook" in userSaid:
        webbrowser.open("www.facebook.com")
    elif "play music" or "play songs" or "play song" in userSaid:
        playmusic("D:\songs")


