import random

import png

title = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 3, 3, 3, 0, 5, 0, 8, 0],
    [0, 1, 0, 0, 0, 0, 4, 0, 0, 5, 0, 8, 0],
    [0, 1, 0, 0, 0, 0, 4, 0, 0, 6, 6, 6, 0],
    [0, 1, 0, 0, 0, 0, 4, 0, 0, 7, 0, 9, 0],
    [0, 2, 2, 2, 0, 0, 4, 0, 0, 7, 0, 9, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

w = len(title[0])
h = len(title)
m = max(map(max, title))

DMX = 320 * 20
DMY = 200 * 20
level0 = [(0, 0)]


def draw(bi, arr, new_arr):
    x0 = DMX
    y0 = DMY
    x1 = 0
    y1 = 0

    for y in range(h):
        for x in range(w):
            if title[y][x] == bi:
                x0 = min(x, x0)
                y0 = min(y, y0)
                x1 = max(x, x1)
                y1 = max(y, y1)

    cw = DMX / w
    dx = x1 - x0 + 1
    ch = DMY / h
    dy = y1 - y0 + 1

    if dx >= dy:
        for (x, y) in arr:
            new_arr.append(
                (int(x0 * cw + (x / DMX) * dx * cw),
                 int(y0 * ch + (y / DMY) * dy * ch))
            )
    else:
        for (y, x) in arr:
            new_arr.append(
                (int(x0 * cw + (x / DMY) * dx * cw),
                 int((y1 + 1) * ch - (y / DMX) * dy * ch))
            )
    return


for bb in range(8):
    print(f"{bb}, {len(level0)}")
    na = []
    for i in range(1, m + 1):
        draw(i, level0, na)
    level0 = list(set(na))

random.shuffle(level0)

img = [[0 for x in range(DMX)] for y in range(DMY)]


def plot(x, y):
    img[y][x] = 255


print(len(level0))
for i in range(len(level0)):
    (x, y) = level0[i]
    plot(x, y)

png.fromarray(img, 'L').save("dots.png")
