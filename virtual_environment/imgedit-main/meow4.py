from PIL import Image

cat = Image.open("cat.jpg")

properties = [cat.format, cat.mode, cat.size, cat.width, cat.height]

cat_pixels = cat.load()
edit_cat = []

for y in range(cat.height):
    for x in range(cat.width):
        one_pixel = cat_pixels[x, y]




# Determine the center of the image (the pixel that is right at the center of the image), and the further we go away from that center
# of the image, the darker the image becomes. (This is called a vignette)