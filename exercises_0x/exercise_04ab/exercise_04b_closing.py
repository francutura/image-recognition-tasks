import cv2
import sys
from exercise_04a_opening import erosion, dilation


def closing(img, i):
    output_img = dilation(img, i)
    return erosion(output_img, i)


try:
    i = int(sys.argv[1])
    img_name = sys.argv[2]
    output_name = sys.argv[3]
except Exception:
    print("Invalid arguments")
    exit(1)

img = cv2.imread(img_name, cv2.IMREAD_GRAYSCALE)

img_eroded = closing(img, i)
cv2.imwrite(output_name, img_eroded)
