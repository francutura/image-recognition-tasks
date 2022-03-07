import cv2
import sys
from exercise_06a_closing_opening import opening, closing

try:
    img_name = sys.argv[1]
except Exception:
    print("Invalid arguments")
    exit(1)

img = cv2.imread(img_name, cv2.IMREAD_GRAYSCALE)

img1 = opening(img, 1)
img2 = closing(img, 1)
img3 = closing(img1, 1)
img4 = opening(img1, 1)

cv2.imwrite("filter_1.pgm", img1)
cv2.imwrite("filter_2.pgm", img2)
cv2.imwrite("filter_3.pgm", img3)
cv2.imwrite("filter_4.pgm", img4)
