from PIL import Image

cat = Image.open("cat.jpg")

properties = [cat.format, cat.mode, cat.size, cat.width, cat.height]

cat_pixels = cat.load()
edit_cat = []

for y in range(cat.height):
    for x in range(cat.width):
        one_pixel = cat_pixels[x, y]
        grey_val=round((one_pixel[0] + one_pixel[1] + one_pixel[2])/3)
        one_pixel = (grey_val, grey_val, grey_val)
        edit_cat.append(one_pixel)

new_cat = Image.new("RGB", cat.size)
new_cat.putdata(edit_cat)

new_cat.save("depressed_cat_#grey.jpg")