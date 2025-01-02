from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up the WebDriver (assuming ChromeDriver is in your PATH)
driver = webdriver.Chrome()

driver.get("https://norvicstg.dolphin.com.np/login")

username_field = driver.find_element(By.ID, "email")
username_field.send_keys("shreeyashi")
pw_field = driver.find_element(By.ID, "password")
pw_field.send_keys("Nepal@123")

buttons = driver.find_elements(By.TAG_NAME, "button")

# Filter buttons to find the one with type="submit"
submit_button = next(
    button for button in buttons if button.get_attribute("type") == "submit"
)
submit_button.click()

driver.implicitly_wait(10)


dropdown = driver.find_element(By.CLASS_NAME, "dropdown-toggle")

dropdown.click()

first_li = driver.find_element(
    By.CSS_SELECTOR, "ul.dropdown-menu.dropdown-menu-default > li:first-child"
)
print("first_li", first_li)
print("first_li", first_li.text)

first_li.click()

driver.implicitly_wait(20)

time.sleep(10)
opd_adm = driver.find_elements(By.CSS_SELECTOR, "span.title")

opd_span = None

for span in opd_adm:
    if span.text == "OPD Administration":
        opd_span = span
        print(span.text)
        break
if opd_span:
    print("now clicking")
    opd_span.click()
    time.sleep(10)
    
    print("clicked")
else:
    print("not found")

time.sleep(10)
driver.implicitly_wait(20)

driver.quit()
