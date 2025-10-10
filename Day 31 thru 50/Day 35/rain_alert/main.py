# api_key = "759d4498e3428e9709c033efdb7aa198"
# # https://api.openweathermap.org/geo/1.0/direct?q=London,UK&limit=10&appid=759d4498e3428e9709c033efdb7aa198

from dotenv import load_dotenv
import os
import requests

# Load variables from .env file
load_dotenv()

# Retrieve API key
api_key = os.getenv("OPENWEATHER_API_KEY")

# Base URL
url = "https://api.openweathermap.org/geo/1.0/direct"
location = os.getenv("LOCATION")

def get_city_state_weather():
    # Parameters
    params = {
        "q": location,
        "limit": 10,
        "appid": api_key
    }

    # Make API request
    response = requests.get(url, params=params)

    # Check and print results
    if response.status_code == 200:
        print("data is: ",response.json())
    else:
        print("Error:", response.status_code, response.text)

# get_city_state_weather()

#============================================================================================================
import requests

def get_current_location():
    try:
        response = requests.get("https://ipinfo.io/json")
        data = response.json()
        loc = data.get("loc", None)
        if loc:
            lat, lon = loc.split(",")
            return float(lat), float(lon)
        else:
            print("Location not found.")
    except Exception as e:
        print("Error:", e)
def get_5_days():
    latitude, longitude = get_current_location()
    url_5_days = "https://api.openweathermap.org/data/2.5/forecast"
    params = {
        "lat": latitude,
        "lon": longitude,
        "appid": api_key
    }
    response = requests.get(url_5_days, params=params)
    items = response.json()['list']
    first = items[1]['main']
    for index, weather  in enumerate(items):
        data = weather['main']
        print (f"Weather for day {index} is: {data}")

    # if response.status_code == 200:
    #     print("data is: ",response.json())
    # else:
    #     print("Error:", response.status_code, response.text)
get_5_days()
