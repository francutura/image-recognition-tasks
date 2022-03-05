import cv2

try:
    INPUT_IMG = sys.argv[1]
    VALUE = int(sys.argv[2])
    OUTPUT_IMAGE_NAME = sys.argv[3]
except Exception:
    print("Invalid arguments")
    exit(1)

img = cv2.imread(INPUT_IMG, cv2.IMREAD_GRAYSCALE)

for x in range(0, img.shape[0]):
    for y in range(0, img.shape[1]):
        img[x, y] = 255 if img[x, y] >= VALUE else 0

cv2.imwrite(OUTPUT_IMAGE_NAME, img)
