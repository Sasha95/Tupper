import base64
from io import BytesIO

from PIL import Image
from urllib.request import urlopen
import textwrap

_SIZE_WIDTH = 106
_SIZE_HEIGHT = 17


def get_image(url: str) -> Image:
    im = Image.open(urlopen(url))
    im = im.resize((_SIZE_WIDTH, _SIZE_HEIGHT), Image.ANTIALIAS)
    return im

def generate_image(file) -> None:
    # image = get_image(url)

    image = Image.open(file.stream)
    image = image.resize((_SIZE_WIDTH, _SIZE_HEIGHT), Image.ANTIALIAS)

    image = image.convert('1')

    byteset = ""
    for x in range(105, -1, -1):
        for y in range(0, 17):
            if image.getpixel((x, y)) > 127:
                byteset += '1'
            else:
                byteset += '0'

    k = str(int(byteset, 2) * 17)
    return textwrap.fill(k, width=25), image
