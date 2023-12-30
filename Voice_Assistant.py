import pyttsx3
import speech_recognition as sr

def Speak(Text):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voices',voices[2].id)
    engine.setProperty('rate',170)
    text = "Voice Assistant"
    print("")
    print(f"{text} : {Text}.")
    print("")
    engine.say(Text)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=10,phrase_time_limit=5)

    try:
        print("Recognizing")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said : {query}")

    except Exception as e:
        print("Please Say that Again ..........!")    
        return "None"
    query = query.lower()
    return query

def WhatsApp():
    Speak("To open And Send A WhatsApp Message Please Say whatsapp chat")
    Speak("To use a whatsApp call Please say whatsapp call")
    Speak("")
    cm = takecommand().lower()
    if "whatsapp" in cm or "chat" in cm:
        from WhatsApp import main
        main()

    elif "whatsapp call" in cm or "whatsappcall" in cm:
        from WhatsAppCall import call
        call()

    else:
        exit()

if __name__=="__main__":
    WhatsApp()