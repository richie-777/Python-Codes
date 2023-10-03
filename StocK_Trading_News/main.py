import requests
from newsapi import NewsApiClient
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API = "Stock_API_KEY"
NEWS_API = "NEW_API_KEY"

TWILIO_SID = "Twilio_SID"
TWILIO_AUTH_TOKEN = "TWILIO_AUTH_TOKEN_KEY"


stock_params = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK_NAME,
    'apikey': STOCK_API,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
stock_data = response.json()["Time Series (Daily)"]
stock_data_list = [value for (key, value) in stock_data.items()]
yesterday_data = stock_data_list[0]
yesterday_closing_price = yesterday_data['4. close']
# print(yesterday_data)
print(yesterday_closing_price)

day_before_yesterday_data = stock_data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data['4. close']
# print(day_before_yesterday_data)
print(day_before_yesterday_closing_price)

difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

diff_percent = round((difference / float(yesterday_closing_price)) * 100)
print(diff_percent)

if abs(diff_percent) > 1:
    news_params = {
        'apikey': NEWS_API,
        'qInTitle': COMPANY_NAME,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    news_data = news_response.json()['articles']
    # print(news_data)

new_news_data = news_data[:3]
# print(new_news_data[0])

final_news = [f'{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article["title"]}. \nBrief: {article["description"]}\nMore: {article["url"]}' for article in new_news_data]
# print(final_news[1])
#
client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
for article in final_news:
    message = client.messages \
        .create(
        body=article,
        from_='From Number',
        to= "+Your Number"
    )


