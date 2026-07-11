import tkinter
import tkinter.ttk
screen = tkinter.Tk()
screen.geometry("400x350")
screen.title("Libary Management")

add_button = tkinter.Button(screen,text="Add Book")
borrow_button = tkinter.Button(screen,text= "Borrow Book")
return_button = tkinter.Button(screen,text= "Return Book")
search_button = tkinter.Button(screen,text = "Search")
tree_view = tkinter.ttk.Treeview(screen)
tree_view["columns"] = ("BookName","Author","Genre","Status")
tree_view["show"] = "headings"
tree_view.heading("BookName",text= "Book Name")
tree_view.heading("Author",text= "Author")
tree_view.heading("Genre",text= "Genre")
tree_view.heading("Status",text= "Status")
tree_view.column("BookName",width= 100)
label_1 = tkinter.Label(screen,text= "Book Details")
label_2 = tkinter.Label(screen,text= "Book Name: ")
label_3 = tkinter.Label(screen,text= "Author: ")
label_4 = tkinter.Label(screen,text= "Genre: ")
label_5 = tkinter.Label(screen,text= "Status: ")



entry_1 = tkinter.Entry(screen)
entry_2 = tkinter.Entry(screen)
entry_3 = tkinter.Entry(screen)


label_1.grid(column= 2,row = 1)

label_2.grid(column= 2,row = 2)
entry_1.grid(column=3,row= 2)

label_3.grid(column= 2,row = 3)
entry_2.grid(column=3,row= 3)

label_4.grid(column= 2,row = 4)
entry_3.grid(column=3,row= 4)

label_5.grid(column= 3,row = 4)

add_button.grid(column=1,row=2)
borrow_button.grid(column=1,row=3)
return_button.grid(column=1,row=4)
search_button.grid(column=1,row=5)

tree_view.grid(row= 9,column= 2)













screen.mainloop()