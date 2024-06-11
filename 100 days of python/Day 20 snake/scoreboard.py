from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.score = 0
        self.write(f"Score: {self.score}", align="center",font=('Arial', 22, 'normal'))
        # self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align="center",font=('Arial', 22, 'normal'))
        
        
    def gameover(self):
        self.clear()
        self.goto(0,0)
        self.write(f"Gameover your Score: {self.score}", align="center",font=('Arial', 22, 'normal'))
        