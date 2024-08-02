STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

import requests
import json
import os
import datetime
import smtplib

with open(r"C:\Users\denglis2\API Keys.json","r") as f:
    api_keys = json.load(f)
# with open(r"C:\Users\d0787\Desktop\Pythonmail.txt") as f:
#     lines = f.readlines()

# gmail_pass = lines[1].split(":")[1]
# outlook_pass = lines[2].split(":")[1]
    
def get_news():
    news_api = "https://newsapi.org/v2/everything?"
    news_params = {
        "q" : STOCK,
        "sortBy":"popularity",
        "apiKey": api_keys["stock_news"],
    }
    news_response = requests.get(news_api, params=news_params, verify=False)
    news_data = news_response.json()
    article_1 = news_data["articles"][1]
    article_1_title = article_1["title"]
    article_1_desc = article_1["description"]
    
    article_2 = news_data["articles"][2]
    article_2_title = article_2["title"]
    article_2_desc = article_2["description"]
    
    article_3 = news_data["articles"][3]
    article_3_title = article_3["title"]
    article_3_desc = article_3["description"]
    
    print(f"Title : {article_1_title}\nBrief : {article_1_desc}")
    print(f"Title : {article_2_title}\nBrief : {article_2_desc}")
    print(f"Title : {article_3_title}\nBrief : {article_3_desc}")
    news = {
        "article_1" : {
            "title" : article_1_title,
            "desc" : article_1_desc
        },
        "article_2" : {
            "title" : article_2_title,
            "desc" : article_2_desc
        },
        "article_3" : {
            "title" : article_3_title,
            "desc" : article_3_desc
        },
    }
    return news
    
    
    
stock_api = r"https://www.alphavantage.co/query?"
stock_parameters = {
    "function" : "TIME_SERIES_DAILY",
    "symbol": f"{STOCK}.LON",
    "outputsize" :"full",
    "apikey" : api_keys["stock_api"]
    }

stock_data = requests.get(stock_api, params=stock_parameters,verify=False)
stock_data.raise_for_status()
stock_data_json = stock_data.json()

stock_value = []

date = datetime.datetime.today().strftime('%Y-%m-%d')

yesterday =  (datetime.datetime.today() - datetime.timedelta(days=(1))).strftime('%Y-%m-%d')
yesterday_1 = (datetime.datetime.today() - datetime.timedelta(days=(2))).strftime('%Y-%m-%d')
yesterday_val = float(stock_data_json["Time Series (Daily)"][yesterday]["4. close"])
yesterday_1_val = float(stock_data_json["Time Series (Daily)"][yesterday_1]["4. close"])
print(f"Yesterday = {yesterday} Value = {yesterday_val}")
print(f"Yesterday-1 = {yesterday_1} Value = {yesterday_1_val}")

percentage = (yesterday_val/yesterday_1_val)*100-100
print(percentage)
if percentage > 1 or percentage < -1:
    news = get_news()
    message = []
    if percentage > 0:
        arrow = "^"
    else:
        arrow = "v"
    message.append(f"{STOCK} {arrow}{percentage}%\n")
    for item in news.keys():
        news_message = f"Headline: {news[item]['title']}\nBrief: {news[item]['desc']}\n"
        message.append(news_message)
    message = "".join(message)
    print(message)
    my_email = "d078798.codes@gmail.com"
    connection = smtplib.SMTP("smtp.gmail.com",587,timeout=120)
    password = gmail_pass
    connection.starttls()
    connection.login(user=my_email,password=password)
    connection.sendmail(from_addr=my_email, to_addrs="d078798.codes@outlook.com", msg=message)
    connection.close()