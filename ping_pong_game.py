import tkinter
screen = tkinter.Tk()
screen.title("Ping Pong Game")
screen.geometry("800x400")


canvas = tkinter.Canvas(screen,background= "black",width= 800,height= 400)
canvas.create_line(400,0,400,400,fill= "white",width= 3)
canvas.create_oval(360,160,440,240,outline= "white",width= 3)

canvas.pack()




screen.mainloop()