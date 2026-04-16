from PIL import Image

cat = Image.open("cat.jpg")

properties = [cat.format, cat.mode, cat.size, cat.width, cat.height]

cat_pixels = cat.load()
edit_cat = []

for y in range(cat.height):
    for x in range(cat.width):
        r, g, b = cat_pixels[x, y]

        # Invert the colors
        r = 255 - r
        g = 255 - g
        b = 255 - b

        edit_cat.append((r, g, b))

new_cat = Image.new("RGB", cat.size)

new_cat.putdata(edit_cat)

new_cat.save("inverted_cat_#weird.jpg")