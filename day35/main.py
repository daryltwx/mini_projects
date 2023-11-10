import requests
# from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/weather"
MY_LAT = 1.352083
MY_LONG = 103.819839
API_KEY = "Your_API_Key_here"
# account_sid = "Your_account_sid_here"
# auth_token = "Your_auth_token_here"


PARAMETERS = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    # The API Angela is using is a paid version now.
    # "exclude": "current,minutely,daily"
}

response = requests.get(url=OWM_Endpoint, params=PARAMETERS)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) <= 700:
        will_rain = True

if will_rain:
    print("Bring umbrella")
    ## client = Client(account_sid, auth_token)
    # message = client.messages \ .create(
    #     body="It's going to rain today. Remember to bring an umbrella.",
    #     from="Twilo number here",
    #     to="Recipent's number here",
    # )
    # print(message.status)


### My Attempt.
# def bring_umbrella():
#     for _ in range(0, 12):
#         if weather_data["hourly"][_]["weather"][0]["id"] <= 700:
#             return True
#
# bring_umbrella()




## Environment Variable

"""
In Terminal, type..

# Make sure there is no spaces.
export [API_KEY_NAME]=[API_KEY]
eg:
export AUTH_TOKEN=123412341234


--
To use the env var..

import os

api_key = os.environ.get("[NAME_BEFORE THE EQUAL SIGN]")
eg.
api_key = os.environ.get("AUTH_TOKEN")



To run the script:

Need to run the key before the main file:

export KEY; export KEY; python3 main.py

"""
