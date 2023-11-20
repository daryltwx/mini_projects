import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3742281466&f_AL=true&keywords=Python%20Developer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true")

# Add delay
time.sleep(5)
# Click Sign in button.
sign_in_button = driver.find_element(By.XPATH, value="/html/body/div[1]/header/nav/div/a[2]")
sign_in_button.click()

# Log in linkedin account
time.sleep(3)
type_email = driver.find_element(By.ID, value="username")
type_email.send_keys("hello.tan@hotmail.com")
type_password = driver.find_element(By.ID, value="password")
type_password.send_keys("qawsedrf1" + Keys.ENTER)

time.sleep(3)
easy_apply = driver.find_element(By.CSS_SELECTOR, value='.jobs-s-apply button')
easy_apply.click()


# Full solution @ https://gist.github.com/TheMuellenator/3cc1fdb5f43db6c5d1dd8f773fa4b05c
