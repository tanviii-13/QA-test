from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
try:
    # Open login page
    driver.get("https://auth.segwise.ai/en/login")

    # Enter test credentials
    driver.find_element(By.ID, "email").send_keys("qa@segwise.ai")
    driver.find_element(By.ID, "password").send_keys("segwise_test")
    driver.find_element(By.CLASS_NAME, "radius").click()

    # Wait and verify dashboard
    time.sleep(2)
    assert "/secure" in driver.current_url, "Login failed or dashboard not reached"

    # Check for metric (success message)
    message = driver.find_element(By.CLASS_NAME, "flash").text
    assert "You logged into a secure area!" in message

    print("✅ Test Passed: Dashboard element found")

except Exception as e:
    print("❌ Test Failed:", e)

finally:
    time.sleep(2)
    driver.quit()