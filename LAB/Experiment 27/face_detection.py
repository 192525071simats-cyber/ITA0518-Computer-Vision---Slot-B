import cv2

video = cv2.VideoCapture("vedio.imp4.mp4")

if not video.isOpened():
    print("ERROR: Cannot open video.")
    raise SystemExit(1)

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

if face_cascade.empty():
    print("ERROR: Face detection model not found.")
    video.release()
    raise SystemExit(1)

while True:
    ret, frame = video.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.05,
        minNeighbors=3,
        minSize=(20, 20)
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(
            frame, (x, y), (x + w, y + h),
            (0, 255, 0), 2
        )
        cv2.putText(
            frame, "Face", (x, max(y - 10, 20)),
            cv2.FONT_HERSHEY_SIMPLEX, 0.7,
            (0, 255, 0), 2
        )

    cv2.imshow("Experiment 27 - Face Detection", frame)

    if cv2.waitKey(25) & 0xFF == ord("q"):
        break

video.release()
cv2.destroyAllWindows()
print("Face detection completed.")
