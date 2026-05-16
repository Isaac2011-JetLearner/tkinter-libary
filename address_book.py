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
    entry_1.delete(0,tkinter.END)
    entry_2.delete(0,tkinter.END)
    entry_3.delete(0,tkinter.END)
    entry_4.delete(0,tkinter.END)
    entry_5.delete(0,tkinter.END)

def view(event):
    get_info = list_box.curselection()
    name = list_box.get(get_info)
    values = keep[name]
    tkinter.messagebox.showinfo("Details","Name :"+name+"\nAddress :"+ values[0]+"\nMobile :"+ values[1]+ "\nEmail :"+ values[2]+"\nBirthday :"+values[3])


def Update_listbox():
    list_box.delete(0,tkinter.END)
    for name in keep.keys():
        list_box.insert(tkinter.END,name)

def delete():
    index_var = list_box.curselection()
    item = list_box.get(index_var)
    del keep[item]
    Update_listbox()

def save():
    save_file = tkinter.filedialog.asksaveasfile()
    if save_file != None:
        print(keep,file= save_file)
    
def open():
    global keep
    open_file = tkinter.filedialog.askopenfile()
    if open_file!= None:
       keep = eval(open_file.read())
       Update_listbox()

def edit():
    index = list_box.curselection()
    name = list_box.get(index)
    values = keep[name]
    entry_1.insert(tkinter.END,name)
    entry_2.insert(tkinter.END,values[0])
    entry_3.insert(tkinter.END,values[1])
    entry_4.insert(tkinter.END,values[2])
    entry_5.insert(tkinter.END,values[3])


label_1 = tkinter.Label(screen, text= "My Address Book:")
label_2 = tkinter.Label(screen,text= "Name:")
label_3 = tkinter.Label(screen,text = " Address:")
label_4 = tkinter.Label(screen,text= "Mobile:")
label_5 = tkinter.Label(screen, text = "Email:")
label_6 = tkinter.Label(screen,text ="Birthday:")

button_1 = tkinter.Button(screen,text="Open",command= open)
button_2 = tkinter.Button(screen,text="Edit",command= edit)
button_3 = tkinter.Button(screen,text="Delete",command= delete)
button_4 = tkinter.Button(screen,text="Save",command= save)
button_5 = tkinter.Button(screen,text="Update/add",command= update)

entry_1 = tkinter.Entry(screen)
entry_2 = tkinter.Entry(screen)
entry_3 = tkinter.Entry(screen)
entry_4 = tkinter.Entry(screen)
entry_5 = tkinter.Entry(screen)

list_box = tkinter.Listbox(screen)
list_box.bind("<<ListboxSelect>>",view)




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