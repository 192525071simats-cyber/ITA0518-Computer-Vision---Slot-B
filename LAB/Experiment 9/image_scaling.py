import cv2

image = cv2.imread("image.jpg1.jpeg")

if image is None:
    print("ERROR: Image not found")
else:
    bigger_image = cv2.resize(image, None, fx=2, fy=2)

    smaller_image = cv2.resize(image, None, fx=0.5, fy=0.5)

    cv2.imshow("Original Image", image)
    cv2.imshow("Bigger Image", bigger_image)
    cv2.imshow("Smaller Image", smaller_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()