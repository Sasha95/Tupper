import io

import numpy
from PIL import Image
from flask import send_file
from matplotlib.pyplot import imsave


def from_k_to_bin(k: int) -> list:
    k //= 17
    binary = bin(k)[2:]
    binary = binary.rjust(1802, "0")

    lists = [[] for x in range(17)]
    for x in range(1802):
        lists[x % 17].append(binary[x])

    lists.reverse()
    return lists


def get_image(k: int):
    lists = from_k_to_bin(k)

    image = Image.new("1", (106, 17), 0)
    for y in range(17):
        for x in range(106):
            image.putpixel(xy=(105 - x, 16 - y), value=(int(lists[y][x]),))

    image.save("/app/static/result.png")
