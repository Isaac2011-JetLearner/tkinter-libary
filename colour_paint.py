import tkinter
screen = tkinter.Tk()
screen.title("Colour painter")
screen.geometry("375x375")

button_1 = tkinter.Button(screen,text= "Pen")
button_2 = tkinter.Button(screen,text= "Brush")
button_3 = tkinter.Button(screen,text= "Colour")
button_4 = tkinter.Button(screen,text= "Eraser")
scale = tkinter.Scale(screen,orient= tkinter.HORIZONTAL,from_= 1,to = 10)
canvas = tkinter.Canvas(screen)


button_1.grid(row= 1,column=1)
button_2.grid(row= 1,column=2)
button_3.grid(row= 1,column=3)
button_4.grid(row= 1,column=4)
scale.grid(row= 1,column=5)
canvas.grid(row = 2,column=1,columnspan=5)



screen.mainloop()