import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
import cv2
import numpy as np

width = int(input("Enter image width: "))
height = int(input("Enter image height: "))
image = np.ones((height, width, 3), dtype=np.uint8) * 255

x = int(input("Enter circle center X: "))
y = int(input("Enter circle center Y: "))
radius = int(input("Enter circle radius: "))

cv2.circle(image, (x, y), radius, (255, 0, 0), 3)
cv2.imwrite("circle_output.png", image)
print("Output saved as circle_output.png")
cv2.imshow("Circle", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

