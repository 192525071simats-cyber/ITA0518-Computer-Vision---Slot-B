import cv2
import os

video = cv2.VideoCapture("vedio.imp4.mp4")

if not video.isOpened():
    print("ERROR: Cannot open vedio.imp4.mp4")
    raise SystemExit(1)

smile_path = cv2.data.haarcascades + "haarcascade_smile.xml"
smile_cascade = cv2.CascadeClassifier(smile_path)

if smile_cascade.empty():
    print("ERROR: Smile detection model not found.")
    video.release()
    raise SystemExit(1)

fps = video.get(cv2.CAP_PROP_FPS)
if fps <= 0:
    fps = 25.0

width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

writer = cv2.VideoWriter(
    "smile_detection_output.mp4",
    cv2.VideoWriter_fourcc(*"mp4v"),
    fps,
    (width, height)
)

if not writer.isOpened():
    print("ERROR: Cannot create output video.")
    video.release()
    raise SystemExit(1)

frame_count = 0
total_smiles = 0
saved_image = False

print("Processing video... Please wait.")

while True:
    ret, frame = video.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    smiles = smile_cascade.detectMultiScale(
        gray,
        scaleFactor=1.7,
        minNeighbors=20,
        minSize=(25, 25)
    )

    total_smiles += len(smiles)

    for (x, y, w, h) in smiles:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(
            frame, "Smile", (x, max(y - 10, 20)),
            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2
        )

    cv2.putText(
        frame, "Smiles detected: " + str(len(smiles)),
        (20, 35), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2
    )

    if not saved_image:
        cv2.imwrite("smile_detection_result.jpg", frame)
        saved_image = True

    writer.write(frame)
    frame_count += 1

video.release()
writer.release()

print("Smile detection completed.")
print("Frames processed:", frame_count)
print("Total smile detections across frames:", total_smiles)
print("Output video: smile_detection_output.mp4")
print("Output image: smile_detection_result.jpg")

# Open the processed output video
result = cv2.VideoCapture("smile_detection_output.mp4")

while True:
    ret, frame = result.read()
    if not ret:
        break

    cv2.imshow("Experiment 30 - Smile Detection Output", frame)

    if cv2.waitKey(30) & 0xFF == ord("q"):
        break

result.release()
cv2.destroyAllWindows()
