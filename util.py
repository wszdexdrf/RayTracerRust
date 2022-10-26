import numpy
from PIL import Image
import os

os.system("cargo run > image.ppm")

with open("image.ppm", "r") as f:
    content = f.read().splitlines()
content.pop(0)
shape = (-1, -1, 3)
r, c = 0, 0
arr = numpy.zeros((1,))
for line in content:
    line = line.replace("\0", "")
    line = line.replace("\n", "")
    if len(line) != 0:
        if shape == (-1, -1, 3):
            shape = tuple(map(int, line.split()))
            shape = shape + (3,)
            arr = numpy.zeros(shape)
        elif r < shape[0]:
            arr[r][c] = numpy.array(list(map(int, line.split())))
            r += 1
        else:
            r = 0
            c += 1
            arr[r][c] = numpy.array(list(map(int, line.split())))

arr = arr.astype(numpy.uint8)
image = Image.fromarray(arr)
image.save("image.png")
