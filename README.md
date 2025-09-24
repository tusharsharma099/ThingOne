# ThingOne 🤖

Thingone: Your Personal AI Voice Assistant
Thingone is a powerful, desktop-based AI voice assistant designed to simplify your daily tasks using simple voice commands. It combines modern AI capabilities with web automation to provide a seamless and interactive experience.

🚀 Key Features
Intelligent AI Responses: Powered by the Google Gemini API, Thingone can answer your questions, provide information, and engage in conversation.

Real-time Information: Get instant updates on the current date and time, live news headlines, and weather information for any city.

Knowledge Base: Get quick summaries on any topic by searching Wikipedia with your voice.

Web Automation: Open your favorite websites like Google, YouTube, and GitHub, and perform searches directly from your browser.

Music Playback: Play songs directly from web links defined in your musiclib.py file.

Continuous Listening: Once activated with the wake word, Thingone listens for commands continuously without needing to be prompted again.

⚙️ Setup and Installation
Prerequisites
You need Python 3.x installed on your system.
This project requires the following Python libraries. You can install them using pip:

Bash

pip install SpeechRecognition
pip install pyttsx3
pip install google-generativeai
pip install wikipedia
pip install newsapi-python
pip install pyowm
pip install pygame
pip install gTTS
API Keys
Some features require a personal API key. Get your free keys from the following services and paste them into your Thingone.py script.

Google Gemini API: Get your key here

News API: Get your key here

OpenWeatherMap: Get your key here

How to Run
Clone this repository or download the source code.

Open the Thingone.py file and insert your API keys where indicated.

Open your terminal or command prompt in the project directory.

Run the script using the following command:

Bash

python Thingone.py
🗣️ Usage
Once the program is running, it will say "Initializing Thingone. I'm ready to listen."

Wake Word: Say "Hey bro" to activate the assistant.

Continuous Listening: After activation, you can give multiple commands without saying "Hey bro" again.

Exit: To make Thingone stop listening, say "Bye bro".

Available Voice Commands
General/AI:

"Who is Virat Kohli?"

"Tell me a joke."

Time & Date:

"What's the time?"

"What is the date today?"

News & Weather:

"Tell me the news."

"What is the weather in [city name]?"

Wikipedia:

"Search Wikipedia for [topic]."

"Wikipedia [topic]."

Web & Search:

"Open Google."

"Search for [something]."

"Search on YouTube for [something]."

"Open YouTube."

Music:

"Play [song name]."

🐛 Troubleshooting
"Permission denied" Error: Run your terminal or command prompt as an administrator and try again.

pyttsx3 not speaking: Check your system's text-to-speech drivers.

API Key Error (e.g., 404 Not Found): The API key is either incorrect or not yet active. Please double-check the key or try generating a new one.
