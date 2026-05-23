import tkinter
import tkinter.filedialog
screen =tkinter.Tk()
screen.geometry("500x400")
screen.title("Smart Inventory Manager")
store = { }
def add():
    keep_1 = entry_1.get()
    keep_2 = entry_2.get()
    keep_3 = entry_3.get()
    keep_4 = entry_4.get()
    store[keep_1] = [keep_2,keep_3,keep_4]

    upd_listbox()
    entry_1.delete(0,tkinter.END)
    entry_2.delete(0,tkinter.END)
    entry_3.delete(0,tkinter.END)
    entry_4.delete(0,tkinter.END)
    

def upd_listbox():
    list_box.delete(0,tkinter.END)
    for name in store.keys():
        list_box.insert(tkinter.END,name)

def view(event):
    get_info = list_box.curselection()
    name = list_box.get(get_info)
    values = store[name]
    tkinter.messagebox.showinfo("Details","Product Name :"+name+"\nProduct ID:" + values[0]+"\nPrice :"+ values[1]+ "\nQantity :"+ values[2]+ "")

def delete():
    select = list_box.curselection()
    store_item = list_box.get(select)
    del store[store_item]
    upd_listbox()

def clear():
    list_box.delete(0,tkinter.END)

label_1 =  tkinter.Label(screen,text= "Smart Inventory Manager")
label_2 =  tkinter.Label(screen,text= "Product Name: ")
label_3 =  tkinter.Label(screen,text= "Product ID: ")
label_4 =  tkinter.Label(screen,text= "Price ($): ")
label_5 =  tkinter.Label(screen,text= "Quantity: ")

entry_1 = tkinter.Entry(screen)
entry_2 = tkinter.Entry(screen)
entry_3 = tkinter.Entry(screen)
entry_4 = tkinter.Entry(screen)

button_1 =  tkinter.Button(screen,text= "Add item",command= add,bg= "green")
button_2 =  tkinter.Button(screen,text= "Delete",command= delete,bg = "red")
button_3 =  tkinter.Button(screen,text= "Clear",command= clear,bg= "orange")

list_box = tkinter.Listbox(screen)
list_box.bind("<<ListboxSelect>>",view)


label_1.grid(row=1,column=2,columnspan= 3)
label_2.grid(row= 2,column=1)
label_3.grid(row= 3,column=1)
label_4.grid(row=4,column=1)
label_5.grid(row= 5,column=1)

entry_1.grid(row= 2,column=2)
entry_2.grid(row=3,column=2)
entry_3.grid(row=4,column= 2 )
entry_4.grid(row= 5,column= 2)

button_1.grid(row=6,column=1)
button_2.grid(row=6,column=2)
button_3.grid(row=6,column=3)

list_box.grid(row= 2,rowspan=4,column=4 )

















tkinter.mainloop()