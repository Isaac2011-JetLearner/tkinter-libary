import tkinter
import tkinter.filedialog
screen  = tkinter.Tk()
screen.geometry("400x300")
screen.title("Address Book")

keep = { }
def update():
    store_1 = entry_1.get()
    store_2 = entry_2.get()
    store_3 = entry_3.get()
    store_4 = entry_4.get()
    store_5 = entry_5.get()
    keep[store_1]  = [store_2,store_3,store_4,store_5]
    Update_listbox()


def Update_listbox():
    list_box.delete(0,tkinter.END)
    for name in keep.keys():
        list_box.insert(tkinter.END,name)

def delete():
    

label_1 = tkinter.Label(screen, text= "My Address Book:")
label_2 = tkinter.Label(screen,text= "Name:")
label_3 = tkinter.Label(screen,text = " Address:")
label_4 = tkinter.Label(screen,text= "Mobile:")
label_5 = tkinter.Label(screen, text = "Email:")
label_6 = tkinter.Label(screen,text ="Birthday:")

button_1 = tkinter.Button(screen,text="Open")
button_2 = tkinter.Button(screen,text="Edit")
button_3 = tkinter.Button(screen,text="Delete")
button_4 = tkinter.Button(screen,text="Save")
button_5 = tkinter.Button(screen,text="Update/add",command= update)

entry_1 = tkinter.Entry(screen)
entry_2 = tkinter.Entry(screen)
entry_3 = tkinter.Entry(screen)
entry_4 = tkinter.Entry(screen)
entry_5 = tkinter.Entry(screen)

list_box = tkinter.Listbox(screen)




label_1.grid(row= 1,column= 1)
label_2.grid(row= 2,column= 2)
label_3.grid(row= 3,column= 2)
label_4.grid(row = 4,column= 2)
label_5.grid(row = 5,column= 2)
label_6.grid(row = 6,column= 2)

button_1.grid(row= 1,column=2)
button_2.grid(row = 7,column= 1)
button_3.grid(row= 7,column=2 )
button_4.grid(row= 8,column=2)
button_5.grid(row=7,column=3)

entry_1.grid(row=2,column=3)
entry_2.grid(row=3,column=3)
entry_3.grid(row=4,column=3)
entry_4.grid(row=5,column=3)
entry_5.grid(row=6,column=3)

list_box.grid(row = 2,rowspan= 5, column= 1)

























tkinter.mainloop()