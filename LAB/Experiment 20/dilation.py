import cv2
import numpy as np

image = cv2.imread("image.jpg")

if image is None:
    print("ERROR: Image not found!")
else:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    kernel = np.ones((5, 5), np.uint8)
    dilated = cv2.dilate(binary, kernel, iterations=1)

    cv2.imshow("Original Image", image)
    cv2.imshow("Dilation Image", dilated)

    cv2.imwrite("dilation_output.jpg", dilated)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
