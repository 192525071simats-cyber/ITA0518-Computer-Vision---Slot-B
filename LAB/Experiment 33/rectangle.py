import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
import cv2
import numpy as np

width = int(input("Enter image width: "))
height = int(input("Enter image height: "))
image = np.ones((height, width, 3), dtype=np.uint8) * 255

x1 = int(input("Enter top-left X: "))
y1 = int(input("Enter top-left Y: "))
x2 = int(input("Enter bottom-right X: "))
y2 = int(input("Enter bottom-right Y: "))

cv2.rectangle(image, (x1, y1), (x2, y2), (0, 0, 255), 3)
cv2.imwrite("rectangle_output.png", image)
print("Output saved as rectangle_output.png")
cv2.imshow("Rectangle", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

