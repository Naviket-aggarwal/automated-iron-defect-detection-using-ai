from measurement import measure_object
from inspection import check_dimensions
from anomaly import detect_anomaly
from logger import save_result

image_path = "images/sample 2.jpg"

# Dimension detection
width, height, _ = measure_object(image_path)
dimension_result = check_dimensions(width, height)

# Surface defect detection
anomaly_status, _ = detect_anomaly(image_path)

# Final industrial decision
if dimension_result == "OK" and anomaly_status == "NO DEFECT":
    final_status = "PASS"
else:
    final_status = "FAIL"

print("Width:", width)
print("Height:", height)
print("Dimension Result:", dimension_result)
print("Anomaly Status:", anomaly_status)
print("Final Status:", final_status)

save_result(width, height, final_status)