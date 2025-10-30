# 🧪 Automated Login Testing with Selenium

## 📌 Project Overview
This project automates **login functionality testing** using **Selenium with Python and Pytest**.  
It verifies both **valid** and **invalid** login scenarios on a sample web application and automatically:

- ✅ Generates an **HTML test report**  
- ⚠️ Logs defects into a **CSV file**  
- 📸 Captures screenshots of failed test cases  

---

## 🧰 Features
- Automated functional testing of login page  
- Validation of both correct and incorrect credentials  
- Screenshot capture for failed tests  
- Defect logging (timestamp, expected vs actual result)  
- HTML report generation with test results summary  

---

## ⚙️ Prerequisites

Before running the project, ensure the following are installed:

### 🔧 Software
- Python **3.8+**
- Google Chrome Browser
- ChromeDriver (auto-managed via `webdriver_manager`)

### 🧩 Python Libraries
Install the required packages by running:

```bash
pip install -r requirements.txt


qa_project
├── selenium_tests/
│   ├── test_login_valid.py          # Valid login test
│   ├── test_login_invalid.py        # Invalid login test
│   ├── conftest.py                  # Pytest configuration and setup
│   ├── defect_logger.py             # Logs failed test details
│   ├── screenshots/                 # Stores screenshots of failed tests
│   ├── report.html                  # Generated HTML report
│   ├── defects_log.csv              # Logged defect details
│
└── README.md                        # Project documentation


Step 1: Create & Activate Virtual Environment
cd selenium_tests
python -m venv venv


Activate the environment:
Windows: venv\Scripts\activate
macOS/Linux: source venv/bin/activate

Step 2: Install Dependencies
pip install selenium pytest pytest-html webdriver-manager

Execute Tests
Run all tests and generate the HTML report:
pytest conftest.py --html=report.html --self-contained-html

This command:
Runs all test cases
Generates a detailed HTML report
Saves it as report.html in the project directory
Captures screenshots automatically when any test fails

Step 4: View Results
After execution:
📄 Report: Open report.html in any browser
⚠️ Defects: Check defects_log.csv
📸 Screenshots: Found in /screenshots folder

🧑‍💻 Author
M.RAM KUMAR
B.Tech. Computer Science Engineering
Vel Tech, Chennai

📘 Project: Automated Web Login Testing using Selenium and Pytest
