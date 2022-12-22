import threading
import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
from ttkthemes import ThemedTk
import wikipedia
import webbrowser
import os
import email
import random
import webbrowser
import urllib
import re
import urllib.parse
import urllib.request
from ttkthemes import themed_tk
from tkinter import Image, ttk
import tkinter as tk
from tkinter import scrolledtext
import pywhatkit
import playsound
from PIL import ImageTk, Image
import subprocess
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

class note:
    def Note(self,data):
        date=datetime.datetime.now()
        filename=str(date).replace(':','-')+'-note.txt'
        a=os.getcwd()
        if not os.path.exists('Notes'):
            os.mkdir('Notes')
        os.chdir(a+r'\Notes')
        with open(filename,'w') as f:
            f.write(data)
        subprocess.Popen(['notepad.exe',filename])
        os.chdir(a)


def there_exists(terms, query):
    for term in terms:
        if term in query:
            return True


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am Friday. Please tell me how may I help you")


class MainframeThread(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name

    def run(self):
        mainframe()


def gen(n):
    for i in range(n):
        yield i


def Launching_thread():
    Thread_ID = gen(1000)
    global MainframeThread_object
    MainframeThread_object = MainframeThread(Thread_ID.__next__(), "Mainframe")
    MainframeThread_object.start()


def takeCommand():
    # it takes microphone input from user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1  # ......if we take gap while speaking system will wait for us
        audio = r.listen(source)

    try:
        print("Recognizing")
        query = r.recognize_google(audio, language="en-US")
        print(f"You said: {query}\n")

    except Exception as e:
        print(e)

        print("Say that again please....")
        return "None"
    return query


def mainframe():
    """Logic for execution task based on query"""
    wishMe()
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
    query_for_future = None
    try:
        while True:
            query = takeCommand().lower()
            if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to wikipedia")
                speak(results)
                print(results)

            elif 'open youtube' in query:
                speak("opening youtube")
                webbrowser.open("youtube.com")

            elif 'open google' in query:
                speak("opening google")
                webbrowser.open("google.com")

            elif 'open whatsapp' in query:
                speak("opening whatsapp")
                webbrowser.open("whatsapp.com")

            elif 'open stack overflow' in query:
                webbrowser.open("stackoverflow.com")
            
            elif 'open gmail' in query:
                webbrowser.open("gmail.com")
            
            

            elif 'play music' in query:
                music_dir = 'D:\\AI songs'
                songs = os.listdir(music_dir)
                print(songs)
                la = random.randint(0, 18)
                os.startfile(os.path.join(music_dir, songs[la]))

            elif 'open chrome'in query:
                speak("Opening chrome")
                os.startfile(r'C:\Program Files\Google\Chrome\Application\chrome.exe')
                
            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the thime is{strTime}")

            elif there_exists(['open file manager','file manager','open my computer','my computer','open file explorer','file explorer','open this pc','this pc'],query):
                speak("Opening File Explorer")
                os.startfile("C:\\Windows\\explorer.exe")
                
            elif there_exists(['powershell'],query):
                speak("Opening powershell")
                os.startfile(r'C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe')
                
            elif there_exists(['cmd','command prompt','command prom','commandpromt',],query):
                speak("Opening command prompt")
                os.startfile(r'C:\Windows\System32\cmd.exe')
                
            # elif there_exists(['open whatsapp'],query):
            #     speak("Opening whatsApp")
            #     os.startfile(r'C:\Users\Vishal\AppData\Local\WhatsApp\WhatsApp.exe')
            #     break
            elif there_exists(['open settings','open control panel','open this computer setting Window','open computer setting Window'   ,'open computer settings','open setting','show me settings','open my computer settings'],query):
                speak("Opening settings...")
                os.startfile('C:\\Windows\\System32\\control.exe')
                break

            elif 'open code' in query:
                speak("opening visual studio code")
                codePath = "D:\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)

            elif 'rock on' in query:
                speak("opening miles morales")
                codePath = "E:\\Marvels SpiderMan Miles Morales\\MilesMorales.exe"
                os.startfile(codePath)
            
            elif 'open firefox' in query:
                speak("opening firefox")
                codePath = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
                os.startfile(codePath)

            elif 'powershell' in query:
                speak("opening Powershell")
                codePath = "C:\\Users\\sarat\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Windows PowerShell\\powershell.exe"
                os.startfile(codePath)

            elif 'game on' in query:
                speak("opening spiderman")
                codePath = "D:\\Marvel's Spider-Man Remastered\\Spider-Man.exe"
                os.startfile(codePath)
            
            elif there_exists(['make a note','take note','take a note','note it down','make note','remember this as note','open notepad and write'],query):
                speak("What would you like to write down?")
                data=takeCommand()
                n= note()
                n.Note(data)
                speak("I have a made a note of that.")
                break

            elif there_exists(["toss a coin","flip a coin","toss"],query):
                moves=["head", "tails"]
                cmove=random.choice(moves)
                playsound.playsound('quarter spin flac.mp3')
                speak("It's " + cmove)
                break

            elif there_exists(['the time'],query):
                strTime =datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strTime}")
            elif there_exists(['the date'],query):
                strDay=datetime.date.today().strftime("%B %d, %Y")
                speak(f"Today is {strDay}")
            elif there_exists(['what day it is','what day is today','which day is today',"today's day name please"],query):
                speak(f"Today is {datetime.datetime.now().strftime('%A')}")

            elif there_exists(['open youtube and play', 'on youtube'], query):
                if 'on youtube' in query:
                    speak("Opening youtube")
                    pywhatkit.playonyt(query.replace('on youtube', ''))
                else:
                    speak("Opening youtube")
                    pywhatkit.playonyt(query.replace('open youtube and play ', ''))

            elif there_exists(['play some songs on youtube', 'i would like to listen some music', 'i would like to listen some songs', 'play songs on youtube'], query):
                speak("Opening youtube")
                pywhatkit.playonyt('play random songs')

            elif there_exists(['open youtube', 'access youtube'], query):
                speak("Opening youtube")
                webbrowser.get(chrome_path).open("https://www.youtube.com")

            elif there_exists(['open google and search', 'google and search'], query):
                url = 'https://google.com/search?q='+query[query.find('for')+4:]
                webbrowser.get(chrome_path).open(url)
    except Exception as e:
        pass


