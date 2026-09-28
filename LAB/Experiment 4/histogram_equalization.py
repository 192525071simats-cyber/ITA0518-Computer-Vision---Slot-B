import cv2

image = cv2.imread("image.jpg")

if image is None:
    print("ERROR: Image not found")
else:
    print("Image loaded successfully")

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    equalized_image = cv2.equalizeHist(gray_image)

    cv2.imshow("Original Image", gray_image)
    cv2.imshow("Equalized Image", equalized_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
