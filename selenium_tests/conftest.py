import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import os

# ---- Fixture to initialize WebDriver ----
@pytest.fixture
def driver():
    # Chrome setup
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # comment this line if you want to see the browser
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    service = Service()  # Uses default ChromeDriver in PATH
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()



import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def setup():
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()

# ---- Pytest hook for screenshots on failure ----
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook to capture screenshot when test fails
    """
    outcome = yield
    rep = outcome.get_result()

    # Only act if the test has failed
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver")
        if driver:
            # Create folder if not exists
            screenshot_dir = os.path.join(os.getcwd(), "screenshots")
            os.makedirs(screenshot_dir, exist_ok=True)

            # Filename with timestamp
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            file_name = f"{item.name}_{timestamp}.png"
            destination_file = os.path.join(screenshot_dir, file_name)

            # Capture screenshot
            driver.save_screenshot(destination_file)
            print(f"\n📸 Screenshot saved to: {destination_file}")

            # Attach screenshot to pytest-html report (if plugin is used)
            if hasattr(item.config, "_html"):
                extra = getattr(rep, "extra", [])
                extra.append(pytest_html.extras.image(destination_file))
                rep.extra = extra


# ---- Add screenshot to HTML report automatically ----
def pytest_configure(config):
    global pytest_html
    pytest_html = config.pluginmanager.getplugin('html')
    if not os.path.exists("screenshots"):
        os.mkdir("screenshots")
"""from defect_logger import log_defect

if test_failed:
    log_defect(test_name, username, password, expected, actual, screenshot_path)
"""