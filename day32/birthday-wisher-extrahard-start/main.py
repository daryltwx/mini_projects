##################### Extra Hard Starting Project ######################
import pandas as pd
import datetime as dt
import random
import smtplib

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
today_tuple = (now.month, now.day)

MY_EMAIL = "[EMAIL HERE]"
MY_PASSWORD = "[PASSWORD HERE]"
to_email = "[EMAIL HERE]"

data = pd.read_csv("birthdays.csv")
birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    file_path = f"/Users/Pandaphy/github/mini_projects/day32/birthday-wisher-extrahard-start/letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        updated_content = contents.replace("[NAME]", birthday_person["name"])
# 4. Send the letter generated in step 3 to that person's email address.
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=to_email,
                            msg=f"Subject: Happy Birthday!\n\n{updated_content}"
                            )




