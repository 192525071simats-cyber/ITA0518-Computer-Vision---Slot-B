import cv2
from ultralytics import YOLO

model = YOLO("yolo11n.pt")
video = cv2.VideoCapture("vehicle vedio.mp4")

if not video.isOpened():
    print("ERROR: Cannot open vehicle vedio.mp4")
    raise SystemExit(1)

vehicle_classes = {"car", "motorcycle", "bus", "truck"}

while True:
    ret, frame = video.read()
    if not ret:
        break

    results = model.predict(frame, imgsz=640, conf=0.35, verbose=False)

    for result in results:
        for box in result.boxes:
            class_id = int(box.cls[0])
            label = model.names[class_id]

            if label in vehicle_classes:
                x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, label, (x1, max(y1 - 10, 20)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    cv2.imshow("Experiment 28 - Vehicle Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video.release()
cv2.destroyAllWindows()
print("Vehicle detection completed.")
