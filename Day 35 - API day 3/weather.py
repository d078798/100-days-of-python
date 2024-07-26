import requests
import json
import os
import certifi
from twilio.rest import Client

certifi.where()

with open(r"C:\Users\denglis2\API Keys.json","r") as f:
    api_keys = json.load(f)
    
twilio_sid = api_keys["twilio_sid"]
twilio_token = api_keys["twilio_token"]
my_phone = api_keys["myphone"]
    
# print(api_keys)
api_key = api_keys["OpenWeather"]
# print(api_key)
city_name = "Coventry,UK"
# api_address = f" https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
api_address = f"https://api.openweathermap.org/data/2.5/forecast"
weather_params = {
    "q" : city_name,
    "appid" : api_key,
    "cnt" : 4
}
weather = requests.get(api_address,params=weather_params,verify=False)
weather.raise_for_status()
weaather_data = weather.json()
rain = False

for item in weaather_data["list"]:
    if item["weather"][0]["id"] < 700:
        raintime = item["dt_txt"].split(" ")[1]
        print(f"Bring Umbrella as it will rain at {raintime}")
        rain = True
    else:
        raintime = item["dt_txt"].split(" ")[1]
        print(f"No umbrella needed at {raintime}")
        
if rain:
    client = Client(twilio_sid,twilio_token)
    
    message = client.messages.create(
        body="It is going to rain today, remember to bring an umbrella",
        from_= "+15088024519",
        to= my_phone
    )
    print(message.status)