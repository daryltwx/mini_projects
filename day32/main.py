import datetime as dt
import pandas as pd
import random
import smtplib


MY_EMAIL = "aboutdaryl@gmail.com"
MY_PASSWORD = "aerx pujl mani oouy"
to_email = "dryalnat@gmail.com"

now = dt.datetime.now()
day_of_week = now.weekday()
if day_of_week == 0:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=to_email,
                            msg=f"Subject: Monday Motivation\n\n{quote}"
                            )



