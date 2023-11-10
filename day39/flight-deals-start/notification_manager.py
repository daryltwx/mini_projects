import smtplib


MY_EMAIL = "[EMAIL HERE]"
MY_PASSWORD = "[PASSWORD HERE]"
TO_EMAIL = "[EMAIL HERE]"



class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self, sender_email=MY_EMAIL, sender_password=MY_PASSWORD, recipient_email=TO_EMAIL, city, iata_code, flight_price):
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.recipient_email = recipient_email
        self.city = city
        self.iata_code = iata_code
        self.flight_price = flight_price


    def send_email(self):
        # Use email
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=self.sender_email, password=self.sender_password)
            connection.sendmail(from_addr=self.sender_email,
                                to_addrs=self.recipient_email,
                                msg=f"Subject: {iata_code} Flight Prices lowered.\n\n{city}, {iata_code} is at {flight_price}."
                                )
