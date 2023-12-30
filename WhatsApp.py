from time import sleep
import pyautogui
import speech_recognition as sr
from Voice_Assistant import Speak

def search_contact(name):
    print("The Receiver Name is :- ",name)
    pyautogui.press("win")
    sleep(1.5)
    pyautogui.write("whatsapp")
    sleep(1)
    pyautogui.press("enter")
    sleep(3)

    try:
        # x, y = pyautogui.locateCenterOnScreen("res\\WhatsappSearch.png", confidence=0.8)
        # if (x!=None and y!=None):
        #     pyautogui.moveTo(x, y, duration=0.5)
        #     pyautogui.leftClick()
            pyautogui.hotkey("ctrl","f")
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
        
def send_message(msg):
    try:
        x, y = pyautogui.locateCenterOnScreen("res\\TypeMsg.png", confidence=0.7)
        if (x!=None and y!=None):
            pyautogui.moveTo(x, y, duration=0.5)
            pyautogui.leftClick()
            sent = msg
            pyautogui.write(sent)
            Speak("Are You Sure To Send The Message")
            Speak("if you Sure To Send the message please say Yes and if you are not sure please say No")
            mg = takecommand().lower()
            if "yes" in mg:
                pyautogui.press("enter")
                Speak("Message has been send")
                pyautogui.hotkey("alt","f4")
            else:
                Speak("Message Can Not be Send")
                pyautogui.hotkey("alt","f4")
        else:
            Speak("Try again")
    except:
        x,y = pyautogui.locateCenterOnScreen("res\\send.png",confidence=0.8)
        x = x-45
        y = y-0
        pyautogui.moveTo(x,y,duration=0.5)
        pyautogui.leftClick()
        pyautogui.hotkey("ctrl","a")
        pyautogui.press("backspace")
        sent = msg
        pyautogui.write(sent)
        Speak("Are You Sure To Send The Message")
        Speak("if you Sure To Send the message please say Yes and if you are not sure please say No")
        mg1 = takecommand().lower()
        if "yes" in mg1:
            pyautogui.press("enter")
            Speak("Message has been send")
            pyautogui.hotkey("alt","f4")
        else:
            Speak("Message Can Not be Send")
            pyautogui.hotkey("alt","f4")

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

def main():
    Speak("tell me receiver name")
    print("Please Enter Receiver Name")
    name = takecommand().lower()
    Speak("The Receiver Name is")
    Speak(name)
    Speak("Tell Me The Message")
    print("Tell Me The Message")
    msg = takecommand().lower()
    Speak("The Message is")
    Speak(msg)
    if (name!="none" and msg!= "none"):
        search_contact(name)
        send_message(msg)
    elif (name == "none" or msg == "none"):
        Speak("Please say again name and message ")
        main()
    else:
        Speak("Speech not recognized or understood.")
