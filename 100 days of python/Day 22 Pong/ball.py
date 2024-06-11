from turtle import Turtle

SPEED = 10

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_len=1,stretch_wid=1)
        #self.showturtle()
        #elf.setheading(0)
        self.penup()
        self.newspeed = SPEED
        self.vx = SPEED
        self.vy = SPEED
        
    def resetspeed(self):
        self.vx = SPEED
        self.vy = SPEED
    
    def start(self):
        self.move()
    
    def move(self):
        #self.forward(10)
        new_x = self.xcor() + self.vx
        new_y = self.ycor() + self.vy
        
        
        self.goto(new_x,new_y)
        
    def bounce(self, obj):
        
        if obj == "wall":
            self.vy *= -1
        elif obj == "paddle":
            self.vx *= -1
            if self.vx < 0:
                self.vx -= 1
            else:
                self.vx += 1
            if self.vy < 0:
                self.vy -= 1
            else:
                self.vy += 1
          
                
            
        