import cv2
import sys


try:
    img1_name = sys.argv[1]
    img2_name = sys.argv[2]
    output_name = sys.argv[3]
except Exception:
    print("Invalid arguments")
    exit(1)

img1 = cv2.imread(img1_name, cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread(img2_name, cv2.IMREAD_GRAYSCALE)
img3 = cv2.min(img1, img2)
cv2.imwrite(output_name, img3)
