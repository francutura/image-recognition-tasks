import sys
import cv2

LABEL_NO_FZ = 0


def parse_input_file(input_data_filename):
    with open(input_data_filename, "r") as f:
        data = f.readlines()

    x = int(data[0].strip())
    y = int(data[1].strip())
    connectivity = int(data[2].strip())
    flat_zone_label = int(data[3].strip())

    return x, y, connectivity, flat_zone_label


def get_neighbours(coordinate, connectivity, bounds):
    c = coordinate
    if connectivity == 4:
        retval = [
            (c[0] + 1, c[1]),
            (c[0], c[1] + 1),
            (c[0] - 1, c[1]),
            (c[0], c[1] - 1),
        ]

    elif connectivity == 8:
        retval = [
            (c[0] + 1, c[1]),
            (c[0], c[1] + 1),
            (c[0] - 1, c[1]),
            (c[0], c[1] - 1),
            (c[0] + 1, c[1] + 1),
            (c[0] - 1, c[1] + 1),
            (c[0] - 1, c[1] - 1),
            (c[0] + 1, c[1] - 1),
        ]
    else:
        return []

    return [
        coordinate
        for coordinate in retval
        if (coordinate[0] >= 0 and coordinate[0] <= bounds[0])
        and (coordinate[1] >= 0 and coordinate[1] <= bounds[1])
    ]


def flat_zone_image(img, x, y, connectivity, flat_zone_label):

    # Create out image
    out_img = img.copy()
    out_img.fill(LABEL_NO_FZ)

    # Init first flat_zone_label
    out_img[x, y] = flat_zone_label

    # The flatzone queue
    flatzone = list()
    flatzone.append((x, y))

    while flatzone:
        curr = flatzone.pop()
        neighbours = get_neighbours(
            curr, connectivity, (img.shape[0] - 1, img.shape[1] - 1)
        )

        for neighbour in neighbours:
            if (img[curr[0], curr[1]] == img[neighbour[0], neighbour[1]]) and (
                out_img[neighbour[0], neighbour[1]] != flat_zone_label
            ):
                out_img[neighbour[0], neighbour[1]] = flat_zone_label
                flatzone.append(neighbour)
                
    return out_img


if __name__ == "__main__":

    try:
        input_data_filename = sys.argv[1]
        input_image_name = sys.argv[2]
        output_image_name = sys.argv[3]
    except Exception:
        print("Invalid arguments")
        exit(1)

    img = cv2.imread(input_image_name, cv2.IMREAD_GRAYSCALE)
    x, y, connectivity, flat_zone_label = parse_input_file(input_data_filename)
    out_img = flat_zone_image(img, x, y, connectivity, flat_zone_label)
    cv2.imwrite(output_image_name, out_img)
