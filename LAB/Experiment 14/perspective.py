import cv2
import numpy as np

image = cv2.imread("image.jpg")

if image is None:
    print("ERROR: Image not found!")
else:
    rows, cols = image.shape[:2]

    source = np.float32([
        [0, 0],
        [cols - 1, 0],
        [0, rows - 1],
        [cols - 1, rows - 1]
    ])

    destination = np.float32([
        [50, 30],
        [cols - 50, 0],
        [0, rows - 30],
        [cols - 1, rows - 1]
    ])

    matrix = cv2.getPerspectiveTransform(source, destination)
    result = cv2.warpPerspective(image, matrix, (cols, rows))

    cv2.imshow("Original Image", image)
    cv2.imshow("Perspective Transformation", result)

    cv2.imwrite("perspective_output.jpg", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
