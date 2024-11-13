from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
driver.maximize_window()
driver.implicitly_wait(2)

message = driver.find_element(By.XPATH, "//p[contains(text(),'Congratulations! You must have the proper credentials.')]").text
assert "Congratulations! You must have the proper credentials." in message
print("Basic Auth authentication test passed successfully.")
