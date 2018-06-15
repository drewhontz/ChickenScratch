from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys
import time

SLEEP_TIME = 3

# Log in element ids
site_url = "https://www.chase.com"
username_id = "userId-input-field"
password_id = "password-input-field"

username_key = input("Please enter username")
password_key = input("Please enter password")

driver = Firefox()
time.sleep(SLEEP_TIME)

driver.get(site_url)

time.sleep(SLEEP_TIME)
driver.switch_to.frame(0)  # switch context to iframe

username = driver.find_element_by_id(username_id)
password = driver.find_element_by_id(password_id)
sign_in_button = driver.find_element_by_id("signin-button")

username.send_keys(username_key)
password.send_keys(password_key)
sign_in_button.click()

time.sleep(SLEEP_TIME)
time.sleep(SLEEP_TIME)
time.sleep(SLEEP_TIME)
time.sleep(SLEEP_TIME)
time.sleep(SLEEP_TIME)
time.sleep(SLEEP_TIME)
# Transactions element ids
transaction_id = "creditCardTransTable"

transactions = driver.find_element_by_id(transaction_id)
print(transactions)