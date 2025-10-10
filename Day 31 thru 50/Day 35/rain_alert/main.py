

import os

import requests
from dotenv import load_dotenv
from twilio.rest import Client

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
        # "q": location,
        "lat": 29.771157,
        "lon": -95.352213,
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
        # "lat": latitude,
        # "lon": longitude,
        "lat": 6.524379,
        "lon": 3.379206,
        "cnt": 4,
        "appid": api_key
    }
    response = requests.get(url_5_days, params=params)
    response.raise_for_status()
    print (response.json())
    weather_data = response.json()['list']

    is_bad = False
    for index, weather  in enumerate(weather_data):
        weather_id = weather['weather'][0]['id']
        if weather_id < 700: is_bad = True

    if is_bad:
         print ('Bring an Umbrella')
    else:
         print ('Clear weather. have a great day!')
    # # first = items[1]['main']
    #
    # for index, weather  in enumerate(weather_data):
    #     data = weather['main']
        # print (f"Weather for day {index} is: {data}")

    # if response.status_code == 200:
    #     print("data is: ",response.json())
    # else:
    #     print("Error:", response.status_code, response.text)
get_5_days()
