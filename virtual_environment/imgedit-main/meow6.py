import random

from PIL import Image

cat = Image.open("cat.jpg")

properties = [cat.format, cat.mode, cat.size, cat.width, cat.height]

cat_pixels = cat.load()
edit_cat = []

def roll(min_val, max_val):
    return random.randint(min_val, max_val)

for y in range(cat.height):
    for x in range(cat.width):
        r, g, b = cat_pixels[x, y]

        r = roll(r - 50, r + 50)
        g = roll(g - 50, g + 50)
        b = roll(b - 50, b + 50)

        edit_cat.append((r, g, b))

new_cat = Image.new("RGB", cat.size)

new_cat.putdata(edit_cat)

new_cat.save("grainy_cat_#grainy.jpg")