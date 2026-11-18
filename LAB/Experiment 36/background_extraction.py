import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
import cv2
import numpy as np

path = input("Enter image filename: ")
image = cv2.imread(path)

if image is None:
    print("Image not found")
else:
    print("Enter background colour range in BGR format")
    lb = int(input("Lower Blue: "))
    lg = int(input("Lower Green: "))
    lr = int(input("Lower Red: "))
    ub = int(input("Upper Blue: "))
    ug = int(input("Upper Green: "))
    ur = int(input("Upper Red: "))

    lower = np.array([lb, lg, lr], dtype=np.uint8)
    upper = np.array([ub, ug, ur], dtype=np.uint8)

    mask = cv2.inRange(image, lower, upper)
    result = cv2.bitwise_and(image, image, mask=mask)

    cv2.imwrite("background_output.png", result)
    print("Output saved as background_output.png")
    cv2.imshow("Extracted Background", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

