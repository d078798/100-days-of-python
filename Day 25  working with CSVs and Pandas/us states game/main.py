import pandas as pd
import turtle
from turtle import Turtle, Screen, textinput
from state_label import State
image = "Day 25  working with CSVs and Pandas\\us states game\\blank_states_img.gif"
data__path = r"Day 25  working with CSVs and Pandas\us states game\50_states.csv"
game_on = True
states_found = 0
screen = Screen()
screen.addshape(image)
bg_turtle = Turtle()
bg_turtle.shape(image)
# screen.bgpic(image)
# screen.setup(width=800,height=600)
screen.tracer(0)


state_turtles = []
states = pd.read_csv(data__path)
states_dict = states.to_dict()
#print(states_dict)

state_list = list(states_dict["state"].values())
print(state_list)
for i in range(len(state_list)):
    state_list[i] = state_list[i].lower()

for state in states_dict["state"].keys():
    state_name = (states_dict["state"][state])
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
    text_in = (textinput(f"{states_found}/50", "Enter State:")).lower()
    if text_in in state_list:
        for state in state_turtles:
            if (state.name).lower() == text_in.lower():
                state.show()
                states_found += 1
                if states_found == 50:
                    congrats = Turtle()
                    congrats.write("CONGRATULATIONS! You guessed all of the states!", font=("Arial",20),align="center")
                    
                
    
screen.exitonclick()