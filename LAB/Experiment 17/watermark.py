import cv2

image = cv2.imread("image.jpg")

if image is None:
    print("ERROR: Image not found!")
else:
    watermark = image.copy()

    cv2.putText(
        watermark, "WATERMARK", (30, 60),
        cv2.FONT_HERSHEY_SIMPLEX, 1.5,
        (255, 255, 255), 3
    )

    result = cv2.addWeighted(watermark, 0.7, image, 0.3, 0)

    cv2.imshow("Original Image", image)
    cv2.imshow("Watermarked Image", result)

    cv2.imwrite("watermark_output.jpg", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
