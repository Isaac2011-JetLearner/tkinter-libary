import tkinter
import os
from gtts import gTTS
screen = tkinter.Tk()
screen.title("Text To Speech")
screen.geometry("400x400")

def enter():
    keep = entry_1.get()
    store = gTTS(keep,lang= "en")
    store.save("Text_to_speech.wav")
    os.system("Text_to_speech.wav")

label_1 = tkinter.Label(screen,text= "Text to Speech",background= "pink",width= 400,height= 7)
entry_1 = tkinter.Entry(screen,background= "light green",width= 200)
button = tkinter.Button(screen,text="SUBMIT",background= "yellow",width=50,height=7,command= enter)


label_1.pack()
entry_1.pack()
button.pack()



screen.mainloop()