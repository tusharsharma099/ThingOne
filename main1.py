import speech_recognition as sr
import webbrowser
import pyttsx3

recoginizer= sr.Recognizer()
engine=pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processcommand(c):
    print(c)
    pass

if __name__=="__main__":

    speak("initializng Thing...!")
while True:
    # Listen for the wake word "Thing"
    # obtain audio from the microphone
    r = sr. Recognizer()
   

    print("recognizing...")
    try:
        with sr.Microphone() as source:
            print("listening..!")
            audio=r.listen(source,timeout=2,phrase_time_limit=1)
        word=r.recognize_bing(audio)
        if(word.lower()=="thing"):
            speak("Yes sirr")
        # listen for command 
            with sr.Microphone() as source:
                print("active Thing")
                audio=r.listen(source)
                command =r.recognize_amazon(audio)
    except Exception as e:
        print("Error;{0}". format(e))   