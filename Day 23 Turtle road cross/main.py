from turtle import Screen, Turtle
from player import Player
from car import Car
from scoreboard import Scoreboard
import time


screen = Screen()
screen.tracer(0)
screen.listen()
screen.setup(width=600,height=600)
screen.colormode(255)
player = Player()
starting_x = -300
starting_y = -230
car_list = []
level = 1
scoreboard = Scoreboard()

def create_cars():
    cars_to_create = 10
    for i in range(cars_to_create):
        car = Car()
        car_list.append(car)


for i in range(8):
    divider = Turtle()
    divider.penup()
    divider.pensize(5)
    divider.setpos(starting_x, starting_y + (i*65))
    while divider.xcor() < 300:
        if i == 0 or i == 3 or i == 4 or i == 7:
            divider.pendown()
            divider.forward(20)
            divider.penup()
        else:
            divider.pendown()
            divider.forward(20)
            divider.penup()
            divider.forward(20)
            

screen.onkeypress(player.moveUp, "Up")
screen.onkeypress(player.moveDown, "Down")

game_on = True
create_cars()

while game_on:
    
    time.sleep(player.speed)
    screen.update()
    for car in car_list:
        if car.xcor() < -300:
            car.newpos()
        car.move()
        if car.distance(player) < 25:
            game_on = False
            print("gameover")
    
    if player.ycor() > 300:
        player.increaseSpeed()
        player.resetpos()
        for i in range(2):
            car = Car()
            car_list.append(car)
        scoreboard.increasescore()
    

screen.exitonclick()

