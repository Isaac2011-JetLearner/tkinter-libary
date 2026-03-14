import tkinter

screen = tkinter.Tk()
screen.geometry("600x600")
screen.title("Basics")

def login():
    complete = tkinter.Label(screen,text = "You Have Logged In!!!!")
    complete.place(x = 300, y= 300)


label = tkinter.Label(screen,text= "Username")
label_2 = tkinter.Label(screen, text= "Password")

entry = tkinter.Entry(screen)
entry_2 = tkinter.Entry(screen)

button = tkinter.Button(screen,text= "Login", command= login)
button_2 = tkinter.Button(screen,text= "Cancel")

# label.pack()
# label_2.pack()
# entry.pack()
# entry_2.pack()

label.grid(row = 1, column= 1)
entry.grid(row= 1, column = 2)

label_2.grid(row= 2, column = 1)   
entry_2.grid(row= 2, column= 2) 

button.grid(row= 3, column=1 )
button_2.grid(row= 3, column= 2)






screen.mainloop()

