import cv2
import sys
import numpy as np

kernel = np.ones((3, 3), np.uint8)

try:
    img_name = sys.argv[1]
except Exception:
    print("Invalid arguments")
    exit(1)

img = cv2.imread(img_name, cv2.IMREAD_GRAYSCALE)

img1 = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
img2 = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
img3 = cv2.morphologyEx(img1, cv2.MORPH_CLOSE, kernel)
img4 = cv2.morphologyEx(img2, cv2.MORPH_OPEN, kernel)

cv2.imwrite("filter_1.pgm", img1)
cv2.imwrite("filter_2.pgm", img2)
cv2.imwrite("filter_3.pgm", img3)
cv2.imwrite("filter_4.pgm", img4)
