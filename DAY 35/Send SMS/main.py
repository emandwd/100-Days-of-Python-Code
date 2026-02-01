import os
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

OWM_Endpoint = os.environ.get("OWM_ENDPOINT")
api_key = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

weather_params = {
    "lat": os.environ.get("LAT"),
    "lon": os.environ.get("LON"),
    "appid" : api_key,
    "cnt" : 6,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
# print(weather_data["list"][0]["weather"][0]["id"])

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ.get('HTTPS_PROXY')}
    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_=os.environ.get("TWILIO_FROM"),
        to=os.environ.get("TWILIO_TO")
    )
    print(message.status)
