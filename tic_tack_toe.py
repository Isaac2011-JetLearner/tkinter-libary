import tkinter
import random
import tkinter.messagebox
screen = tkinter.Tk()
screen.title("Tic tack toe")
screen.geometry("456x360")


def mark(button_selected):
    if button_selected in avaliable_buttons: 
        button_selected.config(text= "X")
        avaliable_buttons.remove(button_selected)
        check()
        choose = random.choice(avaliable_buttons)
        choose.config(text= "O")
        avaliable_buttons.remove(choose)
        check()

def check():
    for win in winning_combos:
        if win[0]["text"] == "X" and win[1]["text"] == "X" and win[2]["text"] == "X":
            tkinter.messagebox.showinfo("YOU WIN!!!","Congratulations you win!!!")
            return

        elif win[0]["text"] == "O" and win[1]["text"] == "O" and win[2]["text"] == "O":
            tkinter.messagebox.showinfo("You Lose","You lost try again")
            return
            
    if len(avaliable_buttons) == 0:
        tkinter.messagebox.showinfo("TIE","It is a tie")
    

button_1 = tkinter.Button(screen,width= 20,height=5,command= lambda: mark(button_1))
button_2 = tkinter.Button(screen,width= 20,height=5,command= lambda: mark(button_2))
button_3 = tkinter.Button(screen,width= 20,height=5,command= lambda: mark(button_3))
button_4 = tkinter.Button(screen,width= 20,height=5,command= lambda: mark(button_4))
button_5 = tkinter.Button(screen,width= 20,height=5,command= lambda: mark(button_5))
button_6 = tkinter.Button(screen,width= 20,height=5,command= lambda: mark(button_6))
button_7 = tkinter.Button(screen,width= 20,height=5,command= lambda: mark(button_7))
button_8 = tkinter.Button(screen,width= 20,height=5,command= lambda: mark(button_8))
button_9 = tkinter.Button(screen,width= 20,height=5,command= lambda: mark(button_9))


avaliable_buttons = [button_1,button_2,button_3,button_4,button_5,button_6,button_7,button_8,button_9]
winning_combos = [(button_1,button_2,button_3),(button_1,button_4,button_7),(button_2,button_5,button_8),(button_3,button_6,button_9),(button_1,button_5,button_9),(button_3,button_5,button_7),(button_4,button_5,button_6),(button_7,button_8,button_9)]


button_1.grid(row= 1,column= 1)
button_2.grid(row= 1,column= 2)
button_3.grid(row= 1,column= 3)
button_4.grid(row= 2,column= 1)
button_5.grid(row= 2,column= 2)
button_6.grid(row= 2,column= 3)
button_7.grid(row= 3,column= 1)
button_8.grid(row= 3,column= 2)
button_9.grid(row= 3,column= 3)


























screen.mainloop()