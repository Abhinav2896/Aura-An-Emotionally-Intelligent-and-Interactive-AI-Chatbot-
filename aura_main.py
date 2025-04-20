import speech_recognition as sr
import pyttsx3
import os
from modules import face_lock, weather, news, emailer
import wikipedia
import subprocess
import webbrowser

engine = pyttsx3.init()
def speak(text):
    print(f"Aura: {text}")
    engine.say(text)
    engine.runAndWait()

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        return recognizer.recognize_google(audio).lower()
    except:
        speak("Could you repeat that?")
        return ""

def execute_command(command):
    if "weather" in command:
        weather.get_weather()
    elif "news" in command:
        news.get_news()
    elif "email" in command:
        emailer.send_email()
    elif "youtube" in command:
        webbrowser.open("https://youtube.com")
    elif "wikipedia" in command:
        topic = command.replace("search", "").replace("on", "").strip()
        result = wikipedia.summary(topic, sentences=2)
        speak(result)
    elif "face lock" in command:
        face_lock.start_face_lock()
    elif "open" in command:
        app = command.replace("open", "").strip()
        subprocess.Popen(app)
    elif "tic tac toe" in command:
        os.system("python modules/games/tic_tac_toe.py")
    elif "lock" in command:
        speak("Locking the system by voice command")
        face_lock.lock_screen()
    elif "unlock" in command:
        face_lock.unlock_by_voice()
    elif "bye" in command:
        speak("Goodbye!")
        exit()
    else:
        speak("Sorry, I didn't understand that.")

if __name__ == "__main__":
    speak("Aura Online. Awaiting your command.")
    while True:
        cmd = take_command()
        execute_command(cmd)