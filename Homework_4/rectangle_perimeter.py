def segment_length(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def perimeter(coords):
    # p = 0
    # coords.append(coords[0], coords[1])
    # for i in range(4):
    #     # 0   (0, 1, 2, 3)
    #     # 1   (2, 3, 4, 5)
    #     # 2   (4, 5, 6, 7)
    #     # 3   (6, 7, 8, 9)
    #     p += segment_length(coords[i * 2], coords[i * 2 + 1], coords[(i + 1) * 2], coords[(i + 1) * 2 + 1])

    p = segment_length(coords[0], coords[1], coords[2], coords[3])
    p += segment_length(coords[2], coords[3], coords[4], coords[5])
    p += segment_length(coords[4], coords[5], coords[6], coords[7])
    p += segment_length(coords[6], coords[7], coords[0], coords[1])

    return p


coordinates = [float(num) for num in input('Enter coordinates: ').split()]

print(perimeter(coordinates))

