import time

from select import select
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://the-internet.herokuapp.com/dropdown")
driver.maximize_window()
driver.implicitly_wait(2)

dropdown = driver.find_element(By.ID, "dropdown")

select = Select(dropdown)

values = ['1', '2']
for value in values:
    select.select_by_value(value)
    assert select.first_selected_option.get_attribute('value') == value
    print(f"The option with the value '{value}' was selected correctly.")
    time.sleep(1)
driver.quit()
