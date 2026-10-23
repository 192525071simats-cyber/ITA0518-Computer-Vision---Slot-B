import cv2

img = cv2.imread("image.jpg")

if img is None:
    print("ERROR: image.jpg is missing from Experiment 25")
    raise SystemExit(1)

net = cv2.dnn.readNetFromCaffe(
    "MobileNetSSD_deploy.prototxt",
    "MobileNetSSD_deploy.caffemodel"
)

classes = [
    "background", "aeroplane", "bicycle", "bird",
    "boat", "bottle", "bus", "car", "cat", "chair",
    "cow", "diningtable", "dog", "horse", "motorbike",
    "person", "pottedplant", "sheep", "sofa", "train",
    "tvmonitor"
]

h, w = img.shape[:2]

blob = cv2.dnn.blobFromImage(
    cv2.resize(img, (300, 300)),
    0.007843, (300, 300), 127.5
)

net.setInput(blob)
detections = net.forward()
count = 0

for i in range(detections.shape[2]):
    confidence = float(detections[0, 0, i, 2])

    if confidence > 0.5:
        class_id = int(detections[0, 0, i, 1])

        if 0 < class_id < len(classes):
            box = detections[0, 0, i, 3:7] * [w, h, w, h]
            x1, y1, x2, y2 = box.astype(int)
            label = classes[class_id]

            cv2.rectangle(
                img, (x1, y1), (x2, y2), (0, 255, 0), 2
            )
            cv2.putText(
                img, label, (x1, max(y1 - 10, 20)),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2
            )

            print("Detected:", label, "Confidence:", round(confidence, 2))
            count += 1

if count == 0:
    print("No objects detected above 50% confidence.")

cv2.imwrite("detected_output.jpg", img)
print("Output saved as detected_output.jpg")

cv2.imshow("Experiment 25 - Object Recognition", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
