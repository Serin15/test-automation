from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")

driver.find_element(By.ID, "username").send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
time.sleep(2)
if "You logged into a secure area!" in driver.page_source:
    print("Correct login: Test passed!")
else:
    print("Correct login: Test failed.")

driver.get("https://the-internet.herokuapp.com/login")
driver.find_element(By.ID, "username").send_keys("invalidUser")
driver.find_element(By.ID, "password").send_keys("WrongPassword")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
time.sleep(2)
error_message = driver.find_element(By.ID, "flash").text
assert "Your username is invalid!" in error_message
print("Both incorrect username and password test: Test passed!")