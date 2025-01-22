from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up the WebDriver (assuming ChromeDriver is in your PATH)
driver = webdriver.Chrome()

# Navigate to Google's homepage
driver.get("https://www.google.com")

# Find the search box using the name attribute
search_box = driver.find_element(By.NAME, "q")

# Type in "Selenium WebDriver" and hit ENTER
search_box.send_keys("Selenium WebDriver")
search_box.send_keys(Keys.RETURN)

# Wait for a few seconds to see the results
time.sleep(5)
# Close the browser
driver.quit()
