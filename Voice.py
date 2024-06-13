import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
    except sr.UnknownValueError:
        speak("Sorry, I did not understand that.")
        return None
    except sr.RequestError:
        speak("Sorry, my speech service is down.")
        return None
    return command.lower()

def tell_time():
    now = datetime.datetime.now()
    time_str = now.strftime("%H:%M")
    speak(f"The time is {time_str}")

def tell_date():
    today = datetime.date.today()
    date_str = today.strftime("%B %d, %Y")
    speak(f"Today's date is {date_str}")

def search_web(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    speak(f"Here are the search results for {query}")

def main():
    speak("Hello, how can I help you today?")
    while True:
        command = listen()
        if command is None:
            continue
        if "hello" in command:
            speak("Hello! How can I assist you?")
        elif "time" in command:
            tell_time()
        elif "date" in command:
            tell_date()
        elif "search for" in command:
            query = command.replace("search for", "").strip()
            search_web(query)
        elif "exit" in command or "quit" in command or "stop" in command:
            speak("Goodbye!")
            break
        else:
            speak("I'm sorry, I don't know how to help with that.")

if __name__ == '__main__':
    main()
