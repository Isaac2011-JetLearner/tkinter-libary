import tkinter
import tkinter.filedialog
screen = tkinter.Tk()
screen.geometry ="600X600"
screen.title("Memoriser")


def add():
    Get = entry_1.get()
    list_box.insert(tkinter.END,Get)

def delete():
    Get_2 = list_box.curselection()
    list_box.delete(Get_2)

def save():
    save_file = tkinter.filedialog.asksaveasfile()
    if save_file != None:
        store = list_box.get(0,tkinter.END)
        for item in store:
            print(item,file= save_file)

def open():
    open_file = tkinter.filedialog.askopenfile()
    if open_file != None:
       read = open_file.readlines()
       for item in read:
           list_box.insert(tkinter.END,item)




button_1 = tkinter.Button(screen,text= "OPEN",command= open)
button_2 = tkinter.Button(screen,text = "DELETE",command= delete)
button_3 = tkinter.Button(screen,text = "SAVE",command= save)
button_4 = tkinter.Button(screen,text = "ADD",command= add)

entry_1 = tkinter.Entry(screen)
list_box = tkinter.Listbox(screen)

button_1.grid(row= 1,column= 1)
button_2.grid(row= 1,column= 2)
button_3.grid(row= 1,column= 3)
button_4.grid(row= 2,column= 3)
entry_1.grid(row= 2,column=2)
list_box.grid(row=3 ,column=1,columnspan= 3)

screen.mainloop()