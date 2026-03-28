import tkinter
import random
screen = tkinter.Tk()
screen.geometry("800x400")
screen.title("Rock-Paper-scissors")
player_score = 0
computer_score = 0
selections = ["rock","paper","scissor"]
def choice(user):
    global player_score,computer_score
    computer = random.choice(selections)
    label_7.config(text= "Computer Selected :"+computer)
    label_5.config(text="Player Selected :"+ user) 

    if user == "rock" and computer == "scissor":
        player_score+=1
        label_6.config(text= "Player Score :"+str(player_score))
        label_4.config(text = "You win")
    
    if user == "paper" and computer == "rock":
       player_score+=1
       label_6.config(text= "Player Score :"+str(player_score))
       label_4.config(text = "You win")

    if user == "scissor" and computer == "paper":
        player_score+=1
        label_6.config(text= "Player Score :"+str(player_score))
        label_4.config(text = "You win")

    if user == "paper" and computer == "paper":
        label_4.config(text= "Its A Draw")    

    if user == "rock" and computer == "rock":
        label_4.config(text= "Its A Draw")

    if user == "scissor" and computer == "scissor":
        label_4.config(text= "Its A Draw")

    if user == "rock" and computer == "paper":
        computer_score+=1
        label_8.config(text= "Computer Score :"+str(computer_score))
        label_4.config(text= "You Lose")

    if user == "paper" and computer == "scissor":
        computer_score+=1
        label_8.config(text= "Computer Score :"+str(computer_score))
        label_4.config(text= "You Lose")
    
    if user == "scissor" and computer == "rock":
        computer_score+=1
        label_8.config(text= "Computer Score :"+str(computer_score))
        label_4.config(text= "You Lose")
        

    
   

        
    


label_1 = tkinter.Label(screen,text="Rock Paper Scissors",font= ("Algerian",30))
label_2 = tkinter.Label(screen, text= "Your Options:")
label_3 = tkinter.Label(screen, text= "Score:")
label_4 = tkinter.Label(screen,text= "You Won!!!!")
label_5 = tkinter.Label(screen,text= "You Selected: ")
label_6 = tkinter.Label(screen,text= "Player Score: " )
label_7 = tkinter.Label(screen,text= "Computer Selected: ")
label_8 = tkinter.Label(screen,text= "Computer Score: ")


button_1 = tkinter.Button(screen,text= "Rock",width= 20,command= lambda:choice(user= "rock"))
button_2 = tkinter.Button(screen,text = "Paper",width= 20,command= lambda:choice(user= "paper"))
button_3 = tkinter.Button(screen,text= "Scissor",width= 20,command= lambda:choice(user= "scissor"))

label_1.grid(row= 1, column= 2,columnspan= 2)
label_2.grid(row= 4,column= 1)
label_3.grid(row=5,column= 1)
label_4.grid(row=2, column= 2,columnspan=2)
label_5.grid(row= 5,column=2)
label_6.grid(row = 5,column= 3)
label_7.grid(row= 6, column= 2)
label_8.grid(row=6,column=3)


button_1.grid(row= 4, column= 2,padx = 10)
button_2.grid(row= 4, column= 3)
button_3.grid(row= 4, column= 4)

















screen.mainloop()