import cv2

video = cv2.VideoCapture("vedio.imp4.mp4")

if not video.isOpened():
    print("ERROR: Cannot open vedio.imp4.mp4")
    raise SystemExit(1)

fps = video.get(cv2.CAP_PROP_FPS)
if fps <= 0:
    fps = 20

frames = []

while True:
    ret, frame = video.read()

    if not ret:
        break

    frames.append(frame)

video.release()

if not frames:
    print("ERROR: No frames found in video.")
    raise SystemExit(1)

height, width = frames[0].shape[:2]

# Save the video in reverse order
output = cv2.VideoWriter(
    "reverse_video.mp4",
    cv2.VideoWriter_fourcc(*"mp4v"),
    fps,
    (width, height)
)

for frame in reversed(frames):
    output.write(frame)

output.release()

print("Reverse video saved as reverse_video.mp4")
print("Total frames:", len(frames))
print("Press Q to close the playback window.")

# Play the reversed video
reversed_video = cv2.VideoCapture("reverse_video.mp4")

while True:
    ret, frame = reversed_video.read()

    if not ret:
        break

    cv2.imshow("Experiment 26 - Reverse Video", frame)

    delay = max(1, int(1000 / fps))
    if cv2.waitKey(delay) & 0xFF == ord("q"):
        break

reversed_video.release()
cv2.destroyAllWindows()
