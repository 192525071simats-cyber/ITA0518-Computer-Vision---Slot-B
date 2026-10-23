import cv2

image = cv2.imread("image.jpg")

if image is None:
    print("ERROR: Image not found!")
else:
    rotated_image = cv2.rotate(image, cv2.ROTATE_180)

    cv2.imshow("Original Image", image)
    cv2.imshow("180 Degree Rotated Image", rotated_image)

    cv2.imwrite("rotated180.jpg", rotated_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
