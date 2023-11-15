from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

# article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")

# To click on a link
# article_count.click()

# Find links by text inbetween the anchor tag.
# all_portals = driver.find_element(By.LINK_TEXT, "More featured articles")
# all_portals.click()


# Type something into the text box.
# search = driver.find_element(By.NAME, "search")
# search.send_keys("Python" + Keys.ENTER)

# Challenge: Fill up a form
first_name = driver.find_element(By.NAME, value="fName")
first_name.send_keys("dryal")
last_name = driver.find_element(By.NAME, value="lName")
last_name.send_keys("nat")
email_address = driver.find_element(By.NAME, value="email")
email_address.send_keys("dryalnat@gmail.com")

submit = driver.find_element(By.CSS_SELECTOR, "form button")
submit.click()

# driver.quit()