import tkinter
import time 
import tkinter.messagebox
screen = tkinter.Tk()
screen.geometry("600x400")
screen.title("Timer")


def timer():
    h =int(Entry_1.get())
    m =int(Entry_2.get())
    s =int(Entry_3.get())
    
    total_s = h*3600+m*60+s*1
    while total_s>0:
        total_s-=1
        th= total_s//3600
        tm = total_s%3600//60
        ts = total_s%60
        hours.set(th)
        minutes.set(tm)
        seconds.set(ts)

        screen.update()
        time.sleep(1)

        if th== 0 and tm == 0 and ts == 0:
            tkinter.messagebox.showinfo("Timer","Time is up")
        
    

hours = tkinter.StringVar()
minutes = tkinter.StringVar()
seconds = tkinter.StringVar()

hours.set("00")
minutes.set("00")
seconds.set("00")


Entry_1 = tkinter.Entry(screen,width= 10,textvariable= hours)
Entry_2 = tkinter.Entry(screen,width= 10,textvariable= minutes)
Entry_3 = tkinter.Entry(screen,width= 10,textvariable= seconds)
button = tkinter.Button(screen,text= "Set time countdown" ,command= timer)





Entry_1.grid(row= 2,column=1,padx= 10)
Entry_2.grid(row= 2,column=2)
Entry_3.grid(row= 2,column=3)
button.grid(row= 3,column=2)






screen.mainloop()