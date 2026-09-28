import cv2
import matplotlib.pyplot as plt

def analyze_histogram(image):
    colors = ("b", "g", "r")

    for i, color in enumerate(colors):
        histogram = cv2.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(histogram, color=color)

    plt.title("Color Histogram")
    plt.xlabel("Color Level")
    plt.ylabel("Number of Pixels")
    plt.show()

image = cv2.imread("image.jpg")

if image is None:
    print("ERROR: Image not found")
else:
    print("Image loaded successfully")
    analyze_histogram(image)
