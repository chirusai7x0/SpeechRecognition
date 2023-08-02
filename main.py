import speech_recognition as sr

def speech_to_text():
    # Create a recognizer instance
    recognizer = sr.Recognizer()

    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Say something...")
        # Adjust ambient noise levels for clearer recognition
        recognizer.adjust_for_ambient_noise(source)
        # Listen to the user's speech
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
    except sr.RequestError:
        print("Couldn't request results from Google Web Speech API. Check your internet connection.")

    return None

# Call the speech_to_text function to get the recognized text
recognized_text = speech_to_text()
if recognized_text:
    print("You said:", recognized_text)
