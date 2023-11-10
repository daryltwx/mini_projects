import requests
from datetime import datetime, timedelta, date
from newsapi import NewsApiClient

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

NEWS_API_KEY = "cb24834fa44b46deb84e1de3dd07be20"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

news_parameters = {
    "q": COMPANY_NAME,
    "apikey": NEWS_API_KEY,
}


FUNCTION = "TIME_SERIES_DAILY"
API_ENDPOINT = "https://www.alphavantage.co/query"
API_KEY = "demo"

stock_parameters = {
    "function": FUNCTION,
    "symbol": STOCK,
    "apikey": API_KEY,
}

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").


# Getting today's date
date, time = datetime.now().split(" ")

today = date.today()
yesterday = today - timedelta(days=1)
day_before_yesterday = today - timedelta(days=2)


# Getting stock details 
stock_response = requests.get(url=API_ENDPOINT, params=stock_parameters)
stock_data = stock_response.json()
# Date format from API is eg: "2023-11-08"
yesterday_closing_price = stock_data["Time Series"][yesterday]["4 close"]
day_before_yesterday_closing_price = stock_data["Time Series"][day_before_yesterday]["4. close"]
percentage_change_in_stock_prices = round(((yesterday_closing_price - day_before_yesterday_closing_price)/day_before_yesterday_closing_price)*100)

if percentage_change_in_stock_prices >= 5:
    print("Get News")



## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
news_response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
news_data = news_response.json()
news_slice = news_data["articles"][:3]

# Loops 3 times then?
for days_data in news_slice:
    news_title = days_data["source"]["title"]
    news_url = days_data["source"]["url"]

news_dict = {days_data["source"]["title"]: days_data["source"]["url"] for days_data in news_slice}


# Format
# {stock}
# 


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

