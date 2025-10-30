
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import time

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")  # Uncomment to run without opening browser
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_valid_login(driver):
    url = "https://practicetestautomation.com/practice-test-login/"
    driver.get(url)

    # Perform login
    driver.find_element(By.ID, "username").send_keys("student")
    driver.find_element(By.ID, "password").send_keys("Password123")
    driver.find_element(By.ID, "submit").click()

    # Wait for page to load
    time.sleep(2)

    # Assertion
    expected_url = "https://practicetestautomation.com/logged-in-successfully/"
    assert driver.current_url == expected_url, f"Expected {expected_url}, got {driver.current_url}"

    print("\n✅ Test Passed: Valid login successful")