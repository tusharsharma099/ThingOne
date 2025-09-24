import speech_recognition as sr
import webbrowser
import pygame
import google.generativeai as genai
import musiclib
import os
import datetime
import wikipedia
from gtts import gTTS
from newsapi import NewsApiClient

# Initialize pygame mixer for playing sound
pygame.mixer.init()

# --- API KEY CONFIGURATION ---
# Replace with your actual keys.
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY_HERE"
NEWS_API_KEY = "YOUR_NEWS_API_KEY_HERE"
WEATHER_API_KEY = "YOUR_WEATHER_API_KEY_HERE"

genai.configure(api_key=GEMINI_API_KEY)
newsapi = NewsApiClient(api_key=NEWS_API_KEY)

# --- HELPER FUNCTIONS ---
def speak(text):
    """Speaks the given text and prints it to the console using gTTS and pygame."""
    print(text)
    try:
        tts = gTTS(text=text, lang='en')
        filename = "temp_voice.mp3"
        tts.save(filename)
        
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()
        
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        
        pygame.mixer.music.unload()
        
        os.remove(filename)
        
    except Exception as e:
        print(f"gTTS or pygame speaking error: {e}")

def aiProcess(command):
    """Processes the command using the Google Gemini API's modern method."""
    try:
        model = genai.GenerativeModel('gemini-pro') 
        response = model.generate_content(command)
        return response.text
    except Exception as e:
        print(f"Gemini API error: {e}")
        return "I am unable to process that request at the moment."

def get_live_news():
    try:
        top_headlines = newsapi.get_top_headlines(country='in', language='en')
        articles = top_headlines['articles']
        if not articles:
            return "Sorry, I couldn't find any news headlines right now."
        
        headlines = [f"News headline: {article['title']}" for article in articles[:3]]
        return " and ".join(headlines)
    except Exception as e:
        print(f"News API error: {e}")
        return "Sorry, I am unable to fetch live news at the moment."

def get_current_time_date():
    now = datetime.datetime.now()
    date_str = now.strftime("%A, %B %d, %Y")
    time_str = now.strftime("%I:%M %p")
    return f"The current date is {date_str} and the time is {time_str}."

def get_weather(city_name):
    try:
        from pyowm.owm import OWM
        owm = OWM(os.environ.get("WEATHER_API_KEY", "YOUR_WEATHER_API_KEY_HERE"))
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place(city_name)
        weather = observation.weather
        
        temp_celsius = weather.temperature('celsius')['temp']
        status = weather.status
        
        return f"The weather in {city_name} is {status} with a temperature of {temp_celsius} degrees Celsius."
    except Exception as e:
        print(f"Weather API error: {e}")
        return "Sorry, I couldn't find the weather for that location."

def get_wikipedia_summary(query):
    try:
        search_results = wikipedia.search(query)
        if not search_results:
            return f"Sorry, I couldn't find any information on Wikipedia about {query}."
        
        summary = wikipedia.summary(search_results[0], sentences=2)
        return summary
    except wikipedia.exceptions.PageError:
        return f"Sorry, I couldn't find a Wikipedia page for {query}."
    except wikipedia.exceptions.DisambiguationError as e:
        return wikipedia.summary(e.options[0], sentences=2)
    except Exception as e:
        print(f"Wikipedia error: {e}")
        return "I encountered an error while searching Wikipedia."

def processcommand(c):
    """Processes the user's command."""
    print("Command received:", c)
    c_lower = c.lower()
    
    output = ""

    if "what is news" in c_lower or "tell me the news" in c_lower:
        output = get_live_news()
    
    elif "date" in c_lower or "time" in c_lower:
        output = get_current_time_date()
    
    elif "weather" in c_lower:
        city = c_lower.replace("what is the weather in", "").strip()
        output = get_weather(city)
    
    elif "wikipedia" in c_lower:
        query = c_lower.replace("search wikipedia for", "").replace("wikipedia", "").strip()
        output = get_wikipedia_summary(query)
    
    elif "open google" in c_lower:
        webbrowser.open("https://google.com")
        output = "Opening Google."
    elif "open youtube" in c_lower:
        webbrowser.open("https://youtube.com")
        output = "Opening YouTube."
    elif "open github" in c_lower:
        webbrowser.open("https://github.com")
        output = "Opening GitHub."
    elif "open whatsapp" in c_lower:
        webbrowser.open("https://whatsapp.com")
        output = "Opening WhatsApp."
    elif "open linkedin" in c_lower:
        webbrowser.open("https://linkedin.com")
        output = "Opening LinkedIn."
    elif "open instagram" in c_lower:
        webbrowser.open("https://instagram.com")
        output = "Opening Instagram."
    
    elif c_lower.startswith("search for") or c_lower.startswith("google search"):
        query = c_lower.replace("search for", "").replace("google search", "").strip()
        search_url = f"https://www.google.com/search?q={query}"
        webbrowser.open(search_url)
        output = f"Searching Google for {query}."

    elif c_lower.startswith("search on youtube for") or c_lower.startswith("youtube search"):
        query = c_lower.replace("search on youtube for", "").replace("youtube search", "").strip()
        youtube_url = f"https://www.youtube.com/results?search_query={query}"
        webbrowser.open(youtube_url)
        output = f"Searching YouTube for {query}."
        
    elif c_lower.startswith("play"):
        song = " ".join(c_lower.split(" ")[1:])
        link = musiclib.music.get(song, None)
        if link:
            webbrowser.open(link)
            output = f"Playing {song}."
        else:
            output = f"Sorry, I couldn't find a song named {song}."
    
    else:
        output = aiProcess(c)

    speak(output)

if __name__ == "__main__":
    speak("Initializing ThingOne. I'm ready to listen.")
    r = sr.Recognizer()
    listening_mode = False # A new variable to track the state

    while True:
        try:
            with sr.Microphone() as source:
                if not listening_mode:
                    print("Recognizing...")
                    print("Listening for wake word 'hey bro'...")
                    audio = r.listen(source, timeout=5, phrase_time_limit=3)
                    word = r.recognize_google(audio)
                    print("You said:", word)
                    
                    if "hey bro" in word.lower():
                        listening_mode = True
                        speak("Yes sir, I'm ready. I will listen continuously now.")
                        
                if listening_mode:
                    print("Active ThingOne, listening for command...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    print("Command:", command)
                    
                    if "bye bro" in command.lower():
                        speak("Goodbye, sir. I'm going to sleep now.")
                        listening_mode = False
                    else:
                        processcommand(command)

        except sr.UnknownValueError:
            if listening_mode:
                print("Could not understand audio. Still listening...")
            else:
                print("Could not understand audio.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
            listening_mode = False
