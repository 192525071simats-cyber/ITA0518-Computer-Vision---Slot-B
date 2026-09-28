import cv2

# Read the image
image = cv2.imread("image.jpg")

# Display original image
cv2.imshow("Original Image", image)

# Convert image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Display grayscale image
cv2.imshow("Gray-scale Image", gray_image)

# Wait until a key is pressed
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()