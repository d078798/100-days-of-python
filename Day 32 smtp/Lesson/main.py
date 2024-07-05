# smtp.gmail.com
# smtplib.SMTP("smtp.gmail.com", port=587)
import smtplib
import datetime as dt
import random
with open(r"C:\Users\d0787\Desktop\Pythonmail.txt") as f:
    lines = f.readlines()

gmail_pass = lines[1].split(":")[1]
outlook_pass = lines[2].split(":")[1]

# print(gmail_pass)
# print(outlook_pass)

my_gmail =      "d078798.codes@gmail.com"
my_outlook =    "d078798.codes@outlook.com"

    
# with smtplib.SMTP("smtp.outlook.com", 587, timeout=120) as smtp:
#     password = outlook_pass
#     smtp.starttls()
#     smtp.login(user=my_outlook,password=password)
#     smtp.sendmail(from_addr=my_outlook, to_addrs="d078798.codes@gmail.com", 
#                         msg="Subject:Hello\n\nThis is the Body of my email"
#                     )

with open("Day 32 smtp\Lesson\quotes.txt","r") as f:
    quotes = f.readlines()

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
weekday = now.weekday()
print(weekday)

if weekday == 4:
    quote = random.choice(quotes)
    with smtplib.SMTP("smtp.gmail.com", 587, timeout=120) as smtp:
        password = gmail_pass
        smtp.starttls()
        smtp.login(user=my_gmail,password=password)
        smtp.sendmail(from_addr=my_gmail, 
                      to_addrs="d078798.codes@outlook.com", 
                      msg=f"Subject:Todays Quote\n\n{quote}"
                    )