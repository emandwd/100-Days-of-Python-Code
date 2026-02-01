import requests
from twilio.rest import Client
import os

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = os.environ.get("STOCK_ENDPOINT")
NEWS_ENDPOINT = os.environ.get("NEWS_ENDPOINT")

STOCK_API_KEY = os.environ.get("STOCK_API_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")

account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")


stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,

}
response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)

difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
up_down = None
if difference > 0:
    up_down = "⬆️"
else:
    up_down = "⬇️"

diff_percent = round((difference/float(yesterday_closing_price))*100, 2)
print(diff_percent)
if abs(diff_percent) > 1:
    news_params = {
        "apikey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]


    three_articles = articles[:3]
    print(three_articles)

    formatted_article = [f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadlines: {article ['title']}. \nBrief: {article ['description']}" for article in three_articles]

    client = Client(account_sid, auth_token)
    for article in formatted_article:
         message = client.messages.create(
                body = article,
                from_=os.environ.get("TWILIO_FROM"),
                to=os.environ.get("TWILIO_TO"),
            )


