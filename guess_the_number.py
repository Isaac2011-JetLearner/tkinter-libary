import tkinter
import tkinter.messagebox
import random
screen = tkinter.Tk()
screen.geometry("600x400")
screen.title("Guess The Number")

def info():
    tkinter.messagebox.showinfo("name",entry_1.get()+"! I am thinking of a number between 1 and 15")
    
number = random.randint(1,15)
def guess():
    if int(entry_2.get())<number:
        tkinter.messagebox.showinfo("Hint","Your number is lower than the answer")
    
    elif int(entry_2.get())>number:
        tkinter.messagebox.showinfo("Hint","Your number is higher than the answer")
    
    elif int(entry_2.get())==number:
        tkinter.messagebox.showinfo("Winner","You Win!!!!")

label_1 = tkinter.Label(screen,text= "Welcome to our game!")
label_2 = tkinter.Label(screen,text= "What is your name?")
label_3 = tkinter.Label(screen,text= "Take a guess: ")

entry_1 = tkinter.Entry(screen)
entry_2 = tkinter.Entry(screen,width=10)

button_1 = tkinter.Button(screen,text= "OK",command=info)
button_2 = tkinter.Button(screen,text= "Guess",command= guess)


label_1.grid(row=1,column=2)
label_2.grid(row=3,column=1)
label_3.grid(row=5,column=1)

entry_1.grid(row= 4,column=1)
entry_2.grid(row= 5,column=2,padx= 10)

button_1.grid(row= 4,column= 3)
button_2.grid(row= 5,column= 3)













screen.mainloop()