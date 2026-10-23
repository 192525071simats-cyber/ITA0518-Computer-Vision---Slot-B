import cv2
import os
import urllib.request

image = cv2.imread("image.jpg")

if image is None:
    print("ERROR: Image not found!")
else:
    prototxt = "deploy.prototxt"
    model = "mobilenet_iter_73000.caffemodel"

    urls = {
        prototxt: "https://raw.githubusercontent.com/chuanqi305/MobileNet-SSD/master/deploy.prototxt",
        model: "https://raw.githubusercontent.com/chuanqi305/MobileNet-SSD/master/mobilenet_iter_73000.caffemodel"
    }

    try:
        for filename, url in urls.items():
            if not os.path.exists(filename):
                print("Downloading", filename)
                urllib.request.urlretrieve(url, filename)

        net = cv2.dnn.readNetFromCaffe(prototxt, model)

        classes = [
            "background", "aeroplane", "bicycle", "bird", "boat",
            "bottle", "bus", "car", "cat", "chair", "cow",
            "diningtable", "dog", "horse", "motorbike", "person",
            "pottedplant", "sheep", "sofa", "train", "tvmonitor"
        ]

        h, w = image.shape[:2]
        blob = cv2.dnn.blobFromImage(
            cv2.resize(image, (300, 300)),
            0.007843, (300, 300), 127.5
        )

        net.setInput(blob)
        detections = net.forward()
        found = False

        for i in range(detections.shape[2]):
            confidence = float(detections[0, 0, i, 2])
            class_id = int(detections[0, 0, i, 1])

            if confidence > 0.5:
                label = classes[class_id]
                if label == "watch":
                    found = True
                    box = detections[0, 0, i, 3:7] * [w, h, w, h]
                    x1, y1, x2, y2 = box.astype(int)
                    cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.putText(image, "Watch", (x1, max(y1 - 10, 20)),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        if not found:
            print("Watch not detected. This model does not support the watch class.")

        cv2.imshow("Watch Recognition", image)
        cv2.imwrite("watch_output.jpg", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    except Exception as e:
        print("Model download or detection failed:", e)
