from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()

driver.get("https://the-internet.herokuapp.com/checkboxes")

checkbox1 = driver.find_element(By.CSS_SELECTOR, "input[type='checkbox']")

if not checkbox1.is_selected():
    checkbox1.click()

assert checkbox1.is_selected()


