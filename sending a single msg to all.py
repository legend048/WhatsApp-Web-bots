from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Message to be sent 
message = "Hello!"

# Path to your WebDriver
driver_path = '/path/to/chromedriver'
driver = webdriver.Chrome(driver_path)
driver.get("https://web.whatsapp.com")
print("Scan QR Code and press Enter")
input("Press Enter after scanning QR code")  # Wait for your QR scan
try:
    contacts = driver.find_elements(By.CSS_SELECTOR, '._3OvU8 ._21S-L')
    for contact in contacts:
        contact.click()
        time.sleep(1)

        message_box = driver.find_element(By.CSS_SELECTOR, 'div[title="Type a message"]')
        message_box.click()
        message_box.send_keys(message + Keys.ENTER) 

        time.sleep(1)

finally:
    print("Messages sent. Closing the driver.")
    driver.quit()
