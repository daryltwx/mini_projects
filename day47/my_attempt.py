import requests
import lxml
import smtplib
import time
from bs4 import BeautifulSoup

amazon_item_url = "https://www.amazon.sg/KeyForge-Archons-Archon-Display-Decks/dp/B07G5M55NY/ref=sr_1_12?crid=35VSXU4EXBRL5&keywords=keyforge&qid=1699918566&sprefix=keyforg%2Caps%2C283&sr=8-12"
MY_EMAIL = "[EMAIL HERE]"
MY_PASSWORD = "[PASSWORD HERE]"
TO_EMAIL = "[EMAIL HERE]"

# Get amazon product name and price
headers = {
    "accept_language": "en-US,en;q=0.9",
    "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
}
amazon_response = requests.get(url=amazon_item_url, headers=headers)
amazon_html = amazon_response.text

soup = BeautifulSoup(amazon_html, "lxml")
item_name = soup.find(id="productTitle", class_="a-size-large product-title-word-break").text.strip()

item_price = soup.find(name="span", class_="a-offscreen").text.split("S$")[1]
price_as_float = float(item_price)

preset_price = 100.00

while True:
    time.sleep(10000)
    if price_as_float <= preset_price:
        # Send email alert when price is lowered
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=TO_EMAIL,
                                msg=f"Subject: {item_name} Prices lowered.\n\nPrices has went below your preset price of {preset_price}.\n\n URL {amazon_item_url}."
                                )