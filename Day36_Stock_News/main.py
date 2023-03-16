import os
import requests
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

AA_Endpoint = "https://www.alphavantage.co/query"
AA_API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")
AA_Params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "interval": "5min",
    "apikey": AA_API_KEY,

}

NEWS_Endpoint = "https://newsapi.org/v2/everything"
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
NEWS_Params = {
    "qInTitle": COMPANY_NAME,
    "apiKey": NEWS_API_KEY,
}

TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_NUMBER = os.getenv("TWILIO_NUMBER")
MY_NUMBER = os.getenv("MY_NUMBER")

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
response = requests.get(AA_Endpoint, params=AA_Params)
response.raise_for_status()
stock_data = response.json()["Time Series (Daily)"]

# turning into a list with each day as a value
stock_data_list = [value for (key, value) in stock_data.items()]
yesterday_data = stock_data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

day_before_yesterday_data = stock_data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

# Get the difference between the stock closing from the last 2 days
difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

diff_percent = round((abs(difference) / float(yesterday_closing_price)) * 100)

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
if diff_percent > 1:
    response = requests.get(NEWS_Endpoint, params=NEWS_Params)
    response.raise_for_status()
    news_data = response.json()["articles"]
    three_articles = news_data[:3]

    # Create a new list of the first 3 article's headlines and description using list comprehension
    formatted_articles_list = [
        f"{STOCK}: {up_down}{diff_percent}% \nHeadline: {article['title']}. \nBrief: {article['description']}" for
        article in
        three_articles]

    ## STEP 3: Use https://www.twilio.com
    # Send a separate message with the percentage change and each article's title and description to your phone number.
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    for article in formatted_articles_list:
        message = client.messages.create(
            body=article,
            from_=TWILIO_NUMBER,
            to=MY_NUMBER
        )
