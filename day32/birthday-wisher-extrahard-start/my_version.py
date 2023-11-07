##################### Extra Hard Starting Project ######################
import pandas as pd
import datetime as dt
import random
import smtplib

# 1. Update the birthdays.csv
df = pd.read_csv("birthdays.csv")
dict1 = df.to_dict(orient="records")

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
to_day = now.day
to_month = now.month

MY_EMAIL = "[EMAIL HERE]"
MY_PASSWORD = "[PASSWORD HERE]"
to_email = "[EMAIL HERE]"

print(now.date, now.month, now.year)

for _ in range(len(dict1)):
    if dict1[_]["month"] == to_month and dict1[_]["day"] == to_day:
        print(dict1[_]["email"])


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        def random_letter():
            if random.randint(1,3) == 1:
                return "letter_1.txt"
            elif random.randint(1,3) == 2:
                return "letter_2.txt"
            else:
                return "letter_3.txt"

        with open(f"/Users/Pandaphy/github/mini_projects/day32/birthday-wisher-extrahard-start/letter_templates/{random_letter()}") as file:
            lines = file.read()
            updated_content = lines.replace("[NAME]", f"{dict1[_]['name']}")


# 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=to_email,
                                msg=f"Subject: Happy Birthday!\n\n{updated_content}"
                                )



