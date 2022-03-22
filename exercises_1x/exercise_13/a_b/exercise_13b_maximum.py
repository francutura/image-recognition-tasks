import sys
import cv2

def parse_input_file(input_data_filename):
    with open(input_data_filename, "r") as f:
        data = f.readlines()

    x = int(data[0].strip())
    y = int(data[1].strip())
    connectivity = int(data[2].strip())

    return y, x, connectivity


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


def is_regional_maximum(img, x, y, connectivity):
    tracking_img = img.copy()
    tracking_img.fill(0)

    flatzone_queue = []
    flatzone_queue.append((x, y))
    tracking_img[x, y] = 1


    while flatzone_queue:
        curr = flatzone_queue.pop()
        
        neighbours = get_neighbours(
            curr, connectivity, (img.shape[0] - 1, img.shape[1] - 1)
        )
    
        for neighbour in neighbours:
            if (img[curr[0], curr[1]] == img[neighbour[0], neighbour[1]] and 
                tracking_img[neighbour[0], neighbour[1]] != 1
            ):
                tracking_img[neighbour[0], neighbour[1]] = 1
                flatzone_queue.append(neighbour)
                continue
                
            if img[curr[0], curr[1]] < img[neighbour[0], neighbour[1]]:
              return False

    return True

if __name__ == "__main__":
  try:
      input_data_filename = sys.argv[1]
      input_image_name = sys.argv[2]
      output_textfile = sys.argv[3]
  except Exception:
      print("Invalid arguments")
      exit(1)

  img = cv2.imread(input_image_name, cv2.IMREAD_GRAYSCALE)
  x, y, connectivity = parse_input_file(input_data_filename)

  with open(output_textfile, "w") as f:
      f.write(str(int(is_regional_maximum(img, x, y, connectivity))) + '\n')