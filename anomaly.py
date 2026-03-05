import cv2
import numpy as np

def detect_anomaly(image_path):
    image = cv2.imread(image_path)

    if image is None:
        return None, None

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Blur to remove noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Edge detection
    edges = cv2.Canny(blurred, 50, 150)

    # Find contours
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    anomaly_count = 0

    for contour in contours:
        area = cv2.contourArea(contour)

        # Filter small noise
        if area > 300:
            anomaly_count += 1
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 2)

    if anomaly_count > 0:
        anomaly_status = "DEFECT DETECTED"
    else:
        anomaly_status = "NO DEFECT"

    return anomaly_status, image