import random
#new_dict = {new_key:new_value for item in list}
#new_dict = {new_key:new_value for (key,value) in dict.items() if test}

names = ["Alex", "Beth", "Caroline", "Dave", "Freddie", "Elanor"]

new_dict = {name:random.randint(0,100) for name in names}
print(new_dict)

passed_students = {key:value for (key,value) in new_dict.items() if value >= 70}
print(passed_students)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# 🚨 Don't change code above 👆
# Write your code below 👇
word_list = sentence.split(" ")
word_dict = {word:len(word) for word in word_list}


print(word_dict)




weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
# 🚨 Don't change code above 👆


# Write your code 👇 below:
weather_f = {day:(val*9/5)+32 for (day,val) in weather_c.items()}


print(weather_f)