#====================Final Project: Stock New Monitoring Project
import os

import requests
from dotenv import load_dotenv

url = "https://www.alphavantage.co/query"

load_dotenv()
alpha_vantage_key = os.getenv("ALPHA_VANTAGE")
stock_symbol = os.getenv("STOCK")
stock_company_name = os.getenv("COMPANY_NAME")
news_api_key = os.getenv("NEWS_API_ORG_KEY")

def get_news(company_name, api_key):
    url = "https://newsapi.org/v2/everything"
    num_articles = 3
    params = {
        "q": company_name,
        "sortBy": "publishedAt",
        "pageSize": num_articles,
        "apiKey": api_key,
        "language": "en"
    }
    response = requests.get(url,params)
    print (response.json())

def get_stocks(symbol:str, api_key:str)->tuple:
    url = "https://www.alphavantage.co/query"f"?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}"
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError(f"Error fetching data: HTTP {response.status_code}")
    else:
        data = response.json()
        quote = data['Global Quote']
        for key, value in quote.items():
            if "price" in key.lower():
                current_price = value
                print(f"{key}: {value}")
            if "previous close" in key.lower():
                previous_close = value
                print(f"{key}: {value}")
    return (current_price, previous_close)


stock_p = get_stocks("TSLA",alpha_vantage_key)
print (get_news(stock_company_name, news_api_key))