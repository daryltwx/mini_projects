import requests
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

# Getting data from webpage.
response = requests.get("https://appbrewery.github.io/Zillow-Clone/")
zillow_webpage = response.text

soup = BeautifulSoup(zillow_webpage, "html.parser")
prices = soup.find_all(class_="PropertyCardWrapper")
rental_prices = [price.text.replace("/mo", "").strip() for price in prices]

addresses = soup.find_all(name="address")
address_names = [address.text.strip() for address in addresses]

urls = soup.find_all(name=["a", "href"], class_="StyledPropertyCardDataArea-anchor")
link_list = [url.get("href") for url in urls]

for i in range(len(rental_prices)):
# Selenium to input to forms
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://forms.gle/CX79usbPtNWBtP5Z6")


    # Delay to load page.
    time.sleep(3) # 3 seconds

    # input boxes.
    address = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address.send_keys(f"{address_names[i]}")
    price = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price.send_keys(f"{rental_prices[i]}")
    link = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link.send_keys(f"{link_list[i]}")

    # Press button.
    submit_button = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
    submit_button.click()

    time.sleep(2)

    driver.quit()