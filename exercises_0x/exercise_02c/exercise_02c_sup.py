import cv2
import sys


def infinum(img1, img2):
    out_img = img1.copy()
    out_img.fill(0)

    dimensions = (len(img1[0]), len(img1))
    for row_idx in range(dimensions[1]):
        for col_idx in range(dimensions[0]):
            out_img[row_idx][col_idx] = max(
                img1[row_idx][col_idx], img2[row_idx][col_idx]
            )

    return out_img


if __name__ == "__main__":
    try:
        img1_name = sys.argv[1]
        img2_name = sys.argv[2]
        output_name = sys.argv[3]
    except Exception:
        print("Invalid arguments")
        exit(1)

    img1 = cv2.imread(img1_name, cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread(img2_name, cv2.IMREAD_GRAYSCALE)

    out_img = infinum(img1, img2)

    cv2.imwrite(output_name, out_img)
