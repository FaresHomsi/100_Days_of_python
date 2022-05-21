import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "Your Stock API Key"
NEWS_API_KEY = "Your News API Key"

TWILIO_ACCOUNT_SID = "Your Twilio Account SID"
TWILIO_AUTH_TOKEN = "Your Twilio API Key"

stock_params =  {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK_NAME,
    "apikey" : STOCK_API_KEY,
}

response = requests.get(url=STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
stock_data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in stock_data.items()]
yesterday_stock = data_list[0]
yesterday_closing_price = yesterday_stock["4. close"]

day_before_yesterday_stock = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_stock["4. close"]

difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = "↗️"
else:
    up_down = "↘️"

diff_percent = round((difference / float(yesterday_closing_price)) * 100 )

if abs(diff_percent) > 5:

    news_params = {
    "q" : COMPANY_NAME,
    "apiKey" : NEWS_API_KEY,
}

    news_response = requests.get(url=NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    articles = news_response.json()["articles"]
    three_articles = articles[:3]

    formatted_articles = [f"{STOCK_NAME}:  {up_down}  {abs(diff_percent)}% \
\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    for article in formatted_articles:
        message = client.messages \
                    .create(
                        body=article,
                        from_='Your Virtual Number',
                        to='+Your Actual Number'
                    )
        print(message.status)


