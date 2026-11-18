import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
import cv2

try:
    import pytesseract
except ImportError:
    print("Install pytesseract: py -m pip install pytesseract")
    raise SystemExit

# Change this path if Tesseract is installed elsewhere.
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

path = input("Enter video filename: ")
video = cv2.VideoCapture(path)

if not video.isOpened():
    print("Video not found")
else:
    frame_number = 0
    extracted = []

    while True:
        ret, frame = video.read()
        if not ret:
            break

        if frame_number % 30 == 0:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            text = pytesseract.image_to_string(gray).strip()

            if text:
                extracted.append("Frame " + str(frame_number) + "\n" + text)
                print("Text found in frame", frame_number)
                print(text)

        frame_number += 1

    video.release()

    with open("extracted_text.txt", "w", encoding="utf-8") as file:
        file.write("\n\n".join(extracted))

    print("Text saved as extracted_text.txt")

