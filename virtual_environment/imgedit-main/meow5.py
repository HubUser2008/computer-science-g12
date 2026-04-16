import random

from PIL import Image

cat = Image.open("cat.jpg")

properties = [cat.format, cat.mode, cat.size, cat.width, cat.height]

cat_pixels = cat.load()
edit_cat = []

def roll(min_val, max_val):
    return random.randint(min_val, max_val)

choice = input("\n How grainy do you want your cat image to be: 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 0r 100? (Enter 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, or 100): \n")

while choice not in ["0","10","20","30","40","50","60","70","80","90","100"]:
    print("Input the correct number that the question asks, now!\n")
    choice = input("How grainy do you want your cat image to be: 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, or 100?\n")

if choice == "0":
    for y in range(cat.height):
        for x in range(cat.width):
            r, g, b = cat_pixels[x, y]

            r = roll(r - 10, r + 10)
            g = roll(g - 10, g + 10)
            b = roll(b - 10, b + 10)

            edit_cat.append((r, g, b))
    
    new_cat = Image.new("RGB", cat.size)

    new_cat.putdata(edit_cat)

    new_cat.save("not_so_grainy_cat_#not_grainy.jpg")


elif choice == "10":
    for y in range(cat.height):
        for x in range(cat.width):
            r, g, b = cat_pixels[x, y]

            r = roll(r - 10, r + 10)
            g = roll(g - 10, g + 10)
            b = roll(b - 10, b + 10)

            edit_cat.append((r, g, b))
    
    new_cat = Image.new("RGB", cat.size)

    new_cat.putdata(edit_cat)

    new_cat.save("grainy_cat_#grainy.jpg")

elif choice == "20":
    for y in range(cat.height):
        for x in range(cat.width):
            r, g, b = cat_pixels[x, y]

            r = roll(r - 20, r + 20)
            g = roll(g - 20, g + 20)
            b = roll(b - 20, b + 20)

            edit_cat.append((r, g, b))
    new_cat = Image.new("RGB", cat.size)

    new_cat.putdata(edit_cat)

    new_cat.save("grainy_cat_#grainy.jpg")

elif choice == "30":
    for y in range(cat.height):
        for x in range(cat.width):
            r, g, b = cat_pixels[x, y]

            r = roll(r - 30, r + 30)
            g = roll(g - 30, g + 30)
            b = roll(b - 30, b + 30)

            edit_cat.append((r, g, b))
    
    new_cat = Image.new("RGB", cat.size)

    new_cat.putdata(edit_cat)

    new_cat.save("grainy_cat_#grainy.jpg")

elif choice == "40":
    for y in range(cat.height):
        for x in range(cat.width):
            r, g, b = cat_pixels[x, y]

            r = roll(r - 40, r + 40)
            g = roll(g - 40, g + 40)
            b = roll(b - 40, b + 40)

            edit_cat.append((r, g, b))
    
    new_cat = Image.new("RGB", cat.size)

    new_cat.putdata(edit_cat)

    new_cat.save("grainy_cat_#grainy.jpg")

elif choice == "50":
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

elif choice == "60":
    for y in range(cat.height):
        for x in range(cat.width):
            r, g, b = cat_pixels[x, y]

            r = roll(r - 60, r + 60)
            g = roll(g - 60, g + 60)
            b = roll(b - 60, b + 60)

            edit_cat.append((r, g, b))
    
    new_cat = Image.new("RGB", cat.size)

    new_cat.putdata(edit_cat)

    new_cat.save("grainy_cat_#grainy.jpg")

elif choice == "70":
    for y in range(cat.height):
        for x in range(cat.width):
            r, g, b = cat_pixels[x, y]

            r = roll(r - 70, r + 70)
            g = roll(g - 70, g + 70)
            b = roll(b - 70, b + 70)

            edit_cat.append((r, g, b))
    
    new_cat = Image.new("RGB", cat.size)

    new_cat.putdata(edit_cat)

    new_cat.save("grainy_cat_#grainy.jpg")

elif choice == "80":
    for y in range(cat.height):
        for x in range(cat.width):
            r, g, b = cat_pixels[x, y]

            r = roll(r - 80, r + 80)
            g = roll(g - 80, g + 80)
            b = roll(b - 80, b + 80)

            edit_cat.append((r, g, b))
    
    new_cat = Image.new("RGB", cat.size)

    new_cat.putdata(edit_cat)

    new_cat.save("grainy_cat_#grainy.jpg")

elif choice == "90":
    for y in range(cat.height):
        for x in range(cat.width):
            r, g, b = cat_pixels[x, y]

            r = roll(r - 90, r + 90)
            g = roll(g - 90, g + 90)
            b = roll(b - 90, b + 90)

            edit_cat.append((r, g, b))
    
    new_cat = Image.new("RGB", cat.size)

    new_cat.putdata(edit_cat)

    new_cat.save("grainy_cat_#grainy.jpg")

elif choice == "100":
    for y in range(cat.height):
        for x in range(cat.width):
            r, g, b = cat_pixels[x, y]

            r = roll(r - 100, r + 100)
            g = roll(g - 100, g + 100)
            b = roll(b - 100, b + 100)

            edit_cat.append((r, g, b))
    
    new_cat = Image.new("RGB", cat.size)

    new_cat.putdata(edit_cat)

    new_cat.save("grainy_cat_#grainy.jpg")

# To add grain to a photo (grain filtering photo), a pixel has a chance of being altered, with "being altered" meaning that you add or
# subtract a number