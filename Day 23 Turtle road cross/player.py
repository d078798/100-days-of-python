from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.setpos(0,-280)
        self.setheading(90)
        self.speed = 0.2
        
    def moveUp(self):
        y = self.ycor()
        new_y = y + 10
        self.goto(0,new_y)

    def moveDown(self):
        y = self.ycor()
        new_y = y - 10
        if y >= -280:
            self.goto(0,new_y)
        
    def increaseSpeed(self):
        self.speed -= 0.01
        if self.speed <= 0:
            self.speed = 0.01
    
    def resetpos(self):
        self.setpos(0,-280)