import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://tinder.com/")

# Add delay
time.sleep(5)
log_in_button = driver.find_element(By.XPATH, value='//*[@id="s-547617529"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
log_in_button.click()

time.sleep(5)
google_sign_in = driver.find_element(By.XPATH, value='//*[@id="container"]/div')
google_sign_in.click()
