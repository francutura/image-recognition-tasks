import cv2
import sys


def is_equal(img1, img2):
    if img1.shape != img2.shape:
        return 0

    for x in range(0, img1.shape[0]):
        for y in range(0, img1.shape[1]):
            if img1[x, y] != img2[x, y]:
                return 0
    return 1


try:
    img1_name = sys.argv[1]
    img2_name = sys.argv[2]
except Exception:
    print("Invalid arguments")
    exit(1)

img1 = cv2.imread(img1_name, cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread(img2_name, cv2.IMREAD_GRAYSCALE)

equal = is_equal(img1, img2)

with open("exercise_02b_output_01.txt", "w") as f:
    f.write(str(equal) + "\n")
