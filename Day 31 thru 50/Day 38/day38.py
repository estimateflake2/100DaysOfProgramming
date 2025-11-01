# ===================== Challenge Project: Build an Exercise Tracking with Python and Google Sheets App
# =======================Introduction to Natural Language Processing

import requests
import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('NUTRITIONIX_API_KEY')
APP_ID = os.getenv('NUTRITIONIX_APP_ID')
if not APP_ID or not API_KEY:
    raise ValueError("Missing NUTRITIONIX_APP_ID or NUTRITIONIX_API_KEY in your .env file.")

url = f"https://trackapi.nutritionix.com/v2/search/item"
params = {"upc": "49000036756"}
nutri_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}
response = requests.get(url=url, json=params, headers=nutri_headers)
print (response.text)