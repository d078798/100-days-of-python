from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, player_number):
        super().__init__()
        self.player = player_number
        
        if self.player == 1:
            self.startpos = (350,0)
        elif self.player == 2:
            self.startpos = (-350,0)
        self.hideturtle()    
        self.penup()
        self.speed("fastest")
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=5,stretch_wid=1)
        self.setpos(self.startpos)
        self.setheading(90)
        self.showturtle()
    def move_up(self):
        if self.ycor() <= 250:
            self.forward(20)
    def move_down(self):
        if self.ycor() >= -250:
            self.backward(20)