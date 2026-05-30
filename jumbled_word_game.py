import tkinter
import random
import tkinter.messagebox
screen = tkinter.Tk()
screen.geometry("400x400")
screen.title("Jumbled Word Game")
screen.config(background= "black")

words =["computer","ability","ballon","correct","crystal","country","desire","dealing","universe","junction"]
word = ""

def scramble():
    global word
    word = random.choice(words) 
    characters = list(word)
    random.shuffle(characters)
    jumbled = "".join(characters)
    label_2.config(text= jumbled)

score = 0
def upd_score():
    global score
    if collect == word:
        score+=1
        label_3.config(text= "Score :"+ str(score))
       
        
    
def check():
    global score
    global collect
    collect = entry_1.get()
    if collect == word:
        tkinter.messagebox.showinfo("congratulations", "It's the correct answer.")
        upd_score()
    else:
        tkinter.messagebox.showinfo("You lost", "The correct word was "+ word)
        
    entry_1.delete(0,tkinter.END)
    scramble()
    


label_1 = tkinter.Label(screen,text= "Jumbled Word Game")
label_2 = tkinter.Label(screen,text= "")
label_3 = tkinter.Label(screen,text= "Score :"+ str(score), background= "red")

entry_1 = tkinter.Entry(screen)
button_1 = tkinter.Button(screen,text= "Check",bg= "Dark grey",command= check)
button_2 = tkinter.Button(screen,text= "Reset",bg= "Grey",)

scramble()

label_1.pack()
label_2.pack()
label_3.place(x = 10, y =10)
entry_1.pack()
button_1.pack()
button_2.pack()




















tkinter.mainloop()