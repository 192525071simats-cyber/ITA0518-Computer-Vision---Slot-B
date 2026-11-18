import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
import cv2
import numpy as np

width = int(input("Enter image width: "))
height = int(input("Enter image height: "))

image = np.ones((height, width, 3), dtype=np.uint8) * 255
bw, bh = max(1, width // 10), max(1, height // 10)

image[0:bh, 0:bw] = (0, 0, 0)
image[0:bh, width-bw:width] = (255, 0, 0)
image[height-bh:height, 0:bw] = (0, 255, 0)
image[height-bh:height, width-bw:width] = (0, 0, 255)

cv2.imwrite("colored_boxes_output.png", image)
print("Output saved as colored_boxes_output.png")
cv2.imshow("Four Coloured Boxes", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

