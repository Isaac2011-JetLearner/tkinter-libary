import tkinter
from tkinter.colorchooser import askcolor
screen = tkinter.Tk()
screen.title("Colour painter")
screen.geometry("375x375")

old_x = None
old_y = None 
pen_colour = "blue"
pen_width = 10
eraser_on = False
def draw(event):
    global eraser_on
    global old_x,old_y
    pen_width = scale.get()
    drawing_colour = pen_colour
    if eraser_on == True:
        drawing_colour = "White"
    
    if old_x and old_y:
        canvas.create_line(old_x,old_y,event.x,event.y,width= pen_width,fill= drawing_colour,smooth= True,capstyle= tkinter.ROUND)

    old_x = event.x
    old_y = event.y


def reset(event):
    global old_y,old_x
    old_y = None
    old_x = None

def eraser():
    global eraser_on
    eraser_on = True

def pen():
    global eraser_on
    global drawing_colour
    drawing_colour = pen_colour
    eraser_on = False

def colour():
    global pen_colour
    pen_colour = askcolor()[1]

    


button_1 = tkinter.Button(screen,text= "Pen",command= pen)
button_2 = tkinter.Button(screen,text= "Brush")
button_3 = tkinter.Button(screen,text= "Colour",command= colour)
button_4 = tkinter.Button(screen,text= "Eraser",command= eraser)
scale = tkinter.Scale(screen,orient= tkinter.HORIZONTAL,from_= 1,to = 10)
canvas = tkinter.Canvas(screen,background= "white")
canvas.bind_all("<B1-Motion>",draw)
canvas.bind_all("<ButtonRelease-1>",reset)


button_1.grid(row= 1,column=1)
button_2.grid(row= 1,column=2)
button_3.grid(row= 1,column=3)
button_4.grid(row= 1,column=4)
scale.grid(row= 1,column=5)
canvas.grid(row = 2,column=1,columnspan=5)



screen.mainloop()