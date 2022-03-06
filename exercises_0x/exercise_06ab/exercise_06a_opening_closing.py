import cv2
import sys
import numpy as np


try:
    i = int(sys.argv[1])
    img_name = sys.argv[2]
    output_name = sys.argv[3]
except Exception:
    print("Invalid arguments")
    exit(1)

img = cv2.imread(img_name, cv2.IMREAD_GRAYSCALE)

kernel = np.ones((2 * i + 1, 2 * i + 1), np.uint8)

img1 = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
img2 = cv2.morphologyEx(img1, cv2.MORPH_OPEN, kernel)

cv2.imwrite(output_name, img2)
