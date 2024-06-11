from turtle import Turtle, Screen

t = Turtle()
s = Screen()
distance = 10
angle = 10

def forward():
    t.fd(distance)

def reverse():
    t.bk(distance)

def anti_clock():
    t.setheading(t.heading()+angle)

def clock():
    t.setheading(t.heading()-angle)

def clear():
    t.setpos(0,0)
    t.clear()
    

s.listen()
s.onkey(key="w", fun=forward)
s.onkey(key="s", fun=reverse)
s.onkey(key="a", fun=anti_clock)
s.onkey(key="d", fun=clock)
s.onkey(key="c", fun=clear)
s.exitonclick()
