import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
import cv2

path = input("Enter image filename: ")
image = cv2.imread(path)

if image is None:
    print("Image not found")
else:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    detector = cv2.CascadeClassifier(cascade_path)

    faces = detector.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    count = len(faces)
    print("Number of faces detected:", count)
    cv2.imwrite("face_detection_output.jpg", image)

    with open("face_count.txt", "w") as file:
        file.write("Number of faces detected: " + str(count))

    print("Output saved as face_detection_output.jpg and face_count.txt")
    cv2.imshow("Face Detection", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

