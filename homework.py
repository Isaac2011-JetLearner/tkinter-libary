import tkinter
import calendar

screen = tkinter.Tk()
screen.geometry("600x500")
screen.title("CALENDAR")


def display():
   year = int(entry.get()) 
   indicator = calendar.calendar(year)
   

   screen_2 = tkinter.Tk()
   screen_2.geometry("900x1000")
   screen_2.title("Calendar")
   
   text = tkinter.Text(screen_2,width= 100, height= 60)
   text.insert(tkinter.END,indicator)
   text.pack()


   screen_2.mainloop()


    
   

label = tkinter.Label(screen,width=500,font=("algerian",75,"normal"), text="Calendar", background= "grey")
label_2 = tkinter.Label(screen,width= 150, font= ("Amasis MT Pro",10,"normal"),text ="Enter Year", background= "light green")

entry = tkinter.Entry(screen,width= 90,font=("Amasis MT Pro",10,"normal"))

button = tkinter.Button(screen,width= 70,text= "Show Calendar",command= display, font=("Amasis MT Pro",10,"normal"), background= "dark blue",activebackground= "light green")
button_2 = tkinter.Button(screen,width=30, text= "Exit", font=("Amasis MT Pro",10,"normal"), background= "dark green",activebackground= "light green")

label.pack()
label_2.pack()
entry.pack()
button.pack()
button_2.pack()



screen.mainloop()