# import smtplib
#
# my_email = "aboutdaryl@gmail.com"
# password = "aerx pujl mani oouy"
# to_email = "dryalnat@gmail.com"
# message = "Subject: Hehe\n\nTest message using SMTP"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs=to_email,
#                         msg=message
#                         )

import datetime as dt
import pandas as pd
import random
import smtplib

now = dt.datetime.now()
# year = now.year
# month = now.month
# date_of_birth = dt.datetime(year=, month=, day=, hour=)
day_of_week = now.weekday()
if day_of_week == 0:
    # send email

    def flatten_extend(list1):
        flat_list = []
        for row in list1:
            flat_list.extend(row)
        return flat_list

    df = pd.read_csv("quotes.txt")
    list1 = df.values.tolist()
    new_list = flatten_extend(list1)
    random_quote, name = random.choice(new_list).split("- ")


    my_email = "aboutdaryl@gmail.com"
    password = "aerx pujl mani oouy"
    to_email = "dryalnat@gmail.com"
    message = f"Subject: Monday Motivation\n\n{random_quote}\n\n\n{name}"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=to_email,
                            msg=message
                            )



