from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://the-internet.herokuapp.com/")
driver.maximize_window()
driver.implicitly_wait(2)

driver.find_element(By.LINK_TEXT, "Add/Remove Elements").click()

add_element = driver.find_element(By.XPATH, "//button[text()='Add Element']").is_displayed()
assert add_element, "The 'Add Element' button is not visible"
print("Test 1: 'Add Element' is visible")

driver.find_element(By.XPATH, "//button[text()='Add Element']").click()
delete_button = driver.find_element(By.CSS_SELECTOR, ".added-manually").is_displayed()
assert delete_button, "No Delete button added"
print("Test 2: 'Delete' button added")

driver.find_element(By.CLASS_NAME, "added-manually").click()
delete_buttons = driver.find_elements(By.CLASS_NAME, "added-manually")
assert len(delete_buttons) == 0
print("Test 3: The 'Delete' button was successfully deleted.")

driver.quit()