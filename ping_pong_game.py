import tkinter
import time
screen = tkinter.Tk()
screen.title("Ping Pong Game")
screen.geometry("800x400")

class Ball():
    def __init__(self):
        self.ball = canvas.create_oval(700,0,720,20,fill= "yellow")
        self.speedx = -2
        self.speedy = -2
        self.score1 = 0
        self.score2 = 0


    def movement(self):
        canvas.move(self.ball,self.speedx,self.speedy)
        keep = canvas.coords(self.ball)
        if keep[0] <= 0:
            self.speedx = 2
            self.score2 +=1

        if keep[1] <=0:
            self.speedy = 2

        if keep[2] >=800:
            self.speedx = -2
            self.score1 +=1

        if keep[3]>= 400:
            self.speedy = -2



        
class Player():
    def __init__(self,x1,y1,x2,y2,colour):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.colour = colour
        self.movey = 0
        

    def draw(self):
       self.player = canvas.create_rectangle(self.x1,self.y1,self.x2,self.y2,fill= self.colour)


    def move(self):
        canvas.move(self.player,0,self.movey)
        keep = canvas.coords(self.player)
        if keep[1] <= 0:
            self.movey = 0

        if keep[3] >=400 :
            self.movey = 0

    def up(self,event):
        self.movey = -2

    def down(self,event):
        self.movey = 2
            
        


canvas = tkinter.Canvas(screen,background= "black",width= 800,height= 400)
canvas.create_line(400,0,400,400,fill= "white",width= 3)
canvas.create_oval(360,160,440,240,outline= "white",width= 3)


player1 = Player(10,170,30,270,"orange")
player1.draw()
canvas.bind_all("w",player1.up)


player2 = Player(790,170,770,270,"orange")
player2.draw()

canvas.pack()

ball = Ball()

running = True

while running:
    ball.movement()
    player1.move()
    player2.move()
    screen.update_idletasks()
    screen.update()
    time.sleep(0.005)

screen.mainloop()