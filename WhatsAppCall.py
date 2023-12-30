from time import sleep
import pyautogui
import speech_recognition as sr
from Voice_Assistant import Speak

def VoiceCall(name):
    print("The Receiver Name is :- ",name)
    pyautogui.press("win")
    sleep(1.5)
    pyautogui.write("whatsapp")
    sleep(1)
    pyautogui.press("enter")
    sleep(3)

    try:
        x, y = pyautogui.locateCenterOnScreen("res\\WhatsappSearch.png", confidence=0.8)
        if (x!=None and y!=None):
            pyautogui.moveTo(x, y, duration=0.5)
            pyautogui.leftClick()
            sleep(1)
            contect = name
            pyautogui.write(contect)
            sleep(2)
            pyautogui.press("down")
            pyautogui.press("enter")
            sleep(1)
        
    except:
        x,y =  pyautogui.locateCenterOnScreen("res\\closewp.png",confidence=0.8)  
        pyautogui.moveTo(x,y,duration=0.5)
        pyautogui.leftClick()   
        contect = name 
        pyautogui.write(contect)
        sleep(2)
        pyautogui.press("down")
        pyautogui.press("enter")
        sleep(1)

def VoiceCallInside():
    x,y = pyautogui.locateCenterOnScreen("res\\voicecall.png",confidence=0.8)
    pyautogui.moveTo(x,y,duration=0.5)
    Speak("Are You Sure You Make A Voice Call")
    Speak("if you Sure To  make a call please say Yes and if you are not sure please say No")
    cl = takecommand().lower()
    if(cl!="none"):
        cl1 = takecommand().lower()
        if "yes" in cl1 or "yas" in cl1:
            Speak("Before i connect with this person You have two options")
            Speak("To Mute the Call Say Mute")
            Speak("To End the Call Say End")
            pyautogui.leftClick()
        
            cm = takecommand().lower()
            if "end" in cm or "and" in cm:
                pyautogui.hotkey("alt","f4")
                pyautogui.press("enter")
            elif "mute" in cm:
                x,y = pyautogui.locateCenterOnScreen("res\\mute.png",confidence=0.8)
                pyautogui.moveTo(x,y,duration=0.5)
                pyautogui.leftClick()
            else:
                Speak("Voice Does Not Recorgnize Please try again")
                pyautogui.hotkey("alt","f4")
                sleep(1)
                pyautogui.press("enter")
                sleep(2)
                pyautogui.hotkey("alt","f4")
        else:
            Speak("voice call Canceled")
            pyautogui.hotkey("alt","f4")
    else:
        Speak("Please can you tell me again")
        VoiceCallInside()

def VedioCall(name):
    print("The Receiver Name is :- ",name)
    pyautogui.press("win")
    sleep(1.5)
    pyautogui.write("whatsapp")
    sleep(1)
    pyautogui.press("enter")
    sleep(3)

    try:
        x, y = pyautogui.locateCenterOnScreen("res\\WhatsappSearch.png", confidence=0.8)
        if (x!=None and y!=None):
            pyautogui.moveTo(x, y, duration=0.5)
            pyautogui.leftClick()
            sleep(1)
            contect = name
            pyautogui.write(contect)
            sleep(2)
            pyautogui.press("down")
            pyautogui.press("enter")
            sleep(1)
        
    except:
        x,y =  pyautogui.locateCenterOnScreen("res\\closewp.png",confidence=0.8)  
        pyautogui.moveTo(x,y,duration=0.5)
        pyautogui.leftClick()   
        contect = name 
        pyautogui.write(contect)
        sleep(2)
        pyautogui.press("down")
        pyautogui.press("enter")
        sleep(1)

def VedioCallInside():
    x,y = pyautogui.locateCenterOnScreen("res\\videocall.png",confidence=0.8)
    pyautogui.moveTo(x,y,duration=0.5)
    Speak("Are You Sure You Can Make A Voice Call")
    Speak("if you Sure To Send the message please say Yes and if you are not sure please say No")
    cl = takecommand().lower()
    if(cl!="none"):
        cl1 = takecommand().lower()
        if "yes" in cl1 or "yas" in cl1:
            Speak("To Mute the Call Say Mute")
            Speak("To End the Call Say End")
            pyautogui.leftClick()
            cm = takecommand().lower()
            if "end" in cm:
                pyautogui.hotkey("alt","f4")
                pyautogui.press("enter")
            elif "mute" in cm:
                x,y = pyautogui.locateCenterOnScreen("res\\mute.png",confidence=0.8)
                pyautogui.moveTo(x,y,duration=0.5)
                pyautogui.leftClick()
            else:
                Speak("Voice Does Not Recorgnize Please try again")
                pyautogui.hotkey("alt","f4")
                sleep(1)
                pyautogui.press("enter")
                sleep(2)
                pyautogui.hotkey("alt","f4")
        else:
            Speak("video call Canceled")
            pyautogui.hotkey("alt","f4")
    else:
        Speak("Please can you tell me again")
        VoiceCallInside()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..........")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=10, phrase_time_limit=5)

    try:
        print("Recognizing")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said : {query}")
        return query.lower()
    except Exception as e:
        print("Please Say that Again ..........!")
        return "None"

def call():
        Speak("Which call do you want to Voice call or Video call")
        tk = takecommand().lower()
        if(tk!="none"):
            if "voicecall" in tk or "voice call" in tk or "voice" in tk:
                Speak("Please Tell Me Name You want to call")
                name = takecommand().lower()
                VoiceCall(name)
                VoiceCallInside()
            elif "videocall" in tk or "video call" in tk or "video" in tk:
                Speak("Please Tell Me Name You want to call")
                name = takecommand().lower()
                VedioCall(name)
                VedioCallInside()
            else:
                Speak("Voice does not recorginize Please try again")
        else:
            Speak("Please Say Again")
            call()

