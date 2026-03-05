import cv2
import numpy as np

def detect_anomaly(image_path):

    image = cv2.imread(image_path)

    if image is None:
        return "IMAGE ERROR", None, 0

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Improve contrast
    gray = cv2.equalizeHist(gray)

    # Detect edges (scratches)
    edges = cv2.Canny(gray, 30, 120)

    # Morphological filtering
    kernel = np.ones((3,3), np.uint8)
    edges = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)

    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    heatmap = image.copy()

    defect_detected = False
    defect_area = 0

    for cnt in contours:

        area = cv2.contourArea(cnt)

        if area > 100:  # threshold for scratches

            defect_detected = True
            defect_area += area

            x,y,w,h = cv2.boundingRect(cnt)

            cv2.rectangle(heatmap,(x,y),(x+w,y+h),(0,0,255),2)

    total_area = image.shape[0] * image.shape[1]

    # Confidence score calculation
    confidence = min((defect_area / total_area) * 100 * 50, 99)

    if defect_detected:
        status = "DEFECT DETECTED"
    else:
        status = "NO DEFECT"
        confidence = 100 - confidence

    return status, heatmap, round(confidence,2)