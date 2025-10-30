import pytest
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from defect_logger import log_defect

@pytest.mark.usefixtures("setup")
class TestInvalidLogin:
    def test_invalid_login(self, setup):
        driver = setup
        driver.get("https://practicetestautomation.com/practice-test-login/")

        screenshots_dir = "screenshots"
        os.makedirs(screenshots_dir, exist_ok=True)
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        screenshot_path = os.path.join(screenshots_dir, f"test_invalid_login_{timestamp}.png")

        # Step 1: Enter invalid credentials
        driver.find_element(By.ID, "username").send_keys("wronguser")
        driver.find_element(By.ID, "password").send_keys("wrongpass")
        driver.find_element(By.ID, "submit").click()

        try:
            wait = WebDriverWait(driver, 10)
            error_element = wait.until(EC.visibility_of_element_located((By.ID, "error")))
            error_message = error_element.text.strip()

            assert error_message == "Your username is invalid!", \
            f"❌ Defect: Expected 'Your username is invalid!', got '{error_message}'"


            print("\n✅ Test Passed: Proper error message displayed.")

        except AssertionError as e:
            time.sleep(1)
            driver.save_screenshot(screenshot_path)
            log_defect("test_invalid_login", str(e), screenshot_path)
            print("\n❌ Test Failed: Defect logged.")
            raise e

        except Exception as ex:
            time.sleep(1)
            driver.save_screenshot(screenshot_path)
            log_defect("test_invalid_login", f"Unexpected error: {str(ex)}", screenshot_path)
            raise ex