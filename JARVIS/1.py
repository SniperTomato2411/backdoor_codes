import os
import openai
import pyttsx3
import speech_recognition as sr
from flask import Flask, render_template, request, jsonify

# Initialize Flask App
app = Flask(__name__)

# Initialize Text-to-Speech Engine (TTS)
tts_engine = pyttsx3.init()

def initialize_tts_engine():
    voices = tts_engine.getProperty('voices')
    tts_engine.setProperty('voice', voices[0].id)  # Use the default voice
    tts_engine.setProperty('rate', 150)  # Speed of speech
initialize_tts_engine()

# Set OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize Speech Recognizer (STT)
recognizer = sr.Recognizer()

# Function for AI Response
def get_ai_response(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150,
            temperature=0.7
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error: {str(e)}"

# Function for Text-to-Speech Output
def speak_text(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

# Function for Speech-to-Text Input
def listen_to_user():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        try:
            audio = recognizer.listen(source, timeout=5)
            return recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            return "Sorry, I didn't understand that."
        except sr.RequestError:
            return "Sorry, I couldn't access the speech recognition service."
        except Exception as e:
            return f"Error: {str(e)}"

# Flask Routes
@app.route('/')
def index():
    return "<h1>Personal AI Assistant</h1><p>Use endpoints to interact: /chat or /voice_chat</p>"

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_input = request.json.get('user_input', '')
        if not user_input:
            return jsonify({"error": "No user input provided."}), 400

        ai_response = get_ai_response(user_input)
        return jsonify({"user_input": user_input, "ai_response": ai_response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/voice_chat', methods=['POST'])
def voice_chat():
    try:
        user_input = listen_to_user()
        if "Error" in user_input:
            return jsonify({"error": user_input})

        ai_response = get_ai_response(user_input)
        speak_text(ai_response)
        return jsonify({"user_input": user_input, "ai_response": ai_response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
