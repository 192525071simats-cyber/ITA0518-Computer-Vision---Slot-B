import cv2

video = cv2.VideoCapture("vedio.imp4.mp4")

if not video.isOpened():
    print("ERROR: Video not found")
else:
    while True:
        ret, frame = video.read()

        if not ret:
            break

        cv2.imshow("Video", frame)

        if cv2.waitKey(30) & 0xFF == ord("q"):
            break

    video.release()
    cv2.destroyAllWindows()