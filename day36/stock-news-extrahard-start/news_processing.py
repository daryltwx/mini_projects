import requests
import smtplib
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


MY_EMAIL = "[EMAIL HERE]"
MY_PASSWORD = "[PASSWORD HERE]"
to_email = "[EMAIL HERE]"



## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# Getting stock details 
stock_response = requests.get(url=API_ENDPOINT, params=stock_parameters)
stock_data = stock_response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in stock_data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
diff_percent = (difference / float(yesterday_closing_price)) * 100

if diff_percent > 4: 
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
    articles = news_response.json()["articles"]
    three_articles = articles[:3]

    formatted_articles = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]


    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=to_email,
                            msg=f"Subject: {STOCK} changes in the past day. \n\n{formatted_articles}"
                            )


# process articles, there is a chance its > 2048 characters. 
news_response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
articles = news_response.json()["articles"][:3]["content"]



# ChatGPT to process the content of the news. 

CHATGPT_API_KEY = ""

from openai import OpenAI
client = OpenAI()


# There is a text limit of 2048 characters for CHATGPT.

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a data analyst with proficiency in reading data input and making well informed decisions. In addition to the initial role, you're also a literature expert in reading news to understand the sentiments of the chunk of information which would aid in your data analyst decision outcome."},
    {"role": "user", "content": "Using the following information, make an educated guess on the direction of the stock. Provide the answer with either 'up' or 'down' and nothing else. : {news}"},
  ]
)


