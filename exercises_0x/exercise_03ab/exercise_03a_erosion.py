import cv2
import sys


def erosion(img, i):
    output_img = img.copy()

    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            min_xy = img[x, y]
            coordinates = []
            for x_s in range(max(0, x - i), min(img.shape[0] - 1, x + i) + 1):
                for y_s in range(max(0, y - i), min(img.shape[1] - 1, y + i) + 1):
                    coordinates.append((x_s, y_s))
            for coordinate in coordinates:
                if min_xy > img[coordinate[0], coordinate[1]]:
                    min_xy = img[coordinate[0], coordinate[1]]
            output_img[x, y] = min_xy

    return output_img


if __name__ == "__main__":
    try:
        i = int(sys.argv[1])
        img_name = sys.argv[2]
        output_name = sys.argv[3]
    except Exception:
        print("Invalid arguments")
        exit(1)

    img = cv2.imread(img_name, cv2.IMREAD_GRAYSCALE)
    output_img = erosion(img, i)
    cv2.imwrite(output_name, output_img)
