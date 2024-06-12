from turtle import Screen, Turtle
import keyboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
snake_list = []
last_direction = []
last_direction.append("right")
last_direction.append("right")
last_direction.append("right")

segment_count = 0
game_is_on = True

class snake_segment():
    global game_is_on
    def __init__(self,segment_number, starting_position):
        self.segment = Turtle("square")
        self.segment.color("white")
        self.segment.speed(2)
        self.segment.penup()
        self.starting_pos = starting_position
        self.segment_number = segment_number
        self.segment_multiplier = segment_number
        self.x = list(starting_position)[0]
        self.y = list(starting_position)[1]
        
        self.segment.setpos(self.x,self.y)
        self.current_direction = ""
        self.new_direction = ""
    
    def move(self, direction):
        if direction == "up":
            self.y += 20
        elif direction == "down":
            self.y += -20
        elif direction == "left":
            self.x += -20
        elif direction == "right":
            self.x += 20
        
        self.update_pos()
        
    def update_pos(self):
        self.segment.setpos(self.x,self.y)
    
    def checkpos(self):
        global game_is_on
        current_position = self.segment.pos()
        if current_position[0] > 300 or current_position[0] < -300:
            game_is_on = False
        if current_position[1] > 300 or current_position[1] < -300:
            game_is_on = False
        
        return game_is_on


class food_turtle():
    def __init__(self):
        
        self.food = Turtle("circle")
        self.food.color("gold")
        self.food.hideturtle
        self.food.penup()
        self.x = 0
        self.y = 0
        
    def new_position(self):
        new_x = random.randrange(-300,300)
        new_y = random.randrange(-300,300)
        self.food.setpos(new_x,new_y) 
        self.food.showturtle
starting_pos = [(0,0), (-20,0), (-40,0)]
for i in range(3):
    segment = i + 1
    segment_count += 1
    new_segment = snake_segment(i, starting_pos[i])
    snake_list.append(new_segment)

food = food_turtle()
food.new_position()

while game_is_on:
    if keyboard.is_pressed("up"):
        if last_direction[0] != "down":
            last_direction.insert(0, "up")
    elif keyboard.is_pressed("down"):
        if last_direction[0] != "up":
            last_direction.insert(0, "down")
    elif keyboard.is_pressed("left"):
        if last_direction[0] != "right":
            last_direction.insert(0, "left")
    elif keyboard.is_pressed("right"):
        if last_direction[0] != "left":
            last_direction.insert(0, "right")
    else:
        last_direction.insert(0, last_direction[0])
        
        
    for segment in snake_list:
        segment.move(last_direction[0+segment.segment_number])
        if segment == snake_list[0]:
            status = segment.checkpos()
        if not game_is_on:
            break
    snake_pos = snake_list[0].segment.pos()
    food_pos = food.food.pos()
    if food_pos[0] - 10 <= snake_pos[0] <= food_pos[0] + 10 and \
    food_pos[1] - 10 <= snake_pos[1] <= food_pos[1] + 10:
        food.new_position()
        segment_count += 1
        last_segment_pos = snake_list[-1].segment.pos()
        x = list(last_segment_pos)[0]
        y = list(last_segment_pos)[1]
        if last_direction[0+segment_count-1] == "left":
            x += 20
        elif last_direction[0+segment_count-1] == "right":
            x-= 20
        elif last_direction[0+segment_count-1] == "up":
            y-= 20
        elif last_direction[0+segment_count-1] == "down":
            y+= 20
        pos_tuple = (x,y)
            
        new_segment = snake_segment(segment_count+1,pos_tuple)
        snake_list.append(new_segment)


screen.exitonclick()