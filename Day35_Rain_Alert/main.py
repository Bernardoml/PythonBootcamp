import os
import requests
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = os.getenv("API_KEY")
ACCOUNT_SID = os.getenv("ACCOUNT_SID")
AUTH_TOKEN = os.getenv("AUTH_TOKEN")
TWILIO_NUMBER = os.getenv("TWILIO_NUMBER")
MY_NUMBER = os.getenv("MY_NUMBER")


weather_parameters = {
    "lat": -19.918180,
    "lon": -43.937050,
    "appid": API_KEY,
    # "exclude": "current, minutely, daily"
}

response = requests.get(OWM_Endpoint, params=weather_parameters)
response.raise_for_status()
weather_data = response.json()
# Getting the 06:00 till 18:00 data using slice
weather_slice = weather_data["list"][1:6]

will_rain = False

for three_hour_data in weather_slice:
    condition_code = three_hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an Umbrella",
        from_=TWILIO_NUMBER,
        to=MY_NUMBER
    )
