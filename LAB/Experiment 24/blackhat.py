import cv2
import numpy as np

image = cv2.imread("image.jpg")

if image is None:
    print("ERROR: Image not found!")
else:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    kernel = np.ones((5, 5), np.uint8)

    result = cv2.morphologyEx(gray, cv2.MORPH_BLACKHAT, kernel)

    cv2.imshow("Original Image", image)
    cv2.imshow("Black Hat Transformation", result)
    cv2.imwrite("blackhat_output.jpg", result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
