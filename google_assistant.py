import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import os
import cv2
import sys
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty('voice' , voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def takeVoice():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("LISTENING....")
        r.pause_threshold = 1
        r.energy_threshold = 400
        audio = r.listen(source)
    try:
        print("recognizing Your voice....")
        query = r.recognize_google(audio, language='en-in')
    except Exception as e:
        print("cant recognize ur voice Please try  again")
        return "None"
    return query.lower()
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
    greet = "Hello!!! This is siri how can i help you..."
    speak(greet)
    print(greet)
    while True:
        userSaid = takeVoice()
        print(f"{userSaid}")
        if "open google" in userSaid:
            webbrowser.open("www.google.com")
        elif "open youtube" in userSaid:
            webbrowser.open("www.youtube.com")
        elif "open instagram" in userSaid:
            webbrowser.open("www.instagram.com")
        elif "open facebook" in userSaid:
            webbrowser.open("www.facebook.com")
        elif "play music" in userSaid:
            playmusic("D:\songs")
        elif  "open notepad" in userSaid:
            notepath ="C:\\Windows\\system32\\notepad.exe"
            os.startfile(notepath)
        elif "open cmd" in userSaid:
            os.system("start cmd")
        elif "open camera" in userSaid:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow("camera",img)
                k = cv2.waitKey(50)
                if k == 27:
                    break
            cap.release()
            cv2.destroyAllWindows()
        elif "exit" in userSaid:
            speak("THANK YOU")
            sys.exit() 

        else:
            speak("sorry please say it again..")

