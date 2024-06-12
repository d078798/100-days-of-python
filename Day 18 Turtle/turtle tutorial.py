# draw triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, decagon

from turtle import Turtle, Screen
import random
import colorgram


# t.shape("turtle")
# t.color("green")
# t.pen

# for i in range(50):
#     if i%2 == 0:
#        t.pendown()
#     else:
#         t.penup()
#     t.forward(10)

# shape_sides = [3,4,5,6,7,8,9,10]
# side_length = 100

# for shape in shape_sides:
#     angle = 360/shape
#     r = random.randrange(0,255)
#     g = random.randrange(0,255) 
#     b = random.randrange(0,255)
#     t.pencolor(r,g,b)
#     for _ in range(shape):
#         t.forward(side_length)
#         t.right(angle)


# t.pensize(10)
# t.speed(100)
# directions = [0,90,180,270]

# while True:
#     t.pencolor0(random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))
#     new_dir = random.choice(directions)
#     t.setheading(new_dir)
#     if new_dir == 0:
#         print(t.pos()[0])
#         if t.pos()[0] + 50 < 500:
#             t.forward(50)
#     elif new_dir == 180:
#         if t.pos()[0] - 50 > -500:
#             t.forward(50)
#     elif new_dir == 90:
#         if t.pos()[1] + 50 < 500:
#             t.forward(50)
#     elif new_dir == 270:
#         if t.pos()[1] - 50 > -500:
#             t.forward(50)      

# draw circles with radius 100 with adjustable angle
# angle = 5
# radius = 100
# current_angle = t.heading()
# t.speed(100)
# while current_angle <= 360:
#     t.pencolor(random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))  
#     t.circle(radius)
#     current_angle += angle
#     t.setheading(current_angle)

screen = Screen()
screen.colormode(255)
x=1000
y=1000
screen.setup(x,y)
t = Turtle()

# colours = colorgram.extract("jpg_44-2.jpg", 30)
# colours_rgb = []
# for col in colours:
#     rgb = col.rgb
#     r = rgb[0]
#     g = rgb[1]
#     b = rgb[2]
#     rbg = (r,b,g)
#     colours_rgb.append(rbg)

# print(colours_rgb)

colours = [(47, 21, 15), (117, 91, 79), (46, 21, 27), (153, 30, 72), (217, 114, 147), (137, 37, 16), (251, 165, 205), (15, 53, 29), (183, 139, 135), (166, 113, 105), (254, 95, 200), (189, 81, 98), (234, 156, 174), (105, 34, 47), (70, 120, 89), (28, 39, 45), (246, 4, 139), (68, 79, 87), (48, 64, 73), (119, 4, 55), (42, 93, 60), (237, 229, 225), (224, 
169, 166), (145, 160, 143), (121, 145, 119), (233, 238, 233), (252, 0, 194), (148, 152, 154), (235, 238, 240), (48, 74, 68)]

# 10 x 10 rows of spote, size 20, 50 paces apart
dot_size = 20
distance = 10
rows = 50
cols = 10
t.hideturtle()

t.penup()
t.speed("fastest")
y = -300
x = -500
t.setpos(x, y)

for _ in range(rows):
    for _ in range(cols):
        t.dot(dot_size, random.choice(colours))
        t.forward(distance)
    y += distance
    t.setpos(x , y)
screen.exitonclick()