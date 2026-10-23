import cv2

image = cv2.imread("image.jpg")

if image is None:
    print("ERROR: Image not found!")
else:
    height, width = image.shape[:2]

    x1, y1 = width // 4, height // 4
    x2, y2 = 3 * width // 4, 3 * height // 4

    roi = image[y1:y2, x1:x2].copy()
    result = image.copy()

    h, w = roi.shape[:2]
    result[0:h, 0:w] = roi

    cv2.imshow("Original Image", image)
    cv2.imshow("Cropped ROI", roi)
    cv2.imshow("Pasted ROI", result)

    cv2.imwrite("cropped_roi.jpg", roi)
    cv2.imwrite("roi_pasted.jpg", result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
