import smtplib

my_email = "aboutdaryl@gmail.com"
password = "aerx pujl mani oouy"
to_email = "dryalnat@gmail.com"
message = "Subject: Hehe\n\nTest message using SMTP"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs=to_email,
                        msg=message
                        )
