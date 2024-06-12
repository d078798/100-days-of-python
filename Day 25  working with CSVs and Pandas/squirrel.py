import pandas as pd 

squirrel_data = pd.read_csv("Day 25  working with CSVs and Pandas\\2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

print(squirrel_data["Primary Fur Color"])
gray = squirrel_data["Primary Fur Color"].value_counts()["Gray"]
black = squirrel_data["Primary Fur Color"].value_counts()["Black"]
red = squirrel_data["Primary Fur Color"].value_counts()["Cinnamon"]

print(f"Gray = {gray}\nBlack = {black}\nred = {red}")
#create csv for squirrel count by fur count: Primary Fur Collumn Gray =Gray, Red = Cinnamon, Black = Black
squirrel_dict = {
    "colour" : ["Gray", "Black", "Red"],
    "quantity" : [gray, black, red]
}



data_frame = pd.DataFrame(squirrel_dict)
data_frame.to_csv("Day 25  working with CSVs and Pandas\\squirrel_colour_quantity.csv")