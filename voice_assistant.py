import speech_recognition as sr
import ollama
import pyttsx3


# -------------------- EARS (Speech to Text) --------------------
def listen():
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("Listening... (Speak now)")
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            print("Processing...")

        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text

    except sr.WaitTimeoutError:
        print("No speech detected.")
        return None

    except sr.UnknownValueError:
        print("Sorry, I didn't understand.")
        return None

    except sr.RequestError:
        print("Speech recognition service error.")
        return None

    except Exception as e:
        print(f"Listen error: {e}")
        return None


# -------------------- BRAIN (LLM Thinking) --------------------
def think(text: str):
    if not text:
        return None

    print("Thinking...")

    try:
        response = ollama.chat(
            model="llama3",
            messages=[
                {"role": "user", "content": text}
            ]
        )

        reply = response["message"]["content"]
        print(f"AI: {reply}")
        return reply

    except Exception as e:
        print(f"Think error: {e}")
        return "Sorry, I had trouble thinking."


# -------------------- MOUTH (Text to Speech) --------------------
def speak(text: str):
    if not text:
        return

    try:
        engine = pyttsx3.init()
        engine.setProperty("rate", 175)
        engine.say(text)
        engine.runAndWait()

    except Exception as e:
        print(f"Speak error: {e}")


# -------------------- MAIN LOOP --------------------
def main():
    print("--- Voice Assistant Started ---")
    speak("Hello, I am ready. You can start speaking.")

    while True:
        user_input = listen()

        if not user_input:
            continue

        if user_input.lower().strip() in ["exit", "quit", "stop"]:
            speak("Goodbye!")
            print("Exiting...")
            break

        ai_response = think(user_input)
        speak(ai_response)


# -------------------- ENTRY POINT --------------------
if __name__ == "__main__":
    main()
