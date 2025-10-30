import csv
import os
from datetime import datetime


def log_defect(test_name, error_message, screenshot_path):
    """
    Logs failed test details into defect_report.csv
    """
    file_name = "defect_report.csv"
    file_exists = os.path.isfile(file_name)

    with open(file_name, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        # Write header only once (if file doesn't exist)
        if not file_exists:
            writer.writerow(["Timestamp", "Test Name", "Error Message", "Screenshot Path"])

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            test_name,
            error_message,
            screenshot_path
        ])
