from turtle import Turtle
import os

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.score = 0
        self.highscore = 0
        
        self.cwd = "./Day 24 Files Directories and paths\Snake with highscore"
        if os.path.isfile(f"{self.cwd}/highscore.txt"):
            with open(f"{self.cwd}/highscore.txt", "r") as f:
                self.highscore = int(f.read())
        else:
            with open(f"{self.cwd}/highscore.txt", "w") as f:
                f.write("0")
        
        self.write(f"Score: {self.score}\t Highscore = {self.highscore}", align="center",font=('Arial', 22, 'normal'))
        # self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}\t Highscore = {self.highscore}", align="center",font=('Arial', 22, 'normal'))
        
        
    def gameover(self):
        self.clear()
        self.goto(0,0)
        if self.score > self.highscore:
            self.highscore = self.score
            self.write(f"Congratulations you beat the High Score\n your Score: {self.score}", align="center",font=('Arial', 22, 'normal'))
            with open(f"{self.cwd}/highscore.txt", "w") as f:
                f.write(str(self.highscore))
        else:
            self.write(f"Gameover your Score: {self.score}", align="center",font=('Arial', 22, 'normal'))
        
        