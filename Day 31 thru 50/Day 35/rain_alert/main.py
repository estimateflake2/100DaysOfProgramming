
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

# Twilio Data
twilio_account_sid = os.getenv("TWILIO_ACCOUNT_SID")
twilio_auth_token = os.getenv("TWILIO_AUTH_TOKEN")
twilio_from_number = os.getenv("TWILIO_FROM_NUMBER")
twilio_to_number = os.getenv("TWILIO_TO_NUMBER")
twilio_service_sid = os.getenv("TWILIO_SERVICE_SID")



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
         "lat": latitude,
         "lon": longitude,
        #"lat": 6.524379,
        #"lon": 3.379206,
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
         # client = Client(twilio_account_sid, twilio_auth_token)
         # message = client.messages.create(
         #     from_= twilio_from_number,
         #     body='test',
         #     to= twilio_to_number
         # )
         # print(message.status)
         # message = client.messages.create(
         #     from_='whatsapp:+14155238886',
         #     content_sid='HXb5b62575e6e4ff6129ad7c8efe1f983e',
         #     content_variables='{"1":"12/1","2":"3pm"}',
         #     to='whatsapp:+12103243158'
         # )

    else:
         print ('Clear weather. have a great day!')


get_5_days()
