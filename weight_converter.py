import tkinter

screen = tkinter.Tk()
screen.geometry("600x200")
screen.title("weight converter")

def converter():
    global label_5
    weight = int(entry.get())
    grams = weight*1000
    pounds = weight*2.22
    ounces = weight*35.3
    label_5 = tkinter.Label(screen,text=str(grams))
    label_5.grid(row=3,column=1)
    label_6 = tkinter.Label(screen,text= str(pounds))
    label_6.grid(row=3,column=2)
    label_7 = tkinter.Label(screen,text= str(ounces))
    label_7.grid(row=3,column=3)
    
    


label = tkinter.Label(screen,text="   Enter the weight in kg")
label_2 = tkinter.Label(screen,text="Gram")
label_3 = tkinter.Label(screen,text= "pounds")
label_4 = tkinter.Label(screen,text = "Ounce")
button = tkinter.Button(screen,text= "Convert",command =converter)

entry  = tkinter.Entry(screen,width= 20)



label.grid(row= 1, column= 1)
entry.grid(row=1,column=2,padx= 30)
button.grid(row= 1,column= 3)
label_2.grid(row = 2, column= 1)
label_3.grid(row=2,column=2)
label_4.grid(row= 2,column=3)







screen.mainloop()