if __name__ == "__main__":
    
    root = ThemedTk()
    root.set_theme("winnative")
    root.geometry("{}x{}+{}+{}".format(745, 360, int(root.winfo_screenwidth() /
                  2 - 745/2), int(root.winfo_screenheight()/2 - 360/2)))
    root.resizable(0, 0)
    root.title("Friday")
    root.iconbitmap('Friday.ico')
    root.configure(bg='#2c4557')
    scrollable_text = scrolledtext.ScrolledText(
        root, state='disabled', height=15, width=87, relief='sunken', bd=5, wrap=tk.WORD, bg='#add8e6', fg='#800000')
    scrollable_text.place(x=10, y=10)
    mic_img = Image.open("Mic.png")
    mic_img = mic_img.resize((55, 55), Image.ANTIALIAS)
    mic_img = ImageTk.PhotoImage(mic_img)
    Speak_label = tk.Label(root, text="SPEAK:", fg="#FFD700",
                           font='"Times New Roman" 12 ', borderwidth=0, bg='#2c4557')
    Speak_label.place(x=250, y=300)
    """Setting up objects"""
    # query = takeCommand().lower() #Speak and Recognition class instance
    Listen_Button = tk.Button(root, image=mic_img, borderwidth=0,
    activebackground='#2c4557', bg='#2c4557', command=mainframe)
    Listen_Button.place(x=330, y=280)
    myMenu = tk.Menu(root)
    # tearoff=0 means the submenu can't be teared of from the window
    m1 = tk.Menu(myMenu, tearoff=0)
    # m1.add_command(label='Commands List',command=CommandsList)
    # myMenu.add_cascade(label="Help",menu=m1)
    # stng_win=Annex.SettingWindow()
    # myMenu.add_cascade(label="Settings",command=partial(stng_win.settingWindow,root))
    # myMenu.add_cascade(label="Clear Screen",command=clearScreen)
    root.config(menu=myMenu)
    root.mainloop()

    # elif 'on youtube' in query:
    #     song = urllib.parse.urlencode({query})
    #     result = urllib.request.urlopen("http://www.youtube.com/results?" + song)
    #     search_results = re.findall(r'href=\"\/watch\?v=(.{4})', result.read().decode())
    #     url = "http://www.youtube.com/watch?v="+str(search_results)
    #     webbrowser.open_new(url)

    # elif 'email to boss' in query:
    #     try:
    #         speak("What should I say")
    #         content = takeCommand()
    #         to = "saratehrishikesh17@gmail.com"
    #         sendEmail(to,content)
    #         speak("Email has been sent!")
    #     except Exception as e:
    #         print(e)
    #         speak("Sorry Sir,I am not able to send email at this moment")

    # elif 'pycharm' or 'open pie chart' in query:
    #     codePath = "C:\\Users\\sarat\\PyCharm Community Edition 2022.1.2\\bin\\pycharm64.exe"
    #     os.startfile(codePath)
