import speech_recognition as sr
import webbrowser
import pyttsx3
import openai
import musiclib

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def aiProcess(command):
    client = openai(api_key="######")

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a virtual assistant named Jarvis, skilled in general tasks like Alexa and Google Assistant."
            },
            {
                "role": "user",
                "content": command
            }
        ]
    )

    response = completion.choices[0].message.content    

def processcommand(c):
    print("Command received:", c)
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif c.lower().startswith("play"):
        # song=c.lower().split(" ")[1]
        song = " ".join(c.lower().split(" ")[1:])
        link = musiclib.music[song]
        webbrowser.open(link)  

    else:
       output= aiProcess(c)
       speak(output)      
    
    # you cxan pass here your command 

if __name__ == "__main__":
    speak("Initializing Thing...!")

    r = sr.Recognizer()

    while True:
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=5, phrase_time_limit=3)

            word = r.recognize_google(audio)
            print("You said:", word)

            if word.lower() == "hey bro":
                speak("Yes sir")

                # listen for command 
                with sr.Microphone() as source:
                    print("Active Thing, listening for command...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    print("Command:", command)
                    processcommand(command)

        except Exception as e:
            print("Error; {0}".format (e))
