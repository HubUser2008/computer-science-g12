from PIL import Image

cat = Image.open("cat.jpg")

properties = [cat.format, cat.mode, cat.size, cat.width, cat.height]

cat_pixels = cat.load()
edit_cat = []

for y in range(cat.height):
    for x in range(cat.width):
        r, g, b = cat_pixels[x, y]

        # Check if RGB total exceeds 3 * 255
        if (r + g + b) > 765:
            r = int(r * 0.20)
            g = int(g * 0.20)
            b = int(b * 0.20)

        edit_cat.append((r, g, b))

new_cat = Image.new("RGB", cat.size)
new_cat.putdata(edit_cat)

new_cat.save("dimcat.jpg")

'''
for prop in properties:
    print(f"{prop}")

print(cat.getpixel((10,100)))

# RGB "cat.mode" tells us how each pixel data is stored

whole_cat = list(cat.getdata())
print(whole_cat)

print(cat.getpixel((10,100))) # Get's the RGB at pixel column 10 and pixel row 100
'''

# RGB = [255, 255, 255]. Each of these 3 numbers represents a letter in RGB. The 1st 255 represent 'R', the 2nd 255 represent 'G', and
# the 3rd 255 represents 'B'