import cv2
import numpy as np
from config import PIXEL_TO_MM

def measure_object(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

    contours, _ = cv2.findContours(
        thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    if len(contours) == 0:
        return None, None, image

    largest_contour = max(contours, key=cv2.contourArea)

    x, y, w, h = cv2.boundingRect(largest_contour)

    width_mm = w * PIXEL_TO_MM
    height_mm = h * PIXEL_TO_MM

    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    return width_mm, height_mm, image