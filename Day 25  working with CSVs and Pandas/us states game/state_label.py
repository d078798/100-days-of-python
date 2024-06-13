from turtle import Turtle

class State(Turtle):
    def __init__(self,state_name,x,y):
        super().__init__()
        self.name = state_name
        self.x = x
        self.y = y
        self.hideturtle()
        self.penup()
        
        
    
    def show(self):
        self.showturtle()
        self.goto(self.x,self.y)
        self.write(self.name, font=("Arial",10))