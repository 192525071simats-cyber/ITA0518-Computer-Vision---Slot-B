import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
import cv2

path = input("Enter image filename: ")
image = cv2.imread(path)

if image is None:
    print("Image not found")
else:
    text = input("Enter text: ")
    x = int(input("Enter X position: "))
    y = int(input("Enter Y position: "))

    cv2.putText(image, text, (x, y),
                cv2.FONT_HERSHEY_SIMPLEX, 1,
                (0, 0, 255), 2, cv2.LINE_AA)

    cv2.imwrite("text_output.jpg", image)
    print("Output saved as text_output.jpg")
    cv2.imshow("Text on Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

