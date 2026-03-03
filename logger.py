import csv
import os
from config import CSV_FILE

def save_result(width, height, result):
    file_exists = os.path.isfile(CSV_FILE)

    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["Width (mm)", "Height (mm)", "Result"])

        writer.writerow([width, height, result])