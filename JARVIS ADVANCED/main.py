import os   
import wikipedia as wiki
import webbrowser
import speech_recognition as sr                            
import pyttsx3
import datetime

# Initialize the text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Predefined password
PASSWORD = "mississippi"  # You can change this to any passcode you prefer

# Function to speak
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Function to wish the user based on the time
def wishme():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning sir.")
    elif 12 <= hour < 16:
        speak("Good afternoon sir.")
    else:
        speak("Good evening sir.")
    speak("May I know the passcode before we commence?")        

# Function to recognize user's speech
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        return query.lower()  # Return the recognized query in lowercase
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that. Could you please repeat?")
        speak("Sorry, I didn't catch that. Could you please repeat?")
    except sr.RequestError as e:
        print(f"Sorry, there was an error with the speech recognition service: {e}")
        speak(f"Sorry, there was an error with the speech recognition service: {e}")
    return None  # Return None if speech recognition fails

# Function to ask for and verify password
def checkPassword():
    speak("Please say the password.")
    password_attempt = takeCommand()  # Get password attempt from the user
    
    if password_attempt == PASSWORD:
        speak("Password correct. How may I assist you today?")
        return True
    else:
        speak("Incorrect password. Terminating program.")
        exit()

if __name__ == "__main__":
    wishme()
    
    # Ask for and verify password before proceeding
    if checkPassword():
        while True:
            query = takeCommand()

            if query:
                # Check if "Wikipedia" is in the query
                # if "wikipedia" or "wiki" in query:
                if "wikipedia" in query or "wiki" in query:
                   speak("Searching Wikipedia")
                   query = query.replace("wikipedia", "")
                   try:
                        results = wiki.summary(query, sentences=2)
                        speak("According to Wikipedia")
                        print(results)
                        speak(results)
                   except wiki.exceptions.DisambiguationError as e:
                       speak("I found multiple results. Please specify your query.")
                   except wiki.exceptions.PageError as e:
                        speak("I couldn't find any information on that topic.")

                elif "open youtube" in query:
                    webbrowser.open("https://www.youtube.com")
                elif "open google" in query:
                    webbrowser.open("https://www.google.com")
                elif "open gmail" in query:
                    webbrowser.open("https://mail.google.com")
                elif "open whatsapp" in query:
                    webbrowser.open("https://web.whatsapp.com")
                elif "open instagram" in query:
                    webbrowser.open("https://www.instagram.com")
                elif "open linked" in query:
                    webbrowser.open("https://www.linkedin.com/in/atharv-vij-313b15332/")
                elif "open facebook" in query:
                    webbrowser.open("https://www.facebook.com/")
                elif "open Asphalt" in query:
                    os.system("")

                # Play music
                elif "play music" in query:
                    music_dir = r'C:\Fav Songs'  # Use double backslashes in the path
                    try:
                        songs = [song for song in os.listdir(music_dir) if song.endswith(('.mp3', '.wav', '.flac'))]  # Filter only audio files
                        if songs:
                            print(songs)
                            os.startfile(os.path.join(music_dir, songs[0]))  # Play the first song
                            speak(f"Playing {songs[0]} for you.")
                        else:
                            speak("No audio files found in the directory.")
                    except Exception as e:
                        speak(f"Sorry, I encountered an error: {e}")

                elif "what is the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    speak(f"Sir, the time is {strTime}")

                elif "thank you" in query:
                    speak(f"My utmost pleasure sir")

                elif "terminate" in query or "close" in query or "stop" in query:
                    speak("Alright sir, I may take my leave now")
                    exit()