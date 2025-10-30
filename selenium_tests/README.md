🧪 Automated Login Testing with Selenium
📌 Project Overview
This project automates login functionality testing using Selenium with Python and Pytest.
It verifies both valid and invalid login attempts on a web application and captures screenshots of failures.
Each test result is logged in:

✅ HTML Report → report.html
⚠️ Defect Log → defects_log.csv
📸 Screenshots Folder → /screenshots


Install selenium
pip install selenium
Install Python 3.10+ (if not installed).

Install pip packages:

cd QA_Login_Test/selenium_tests
python -m venv venv
# Activate virtualenv:
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

pip install selenium pytest webdriver-manager

📁 Project Structure
F:\QA_Login_Test\
│
├── selenium_tests/
│   ├── test_login_valid.py
│   ├── test_login_invalid.py
│   ├── conftest.py
│   ├── defect_logger.py
│   ├── screenshots/           ✅ keep screenshots here
│   ├── report.html            ✅ main report
│
├── defects_log.csv            ✅ shows logged defect
└── README.md



⚙️ Prerequisites
Before running, make sure you have the following installed:
🔧 Software
Python 3.8 or later
Google Chrome Browser
ChromeDriver (auto-installed by webdriver_manager)

📦 Python Libraries
Install required dependencies: OPEN CMD
     pip install -r requirements.txt

If requirements.txt is missing, create it with the following content:
selenium
pytest
pytest-html
webdriver-manager


▶️ How to Run the Tests
1️⃣ Run All Tests
In your project folder, run:
pytest confest.py --html=report.html --self-contained-html

This command:
Executes all test cases
Generates a detailed HTML report
Saves the report as report.html in your project directory

2️⃣ View the Report
After the run, open:
report.html
in any browser to view test results.


📸 Screenshot Capture Logic
Screenshots are auto-captured on every failed test.
Files are named with timestamps like:
test_invalid_login_20251030_203012.png
They are stored in the /screenshots folder for easy review.



🧾 Logging Defects
If a test fails, it automatically logs details in defects_log.csv:
Test CaseUsernamePasswordExpected ResultActual ResultTimestampInvalid LoginstudentwrongpasswordInvalid username or passwordLogin success page2025-10-30 20:35:00

🧰 Example Run Summary
After test execution:
Report: report.html
Defects logged in: defects_log.csv
Screenshots saved in: /screenshots



🧑‍💻 Author
Aisha Vel Tech, Chennai
B.E Computer Science Engineering
Project: Automated Web Login Testing using Selenium and Pytest