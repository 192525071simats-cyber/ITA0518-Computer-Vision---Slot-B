import cv2
import numpy as np

image = cv2.imread("image.jpg")

if image is None:
    print("ERROR: Image not found!")
else:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = np.float32(gray)

    corners = cv2.cornerHarris(gray, 2, 3, 0.04)

    result = image.copy()
    result[corners > 0.01 * corners.max()] = [0, 0, 255]

    cv2.imshow("Original Image", image)
    cv2.imshow("Harris Corner Detection", result)

    cv2.imwrite("harris_output.jpg", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
