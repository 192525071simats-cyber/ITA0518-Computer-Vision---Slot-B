import cv2

video = cv2.VideoCapture("vedio.imp4.mp4")

if not video.isOpened():
    print("ERROR: Cannot open vedio.imp4.mp4")
    raise SystemExit(1)

eye_path = cv2.data.haarcascades + "haarcascade_eye.xml"
eye_cascade = cv2.CascadeClassifier(eye_path)

if eye_cascade.empty():
    print("ERROR: Eye detection model not found.")
    video.release()
    raise SystemExit(1)

print("Eye detection started. Press Q to stop.")

while True:
    ret, frame = video.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    eyes = eye_cascade.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=5, minSize=(20, 20)
    )

    for (x, y, w, h) in eyes:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.putText(
        frame, "Eyes detected: " + str(len(eyes)),
        (20, 35), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2
    )

    cv2.imshow("Experiment 29 - Eye Detection", frame)

    if cv2.waitKey(30) & 0xFF == ord("q"):
        break

video.release()
cv2.destroyAllWindows()
print("Eye detection completed.")
