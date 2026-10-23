import cv2
import numpy as np

image = cv2.imread("image.jpg")

if image is None:
    print("ERROR: Image not found!")
else:
    rows, cols = image.shape[:2]

    matrix = np.float32([
        [1, 0, 50],
        [0, 1, 30]
    ])

    transformed = cv2.warpAffine(
        image, matrix, (cols, rows)
    )

    cv2.imshow("Original Image", image)
    cv2.imshow("Affine Transformation", transformed)

    cv2.imwrite("affine_output.jpg", transformed)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
