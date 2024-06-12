from turtle import Turtle, Screen
import random
s = Screen()
class new_turtle():
    def __init__(self, speed, colour, start_pos):
        self.t = Turtle()
        self.t.shape("turtle")
        self.t.penup()
        self.speed = speed 
        self.colour = colour
        self.t.color(self.colour)
        self.start_pos = start_pos
        self.t.setpos(start_pos)
    
    def move(self):
        self.t.pendown()
        self.t.forward(self.speed)
        old_speed = self.speed
        self.speed = random.randrange(10,50,10)
        print(f"{self.colour} speed {old_speed} -> {self.speed}")
f = Turtle()
f.penup()
f.setpos(200,0)
f.pendown()
f.setpos(200,-300)
f.penup()
f.hideturtle()



colours = ["black", "blue", "green", "red", "yellow", "orange", "purple", "cyan"]
x = -400
y = -200

user_guess = input("Enter the colour of the turtle you want to win: ").lower()
black = new_turtle(random.randrange(10,50), "black", (x,-200))
blue = new_turtle(random.randrange(10,50), "blue", (x,-180))
green = new_turtle(random.randrange(10,50), "green", (x,-160))
red = new_turtle(random.randrange(10,50), "red", (x,-140))
yellow = new_turtle(random.randrange(10,50), "yellow", (x,-120))
orange = new_turtle(random.randrange(10,50), "orange", (x,-100))
purple = new_turtle(random.randrange(10,50), "purple", (x,-80))
cyan = new_turtle(random.randrange(10,50), "cyan", (x,-60))
end = True
winner = ""

while end:
    black.move()
    if black.t.pos()[0] >= 200:
        end = False
        winner = "black"
        break
            
    blue.move()
    if blue.t.pos()[0] >= 200:
        end = False
        winner = "blue"
        break
    green.move()
    if green.t.pos()[0] >= 200:
        end = False
        winner = "green"
        break
    red.move()
    if red.t.pos()[0] >= 200:
        end = False
        winner = "red"
        break
    yellow.move()
    if yellow.t.pos()[0] >= 200:
        end = False
        winner = "yellow"
        break
    orange.move()
    if orange.t.pos()[0] >= 200:
        end = False
        winner = "orange"
        break
    purple.move()
    if purple.t.pos()[0] >= 200:
        end = False
        winner = "purple"
        break
    cyan.move()
    if cyan.t.pos()[0] >= 200:
        end = False
        winner = "cyan"
        break
    
    

print(f"Winner = {winner}")
if user_guess == winner:
    print("you win")
s.exitonclick()