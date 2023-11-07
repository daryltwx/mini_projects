import requests
import smtplib
from datetime import datetime
import time

MY_LAT = 1.3521
MY_LONG = 103.8198

MY_EMAIL = "[EMAIL HERE]"
MY_PASSWORD = "[PASSWORD HERE]"
to_email = "[EMAIL HERE]"

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    if float(MY_LAT-5) <= iss_latitude <= float(MY_LAT+5) and float(MY_LONG-5) <= iss_longitude <= float(MY_LONG+5):
        return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }


    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    now_hour = time_now.hour

    if now_hour >= sunset and now_hour <= sunrise:
        return True

#If the ISS is close to my current position

# and it is currently dark

while True:
# Then send me an email to tell me to look up.
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=to_email,
                                msg=f"Subject: Lookup!\n\nISS is above you!"
                                )
# BONUS: run the code every 60 seconds.



