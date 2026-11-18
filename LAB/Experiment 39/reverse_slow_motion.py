import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
import cv2

path = input("Enter video filename: ")
video = cv2.VideoCapture(path)

if not video.isOpened():
    print("Video not found")
else:
    fps = video.get(cv2.CAP_PROP_FPS)
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    frames = []

    while True:
        ret, frame = video.read()
        if not ret:
            break
        frames.append(frame)

    video.release()

    if not frames:
        print("No frames found")
    else:
        output_fps = max(fps / 2, 1)
        writer = cv2.VideoWriter(
            "reverse_slow_output.mp4",
            cv2.VideoWriter_fourcc(*"mp4v"),
            output_fps,
            (width, height)
        )

        print("Creating reverse slow-motion video...")
        for frame in reversed(frames):
            writer.write(frame)

        writer.release()
        print("Output saved as reverse_slow_output.mp4")
        print("Press Q to stop playback")

        for frame in reversed(frames):
            cv2.imshow("Reverse Slow Motion", frame)
            if cv2.waitKey(100) & 0xFF == ord("q"):
                break

        cv2.destroyAllWindows()

