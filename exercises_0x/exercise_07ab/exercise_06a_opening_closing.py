import cv2
import sys
from exercise_06a_closing_opening import opening, closing

try:
    i = int(sys.argv[1])
    img_name = sys.argv[2]
    output_name = sys.argv[3]
except Exception:
    print("Invalid arguments")
    exit(1)

img = cv2.imread(img_name, cv2.IMREAD_GRAYSCALE)


img1 = closing(img, i)
img2 = opening(img1, i)

cv2.imwrite(output_name, img2)
