import pytest
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from defect_logger import log_defect


@pytest.mark.usefixtures("setup")
class TestLoginDataDriven:
    def test_login_multiple_cases(self, setup):
        """
        Data-driven test for login functionality using multiple sets of credentials.
        """

        driver = setup
        driver.get("https://practicetestautomation.com/practice-test-login/")

        screenshots_dir = "screenshots"
        os.makedirs(screenshots_dir, exist_ok=True)

        # Step 1: Define test data (username, password, expected_result)
        test_data = [
            ("student", "Password123", "https://practicetestautomation.com/logged-in-successfully/"),  # ✅ valid
            ("student", "wrongpassword", "Your password is invalid!"),  # ❌ invalid password
            ("wronguser", "Password123", "Your username is invalid!"),  # ❌ invalid username
            ("", "Password123", "Your username is invalid!"),  # ❌ empty username (site returns same invalid msg)
            ("student", "", "Your password is invalid!"),  # ❌ empty password
        ]

        for i, (username, password, expected) in enumerate(test_data, start=1):
            print(f"\n🔹 Running Test Case {i}: username='{username}', password='{password}'")

            # Step 2: Reload the page for each test
            driver.get("https://practicetestautomation.com/practice-test-login/")

            # Step 3: Enter credentials
            driver.find_element(By.ID, "username").clear()
            driver.find_element(By.ID, "password").clear()
            driver.find_element(By.ID, "username").send_keys(username)
            driver.find_element(By.ID, "password").send_keys(password)
            driver.find_element(By.ID, "submit").click()

            # Create unique screenshot name
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            screenshot_path = os.path.join(screenshots_dir, f"test_case_{i}_{timestamp}.png")

            try:
                # Wait for page or message
                WebDriverWait(driver, 5).until(
                    EC.any_of(
                        EC.url_contains("logged-in-successfully"),
                        EC.visibility_of_element_located((By.ID, "error"))
                    )
                )

                current_url = driver.current_url
                if "logged-in-successfully" in current_url:
                    assert expected in current_url, f"❌ Expected redirect to {expected}, got {current_url}"
                    print(f"✅ Test Case {i}: Passed (Valid login)")
                else:
                    error_msg = driver.find_element(By.ID, "error").text.strip()
                    assert error_msg == expected, f"❌ Expected '{expected}', got '{error_msg}'"
                    print(f"✅ Test Case {i}: Passed (Error message matched)")

            except AssertionError as e:
                driver.save_screenshot(screenshot_path)
                log_defect(
                    test_name=f"test_case_{i}_login",
                    error_message=str(e),
                    screenshot=screenshot_path
                )
                print(f"❌ Test Case {i}: Failed — Defect logged")
                raise e

            except Exception as ex:
                driver.save_screenshot(screenshot_path)
                log_defect(
                    test_name=f"test_case_{i}_login",
                    error_message=f"Unexpected error: {str(ex)}",
                    screenshot=screenshot_path
                )
                raise ex
