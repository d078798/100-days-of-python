from turtle import Turtle
import random

class Car(Turtle):
    def __init__(self):
        super().__init__()
        
        self.penup()
        self.randspeed = random.randrange(10,20,1)
        self.speed = self.randspeed
        rand_start = random.randint(1, 100)
        self.startx = random.randrange(300,1000, rand_start)
        self.lanes = [-197,-132, -67, 62, 127,192]
        self.starty = random.choice(self.lanes) 
        self.shape("square")
        self.shapesize(stretch_wid=1.5,stretch_len=3)
        #self.colormode(255)
        self.color(self.randomColor())
        self.setheading(180)
        
        
        
    def randomColor(self):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        
        rgb = (r,g,b)
        
        return rgb
    
    def move(self):
        self.forward(self.speed)
        
    def newpos(self):
        rand_start = random.randint(1, 100)
        self.startx = random.randrange(300,1000,rand_start)
        self.lanes = [-197,-132, -67, 62, 127,192]
        self.starty = random.choice(self.lanes) 
        self.setpos(self.startx,self.starty)
        self.speed = random.randrange(10,20,1)