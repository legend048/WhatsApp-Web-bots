from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Message to reply
reply_message = "Thanks!"

# Path to your WebDriver (replace with your actual path)
driver_path = '/path/to/chromedriver'
driver = webdriver.Chrome(driver_path)
driver.get("https://web.whatsapp.com")
print("Scan QR Code and press Enter")
input("Press Enter after scanning QR code")  # Wait for your QR scan

try:
    # Infinite loop to continuously check for new messages
    while True:
        unread_chats = driver.find_elements(By.CSS_SELECTOR, 'span[aria-label="Unread message"]')
        
        for chat in unread_chats:
            chat.click()
            time.sleep(1)
          
            messages = driver.find_elements(By.CSS_SELECTOR, 'span.selectable-text')
            for message in messages:
                if "happy birthday" in message.text.lower():
                    # If in a group, reply to that specific message
                    try:
                        message.click()  # Click the specific message to reply
                        reply_box = driver.find_element(By.CSS_SELECTOR, 'div[title="Type a message"]')
                        reply_box.send_keys(reply_message + Keys.ENTER)
                    except Exception:
                        # If not clickable, it may be a single chat; just send thanks
                        reply_box = driver.find_element(By.CSS_SELECTOR, 'div[title="Type a message"]')
                        reply_box.send_keys(reply_message + Keys.ENTER)
                    time.sleep(1)
                    
        time.sleep(10)

finally:
    print("Closing the driver.")
    driver.quit()
