##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.



import datetime as dt
import pandas as pd
import random
import smtplib
import os
with open(r"C:\Users\d0787\Desktop\Pythonmail.txt") as f:
    lines = f.readlines()

gmail_pass = lines[1].split(":")[1]
outlook_pass = lines[2].split(":")[1]

# print(gmail_pass)
# print(outlook_pass)

my_gmail =      "d078798.codes@gmail.com"
my_outlook =    "d078798.codes@outlook.com"



birthday_file = r"Day 32 smtp\Birthday project\birthdays.csv"
#with open("Day 32 smtp\Birthday project\birthdays.csv","r") as birthdays:
bd_data_frame = pd.read_csv(birthday_file)

print(bd_data_frame)
# bd_data_frame.loc[2] = ["gmail","d0788798.codes@gmail.com",2000,1,10]
# bd_data_frame.loc[3] = ["outlook", "d078798.codes@outlook.com",2000,7,5]

bd_data_frame.to_csv(birthday_file)



now = dt.datetime.now()
day = now.day
month = now.month
year = now.year
letters = os.listdir("Day 32 smtp\Birthday project\letter_templates")
print(letters)
for index in bd_data_frame.index:
    print(index)
    if bd_data_frame._get_value(index,"day") == day:
        if bd_data_frame._get_value(index,"month") == month:
            letter_template = random.choice(letters)
            with open(f"Day 32 smtp\Birthday project\letter_templates\{letter_template}","r") as f:
                letter = f.read()

            letter = letter.replace("[NAME]", bd_data_frame._get_value(index,"name"))
            with smtplib.SMTP("smtp.gmail.com", 587, timeout=120) as smtp:
                password = gmail_pass
                smtp.starttls()
                smtp.login(user=my_gmail,password=password)
                smtp.sendmail(from_addr=my_gmail, 
                            to_addrs=bd_data_frame._get_value(index,"email"), 
                            msg=f"Subject:Happy Birthday\n\n{letter}"
                            )