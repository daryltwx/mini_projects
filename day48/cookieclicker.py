import time
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/cookieclicker/")

# Add lag to load language select page.
time.sleep(3)
# Click on language title name.
language_selector = driver.find_element(By.ID, value="langSelect-EN")
language_selector.click()
print("Language select successful\n---Line break---\n")

# Add lag to load page
time.sleep(3)

# Get list of product price
items = driver.find_elements(By.CSS_SELECTOR, value="#store div .price")
upgrade_list = [item.text for item in items]

# Time setup
timeout = time.time() + 5 # 5 seconds from now
five_minutes = time.time() + 60*5 # 5 minutes from now


# Click cookie
cookie_button = driver.find_element(By.ID, value="bigCookie")

while True:
    cookie_button.click()

