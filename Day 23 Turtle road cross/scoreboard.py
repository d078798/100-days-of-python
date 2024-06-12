from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        
        self.hideturtle()
        self.penup()
        self.setpos(0,270)
        self.color("black")
        self.score = 0
        self.write(self.score, font=('Arial', 22, 'normal'))
    
    def increasescore(self):
        self.score += 1
        self.clear()
        self.write(self.score,font=('Arial', 22, 'normal'))