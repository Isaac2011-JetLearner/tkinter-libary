import tkinter
import tkinter.ttk
import json
screen = tkinter.Tk()
screen.geometry("550x350")
screen.title("Libary Management")
libary = []
def add():
    store_1 = entry_1.get()
    store_2 = entry_2.get()
    store_3 = entry_3.get()
    book = {"BookName":store_1,"Author":store_2,"Genre":store_3,"Status":"Available"}
    libary.append(book)
    display_books()


def display_books():
    tree_view.delete(*tree_view.get_children())
    for book in libary:
        tree_view.insert("","end",values= (book["BookName"],book["Author"],book["Genre"],book["Status"]))


def save():
    file = open("libary_data.json","w")
    json.dump(libary,file,indent= 4)
    file.close()


def load():
    global libary
    file = open("libary_data.json","r")
    libary = json.load(file)
    file.close()

def borrow_book():
    id = tree_view.focus() 
    values = tree_view.item(id,"values")
    for  book in libary:
        if book["BookName"] == values[0]:
          book["Status"] = "borrowed"

    display_books()

def return_book():
    id = tree_view.focus()    
    values = tree_view.item(id,"values")   
    for book in libary:
        if book["BookName"] == values[0]:
            book["Status"] = "available"
    display_books()
add_button = tkinter.Button(screen,text="Add Book",command= add)
save_button = tkinter.Button(screen,text= "Save",command= save)
borrow_button = tkinter.Button(screen,text= "Borrow Book",command= borrow_book)
return_button = tkinter.Button(screen,text= "Return Book",command= return_book)
search_button = tkinter.Button(screen,text = "Search")
tree_view = tkinter.ttk.Treeview(screen)
tree_view["columns"] = ("BookName","Author","Genre","Status")
tree_view["show"] = "headings"
tree_view.heading("BookName",text= "Book Name")

tree_view.heading("Author",text= "Author")
tree_view["show"] = "headings"

tree_view.heading("Genre",text= "Genre")
tree_view["show"] = "headings"

tree_view.heading("Status",text= "Status")
tree_view["show"] = "headings"




    

tree_view.column("BookName",width= 70)
tree_view.column("Author",width= 70)
tree_view.column("Genre",width= 70)
tree_view.column("Status",width= 70)

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
save_button.grid(column=1,row = 6)


tree_view.grid(row= 9,column= 2)

load()
display_books()











screen.mainloop()