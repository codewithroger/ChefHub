import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

# Record audio from the microphone
with sr.Microphone() as source:
    print("Listening...")
    audio_data = recognizer.listen(source)
    print("Recognizing...")

    # Recognize speech using Google Web Speech API
    try:
        text = recognizer.recognize_google(audio_data)
        print("You said: " + text)
    except sr.UnknownValueError:
        print("Google Web Speech API could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Web Speech API; {e}")