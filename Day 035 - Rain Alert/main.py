import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

account_sid = "ACa05cc819782529a0781f09857b40c0c0"
auth_token = os.environ.get("OWM_AUTH_TOKEN")
phone_number = os.environ.get("PHONE_NUMBER")

parameters = {
    "lat":37.871660,
    "lon":32.498960,
    "appid":os.environ.get("OWM_API_KEY"),
    "exclude":"current,minutely,daily"
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = int(hour_data["weather"][0]["id"])
    if condition_code < 700:
        will_rain = True

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {"https": os.environ["https_proxy"]}

    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
                .create(
                     body="it`s going to rain today. Remeber to bring an ☔",
                     from_='+17755264434',
                     to=phone_number
                 )
    print(message.status)

