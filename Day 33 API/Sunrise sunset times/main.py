import requests
import json
import datetime as dt
import smtplib

with open(r"C:\Users\d0787\Desktop\Pythonmail.txt") as f:
    lines = f.readlines()

gmail_pass = lines[1].split(":")[1]
outlook_pass = lines[2].split(":")[1]
my_gmail =      "d078798.codes@gmail.com"
my_outlook =    "d078798.codes@outlook.com"


MY_LAT = 52.408082
MY_LONG =-1.511966

website = "https://api.sunrise-sunset.org/json"
response = requests.get(f"{website}?lat={MY_LAT}&lng={MY_LONG}&formatted=0")
response.raise_for_status()
data = response.json()
print(data)
sunrise = (data["results"]["sunrise"].split("T")[1]).split(":")
sunset = (data["results"]["sunset"].split("T")[1]).split(":")
now = dt.datetime.now()
time = now.hour

iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
iss_response.raise_for_status()
iss_data = iss_response.json()
print(iss_data)
iss_position = iss_data["iss_position"]
longitude = float(iss_position["longitude"])
latitude = float(iss_position["latitude"])

# MY_LONG = longitude
# MY_LAT = latitude
# time = int(sunset[0])+4
# hours = now.hour
# mins = now.min
# sec = now.second
# time = now.time

print(time)


if int(sunset[0]) <= time or time <= int(sunrise[0]):
     if MY_LAT-1 <= latitude <= MY_LAT + 1 and MY_LONG-1<= longitude <= MY_LONG + 1:
        print("sending email")
        with smtplib.SMTP("smtp.gmail.com", 587, timeout=120) as smtp:
                    password = gmail_pass
                    smtp.starttls()
                    smtp.login(user=my_gmail,password=password)
                    smtp.sendmail(from_addr=my_gmail, 
                                to_addrs=my_outlook, 
                                msg=f"Subject:The ISS is currently overhead\n\nThe ISS is currently overhead at:\n Lat:{latitude}\nLong::{longitude}"
                                )
