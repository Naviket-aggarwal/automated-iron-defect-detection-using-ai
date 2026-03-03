from measurement import measure_object
from inspection import check_dimensions
from logger import save_result

import cv2

image_path = "images/sample image.jpg"   # Put test image here

width, height, output_image = measure_object(image_path)

result = check_dimensions(width, height)

print("Width:", width)
print("Height:", height)
print("Inspection Result:", result)

if width is not None:
    save_result(width, height, result)

    cv2.imshow("Inspection Output", output_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()