import cv2

image = cv2.imread("image.jpg1.jpeg")

if image is None:
    print("ERROR: Image not found")
else:
    rotated_image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

    cv2.imshow("Original Image", image)
    cv2.imshow("90 Degree Clockwise Image", rotated_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()