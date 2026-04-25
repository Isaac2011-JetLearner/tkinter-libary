import tkinter
import tkinter.ttk

screen = tkinter.Tk()
screen.title("Matimatical Table")
screen.geometry("500x500")

label_1 = tkinter.Label(screen,text="Matimatical Table")
label_2 =tkinter.Label(screen,text="Number and Range")
combo_box = tkinter.ttk.Combobox(screen)
numbers = []
for i in range(1,101):
    numbers.append(i)
combo_box["values"] = numbers
button = tkinter.Button(screen,text="Generate")
val = tkinter.IntVar()
radio_button_1 = tkinter.Radiobutton(screen,text="10",variable= val,value=10)
radio_button_2 = tkinter.Radiobutton(screen,text="20",variable= val,value= 20)
radio_button_3 = tkinter.Radiobutton(screen,text="30",variable= val, value= 30)


label_1.grid(row= 1,column=2)
label_2.grid(row= 2,column= 1)
combo_box.grid(row = 2,column=2)
radio_button_1.grid(row = 2,column=3)
radio_button_2.grid(row = 3,column=3)
radio_button_3.grid(row = 4,column=3)
button.grid(row=5,column=2)

tkinter.mainloop()





