import requests
import smtplib
import os
from datetime import datetime, timedelta

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

def adjust_to_weekday(date):
    if date.weekday() == 6:  # Sunday
        return date - timedelta(days=2)
    elif date.weekday() == 5:  # Saturday
        return date - timedelta(days=1)
    return date

api_key_stocks = os.environ.get('API_KEY_STOCKS')
api_key_news = os.environ.get('API_KEY_NEWS')
my_email = os.environ.get('MY_EMAIL')
password = os.environ.get('PASSWORD')

# Stock API Key
stocks_data = requests.get(f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK_NAME}&apikey={api_key_stocks}")
stocks_data.raise_for_status()
stocks_data_json = stocks_data.json()

# Adjust dates for weekdays
today = datetime.now()
yesterday = adjust_to_weekday(today - timedelta(days=1))
before_yesterday = adjust_to_weekday(today - timedelta(days=2))
yesterday_str = yesterday.strftime("%Y-%m-%d")
before_yesterday_str = before_yesterday.strftime("%Y-%m-%d")

# Get stock data
try:
    yesterday_data = stocks_data_json["Time Series (Daily)"].get(yesterday_str)
    before_yesterday_data = stocks_data_json["Time Series (Daily)"].get(before_yesterday_str)

    if not yesterday_data or not before_yesterday_data:
        raise KeyError("Dados de fechamento não disponíveis para as datas especificadas.")

    yesterday_closed_at = float(yesterday_data["4. close"])
    before_yesterday_closed_at = float(before_yesterday_data["4. close"])

    percentage_variation = ((yesterday_closed_at - before_yesterday_closed_at) / before_yesterday_closed_at) * 100

    if percentage_variation > 5:
        stocks = f"The stock increased by 🔺{percentage_variation:.2f}%"
    elif percentage_variation < -5:
        stocks = f"The stock decreased by 🔻{abs(percentage_variation):.2f}%"
    else:
        stocks = f"No significant change."

except KeyError as e:
    print(f"Erro ao acessar os dados de fechamento: {e}")
    exit()

# News API Key
news_from_date = yesterday.strftime("%Y-%m-%d")
news_data = requests.get(f"https://newsapi.org/v2/everything?qInTitle={STOCK_NAME}&from={news_from_date}&sortBy=publishedAt&apiKey={api_key_news}")
news_data.raise_for_status()
news_data_json = news_data.json()

# Extract top 3 news articles
news_list = []
for article in news_data_json['articles'][:3]:
    news_list.append({
        "Title": article['title'],
        "Description": article['description'],
        "URL": article['url'],
        "Published At": article['publishedAt']
    })

# Email setup
msg = f"Subject: Tesla Stocks and Latest News\n\nTesla stocks: \n\n{stocks}\n\nLatest News:\n\n"
for i, news in enumerate(news_list, 1):
    msg += f"{i}. {news['Title']}\n{news['Description']}\n{news['URL']}\n\n"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=msg.encode("utf-8"))

print("Email sent successfully!")
