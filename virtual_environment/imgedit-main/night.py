import random

from PIL import Image

night = Image.open("night.jpg")
pixels = night.load
print("loaded")

#pre-process -> This finds what to set the brightness to
population = 0
thresh = 0.03
bright = 3 * 260
while population/(night.width*night.height) < thresh:
    bright -= 5
    population = 0
    for y in range(night.height):
        for x in range(night.width):
            r, g, b = pixels[x, y]
            bright = 3*245
            total = r + b + g
            if total>bright:
                population += 1

print(population/(night.width*night.height))

print(bright/3)

night.save("night.jpg")