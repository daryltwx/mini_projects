from selenium import webdriver
from selenium.webdriver.common.by import By


# Keep chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
price_cents =driver.find_element(By.CLASS_NAME, value="a-price-fraction")
print(f"The price is {price_dollar.text}.{price_cents.text}")

# Search by CSS, if there isn't any identifable way to find.
# documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(documentation_link.text

# If there isn't a way to find, use XPath.
bug_link = driver.find_element(By.XPATH, value='//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[1]/span[2]/span[2]')
print(bug_link.text)

#button = driver.find_element(By.ID, value="submit")



# Close the active tab
# driver.close()

# Quit the entire browser
driver.quit()