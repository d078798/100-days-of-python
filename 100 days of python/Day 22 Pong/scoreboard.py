from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.p1_score = 0
        self.p2_score = 0
        self.p1_score_count = Turtle()
        self.p2_score_count = Turtle()
        
        
        self.p1_score_count.hideturtle()
        self.p1_score_count.penup()
        self.p1_score_count.color("white")
        self.p1_score_count.shapesize(stretch_len=5,stretch_wid=5)
        self.p1_score_count.setpos(50,250)
        self.p1_score_count.write(self.p1_score, font=('Arial', 22, 'normal'))
        
        
        self.p2_score_count.hideturtle()
        self.p2_score_count.penup()
        self.p2_score_count.color("white")
        self.p2_score_count.shapesize(stretch_len=5,stretch_wid=5)
        self.p2_score_count.setpos(-50,250)
        self.p2_score_count.write(self.p2_score, font=('Arial', 22, 'normal'))
        
    def p1_point(self):
        self.p1_score += 1
        self.p1_score_count.clear()
        self.p1_score_count.write(self.p1_score, font=('Arial', 22, 'normal'))
    
    def p2_point(self):
        self.p2_score += 1
        self.p2_score_count.clear()
        self.p2_score_count.write(self.p2_score, font=('Arial', 22, 'normal'))