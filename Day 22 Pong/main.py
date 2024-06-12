from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
import keyboard

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong")
screen.bgcolor("black")
screen.tracer(0)
#setting up divider
divider = Turtle()
divider.speed("fastest")
divider.hideturtle()
divider.color("white")
divider.penup()
divider.setpos(0,-300)
divider.setheading(90)
while divider.ycor() < 300:
    divider.pendown()
    divider.forward(20)
    divider.penup()
    divider.forward(20)

game_is_on = True
p1 = Paddle(1)
p2 = Paddle(2)
ball = Ball()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(p1.move_up, "Up")
screen.onkey(p1.move_down, "Down")
screen.onkey(p2.move_up, "w")
screen.onkey(p2.move_down, "s")

START_NEW = False

# paddle_left = Paddle("left")
# paddle_right = Paddle("right")
# ball = Ball()
# scoreboard = Scoreboard()
def new_round(last_scorer):
    if last_scorer == "p1":
        ball.setpos(0,0)
        ball.resetspeed() 
        ball.vx *= 1
        
    else:
        ball.setpos(0,0)
        ball.resetspeed() 
        ball.vx *= -1
        
         

def start_new_round():
    global START_NEW
    
    if START_NEW == False:
        START_NEW = True
    else:
        START_NEW = False

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce("wall")
    
    #detect collision with right paddle
    if (ball.distance(p1) < 50 and ball.xcor() > 320) or (ball.distance(p2) < 50 and ball.xcor() < -320):
        ball.bounce("paddle")

    if ball.xcor() > 340:
        #p2 wins
        scoreboard.p2_point()
        new_round("p1")
        
    if ball.xcor() < -340:
        #p1 wins
        scoreboard.p1_point()
       #ball.setpos(0,0)
        new_round("p2")

screen.exitonclick()
