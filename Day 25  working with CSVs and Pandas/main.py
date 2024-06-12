import pandas as pd
import csv

# Using csv library

# temps = []

# with open("Day 25  working with CSVs and Pandas\weather_data.csv", "r") as f:
#     #csv_data = f.readlines()
#     #csv_data = f.read()
#     csv_data = csv.reader(f)
#     for row in csv_data:
#         print(row)
#         try:
#             temps.append(int(row[1]))
#         except ValueError:
#             pass
# print(csv_data)
# print(temps)

# Using Pandas Library


csv_data = pd.read_csv("Day 25  working with CSVs and Pandas\weather_data.csv")
# print(type(csv_data))
# print(f"{csv_data}\n")
# print(csv_data["temp"])
#print(type(csv_data["temp"]))

csv_dict = csv_data.to_dict()

#print(csv_dict)

temp_list = csv_data["temp"].to_list()
avg_temp = csv_data["temp"].mean()
max_tmp = csv_data["temp"].max()
# total = sum(temp_list)
# ave_temp = total/len(temp_list) 

# print(ave_temp)
# print(f"Average Temperature = {avg_temp} C")
# print(f'Maximum Temperature = {csv_data["temp"].max()} C')

# print(csv_data.day)

#to get the data in the row
# print(csv_data[csv_data.temp == max_tmp].day)
#challenge get mondays temp and convert it to farrenheit

monday = ((csv_data[csv_data["day"] == "Monday"].temp)* 1.8 ) + 32.

# print(monday)

data_dict = {
    "students" : ["aaa","bbb", "ccc"],
    "scores" : [1,2,3]
}

data_frame = pd.DataFrame(data_dict)
data_frame.to_csv("new_data.csv")
print(data_frame)