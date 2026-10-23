import cv2

image = cv2.imread("image.jpg")

if image is None:
    print("ERROR: Image not found!")
else:
    rotated_image = cv2.rotate(
        image, cv2.ROTATE_90_COUNTERCLOCKWISE
    )

    cv2.imshow("Original Image", image)
    cv2.imshow("270 Degree Clockwise Rotation", rotated_image)

    cv2.imwrite("rotated270.jpg", rotated_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
