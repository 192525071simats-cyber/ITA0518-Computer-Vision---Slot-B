import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
import cv2

path = input("Enter image filename: ")
image = cv2.imread(path)

if image is None:
    print("Image not found")
else:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    lower = int(input("Enter lower threshold: "))
    upper = int(input("Enter upper threshold: "))

    if 0 <= lower <= upper <= 255:
        result = cv2.inRange(gray, lower, upper)
        cv2.imwrite("segmented_output.png", result)
        print("Output saved as segmented_output.png")
        cv2.imshow("Segmented Image", result)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Enter valid thresholds between 0 and 255")

