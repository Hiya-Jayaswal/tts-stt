from gtts import gTTS
import os
import speech_recognition as sr

def text_to_speech():
    mytext = input("Enter the text you want to convert to speech: ")
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("output.mp3")
    os.system("start output.mp3")

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak something...")
        audio = recognizer.listen(source)
    
    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        print("You said:", text)
    except sr.UnknownValueError:
        print("Sorry, I could not understand what you said.")
    

def main():
    print("Select an option:")
    print("1. Text to Speech")
    print("2. Speech to Text")
    choice = input("Enter your choice (1 or 2): ")
    
    if choice == '1':
        text_to_speech()
    elif choice == '2':
        speech_to_text()
    else:
        print("Invalid choice. Please enter either 1 or 2.")

if __name__ == "__main__":
    main()