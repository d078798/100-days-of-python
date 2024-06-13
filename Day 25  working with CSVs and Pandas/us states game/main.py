import pandas as pd
from turtle import Turtle, Screen, textinput
from state_label import State
image = "Day 25  working with CSVs and Pandas\\us states game\\blank_states_img.gif"
data__path = r"Day 25  working with CSVs and Pandas\us states game\50_states.csv"
game_on = True
states_found = 0
screen = Screen()

screen.bgpic(image)
screen.setup(width=800,height=600)
screen.tracer(0)

score = Turtle()
score.hideturtle()
score.setpos(0,250)
score.write(f"{states_found}/50 States Found", font=("Arial",20),align="center")
state_turtles = []
states = pd.read_csv(data__path)
states_dict = states.to_dict()
print(states_dict)
for state in states_dict["state"].keys():
    state_name = states_dict["state"][state]
    print(state_name)
    x = states_dict["x"][state]
    print(x)
    y = states_dict["y"][state]
    print(y)
    new_state = State(state_name,x,y)

    state_turtles.append(new_state)


print(states)

while game_on:
    screen.update()
    text_in = textinput("", "Enter State:")
    if text_in in states_dict["state"].values():
        for state in state_turtles:
            if state.name == text_in:
                state.show()
                states_found += 1
                score.clear()
                score.write(f"{states_found}/50 States Found", font=("Arial",20),align="center")
    
screen.exitonclick()