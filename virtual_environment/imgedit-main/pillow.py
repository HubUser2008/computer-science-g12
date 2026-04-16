import random  # imports random module (not used in the python programming code below, but it's available if need be)

from PIL import Image, ImageFilter # Importing the ImageFilter module from the PIL library so that I'll be able to apply the built-in 
# pillow filters to the images that I've already applied my own custom filters to

# Asks the user which filter they want to apply to the images, with a certain image corresponding to each of the following available filters
choice = input("\n Do you want the light reduction filter, \n contrast enhancement filter, \n diffusion/mist filter, \n box blur filter, \n infrared filter red, \n infrared filter green, or \n infrared filter blue? \n (Enter 'l' for light reduction filter, \n 'c' for contrast enhancement filter, \n 'b' for box blur filter, \n 'd' for diffusion/mist filter, \n 'i red' for infrared filter red, \n 'i green' for infrared filter green, or \n 'i blue' for infrared filter blue): \n")

# These 2 lines of code below just initializes the variables, "choice2" and "choice3", so that an error doesn't occur when they are
# later called in the code, as they are only assigned a value if the user inputs "l" or "i red" for the variable "choice", respectively, 
# and if the user inputs any other filter choice, then "choice2" and "choice3" will just be assigned a value of None, 
# which is what they are initialized to in the lines of code below
choice2 = None
choice3 = None

# The user chose the light reduction filter
if choice == "l":
    choice2 = input("\n Do you want the built-in detail pillow filter onto the already added light reduction filter? (Enter 'y' for yes or 'n' for no): \n")
    while choice2 not in ["y", "n"]:
        print("Input the correct letter that the question asks, now!\n")
        choice2 = input("Do you want to apply the built-in detail pillow filter onto the already added light reduction filter? (Enter 'y' for yes or 'n' for no): \n")
# The user chose the infrared red filter, so as a result of the user choosing the infrared red filter, stack #2 is initialized.
# Since my group's stack #2 was the infrared red filter with the built-in pillow edge enhancement filter, if the user chose infrared red
# filter, which they did, they'll also be asked if they want to apply the built-in edge enhancement pillow filter onto the infrared red
# filter image
if choice == "i red":
    choice3 = input("\n Do you want the built-in edge enhancer pillow filter onto the already added infrared filter? (Enter 'y' for yes or 'n' for no): \n")
    while choice3 not in ["y", "n"]:
        print("Input the correct letter that the question asks, now!\n")
        choice3 = input("Do you want to apply the built-in edge enhancer pillow filter onto the already added infrared filter? (Enter 'y' for yes or 'n' for no): \n")

while choice not in ["l", "c", "b", "d", "i red", "i green", "i blue"]: # Makes sure that the user inputs a valid letter corresponding
    # to one of the filters, and if they don't, the program will keep asking them to input the valid input so that a valid output can
    # take place
    print("Input the correct letter that the question asks, now!\n")
    choice = input("\n Do you want the light reduction filter, \n contrast enhancement filter, \n diffusion/mist filter, \n box blur filter, or \n infrared filter? \n (Enter 'l' for light reduction filter, \n 'c' for contrast enhancement filter, \n 'b' for box blur filter, \n 'd' for diffusion/mist filter, or \n 'i red' for infrared filter red, \n 'i green' for infrared filter green, or \n 'i blue' for infrared filter blue): \n")



# =========================DIFFUSION/MIST FILTER==============================

# Stores the pillow_street.jpg image in the variable "street", so that the image can be edited and manipulated through the usage of the
# variable, "street", instead of having to use the name of the image file, "pillow_street.jpg", every time I want to edit or 
# manipulate the image, which is more efficient and less prone to errors

street = Image.open("pillow_street.jpg")

# Stores the properties of the image, "street", in the variable "street_properties", so that the properties of the image can be 
# easily accessed through the variable, "street_properties"
street_properties = [street.format, street.mode, street.size, street.width, street.height]

# This loads all of the pixels from the "pillow_street.jpg" image (which is represented as the variable, "street"), for future filter 
# manipulation
street_pixels = street.load()

# This creates an empty list, which is used to store the filter manipulated pixels of the "pillow_street.jpg" image
edit_street = []

if choice == "d":
    # loops through each pixel row for each y-coordinate of the image (horizontal)
    for y in range(street.height):
        # loops through each pixel column for each x-coordinate of the image (vertical   )
        for x in range(street.width):
            # The variable, "pixel", is assigned the value of each pixel on the x and y coordinates of the image, thus allowing for the
            # RGB values of each pixel, as each pixel is currently being looped through as a result of the for loops, 
            # to be accessed and filter manipulated later
            pixel = street_pixels[x, y]
            
            # Handles both RGB and RGBA images, so that the code can work for both types of images, and if the image is an RGBA image, 
            # then the alpha value is just ignored in the filter manipulation process, 
            # and if the image is an RGB image, then the code just continues as normal
            if len(pixel) == 4:
                r, g, b, a = pixel
            else:
                r, g, b = pixel

            # This calculates the brightness of each pixel by averaging out the RGB values of said pixel
            brightness = (r + g + b) // 3

            # If the pixel is bright, meaning that the RGB average is greater than 120, then a glow effect will be created by 
            # doubling the RGB values of the pixel that has a brightness (RGB average) greater than 120, making the bright pixels
            # even brighter, which will result in a glow effect being created
            if brightness > 120:
                r = int(min(255, r * 2.0))
                g = int(min(255, g * 2.0))
                b = int(min(255, b * 2.0))

            # This reduces all the rgb values of each looped through pixel of the image to 70% of its original value, which will in turn,
            # create a misty/diffused effect, as the colours and shades of the image, as a result of reducing the rgb values of each
            # pixel by 30%, will be more muted and less vibrant, ultimately creating a misty/diffused effect
            r = int(r * 0.7)
            g = int(g * 0.7)
            b = int(b * 0.7)

        # A further diffusion will take place by blending the current pixel with its neighboring bottom-left pixel
            if x > 0 and y > 0:
                # This determines the RGB values of the neighboring bottom-left pixel to the current pixel that is being looped through
                neighbor_pixel = street_pixels[x-1, y-1]
                # This handles both RGB and RGBA images, so that the code can work for both types of images, and if the image is an RGBA image,
                # then the alpha value of the neighboring pixel is just ignored in the filter manipulation process,
                # and if the image is an RGB image, then the code just continues as normal
                if len(neighbor_pixel) == 4:
                    r2, g2, b2, a2 = neighbor_pixel
                else:
                    r2, g2, b2 = neighbor_pixel
                # This averages out the RGB values of the current pixel with the RGB values of the bottom-left neighboring pixel, which
                # creates the diffusion effect filter
                r = int((r + r2) / 2)
                g = int((g + g2) / 2)
                b = int((b + b2) / 2)

            # This just ensures that the rgb values of each pixel, stays within the valid RGB range of 0-255 when the filter manipulations
            # of the RGB values take place, so that the filter manipulations don't result in any invalud RGB values for each of the pixels
            # that are being looped through
            r = min(255, max(0, r))
            g = min(255, max(0, g))
            b = min(255, max(0, b))

            # This adds the modified RGB values of each pixel to the empty list that was originally called as "edit_street"
            edit_street.append((r, g, b))

    # Creates a new blank image that is the same size as the original image
    new_street = Image.new("RGB", street.size)

    # Inputs the new RGB values of the pixels of the original image into the new blank image
    new_street.putdata(edit_street)

    # Saves the new RGB value modified image as the name, "pillow_diffusion_mist_filter.jpg"
    new_street.save("pillow_diffusion_mist_filter.jpg")

    
    # BOX BLUR FILTER

# Opens the image called "pillow_box_city.jpg" and stores its opening in the variable called "box"
box = Image.open("pillow_box_city.jpg")

# Converts each of the pixels to strictly RGB if necessary, so this ultimately removes the alpha channel from the image if the image is
# an RGBA image, so that the A part will be eliminated from each looped through pixel in the image, resulting in only the RGB values
# being present
if box.mode == 'RGBA':
    box = box.convert('RGB')

# Stores the image's properties as a list in the variable, "box_properties", so that the properties of the image can be easily accessed
# by just calling the variable, "box_properties", instead of having to call each of the properties of the image separately
box_properties = [box.format, box.mode, box.size, box.width, box.height]

# loads all of the pixels from the "pillow_box_city.jpg" image (which is represented as the variable, "box"), for the future 
# filter manipulation python programming process that will take place below
box_pixels = box.load()

# Creates an empty list that will later be used to store the modified filtered pixels of the image
edit_box = []

if choice == "b":
    for y in range(box.height):
        for x in range(box.width):
            r_total = 0
            g_total = 0
            b_total = 0
            count = 0 # This variable, "count", will be used to track the number of surrounding pixels that will be averaged for each
            # of the looped through pixels (which are all of the pixels of the image)

            # Uses a for loop to loop through 3x3 neighboring pixels (including the current pixel), with dy representing the change in
            # y value while dx represents the change in x value, so that the RGB values of the surrounding pixels can be averaged, thus
            # resulting in the creation of the box blur filter
            for dy in [-1, 0, 1]: # Moves down one pixel, stays on the same pixel, and moves up one pixel, hence the 3x3 grid
                for dx in [-1, 0, 1]:
                    nx = x + dx # The x value of the current pixel added onto the change in x value, which is represented as dx, thus giving the x-position of the neighboring pixel
                    ny = y + dy # The y value of the current pixel added onto the change in y value, which is represented as dy, thus giving the y-position of the neighboring pixel

                    # This checks to see if the neighboring pixel is within the bounds of the image, so that an error doesn't occur
                    # when trying to access the RGB values of a neighboring pixel
                    if 0 <= nx < box.width and 0 <= ny < box.height:
                        r, g, b = box_pixels[nx, ny]
                        r_total += r
                        g_total += g
                        b_total += b
                        count += 1

            # Average the surrounding RGB values of the pixels, to give off the box blur filter effect for each looped through pixel
            r = int(r_total / count)
            g = int(g_total / count)
            b = int(b_total / count)

            # Adds each box blur modified pixel to the empty list, that's represented as the variable, "edit_box", thus creating a 
            # whole list of the box blur modified pixels for the image, which will then be used to create the new box blur filtered image
            edit_box.append((r, g, b))

    # Create new blurred image
    new_box = Image.new("RGB", box.size)

    new_box.putdata(edit_box)

    new_box.save("pillow_box_blur_filter.jpg")

# LIGHT REDUCTION FILTER

city = Image.open("pillow_city_night_skyline.jpeg")

# Convert to RGB if necessary
if city.mode == 'RGBA':
    city = city.convert('RGB')

city_properties = [city.format, city.mode, city.size, city.width, city.height]

city_pixels = city.load()

edit_city = []

if choice == "l":
    for y in range(city.height):
        for x in range(city.width):
            # Get's the RGB values of each pixel that is being looped through
            r, g, b = city_pixels[x, y]

            # Detects the pixels that are 'warm', so the pixels that have a high red value, a moderately high green value, and a low
            # blue value, which are the pixels that are light pollution. Underneath, these 'warm' RGB values will be reduced to 
            # create the light reduction filter, as the red and green values will be reduced, while the blue values will be boosted
            if r > 100 and g > 80 and b < 160:
                r = int(r * 0.2)   # reduces red colours and red shades by 80%, to remove some light pollution
                g = int(g * 0.3)   # reduces green colours and red shades by 70%, to remove some light pollution
                b = int(min(255, b * 1.8))   # boosts the blue colours and blue shades by 80%
            
            # Global cool-tone shift (applies to ALL pixels)
            r = int(r * 0.7) # Reduces red colours and red shades by 30%
            g = int(g * 0.8) # Reduces green colours and green shades by 20%
            b = int(min(255, b * 1.3)) # Increases blue colours and blue shades by 30%

            # Makes sure that each RGB value that has been light reducted filtered, is within the valid RGB range of 0-255, so that
            # no error takes place once each looped through pixel of the image is modified by the light reduction filter python programming
            # above
            r = min(255, max(0, r))
            g = min(255, max(0, g))
            b = min(255, max(0, b))

            # Adds the modified RGB values of each pixel of the image into the empty list, "edit_city." This empty list that is now filled
            # with new light reducted RGB values, will then be added to the new blank image below that is the same size as the original
            # image, to ultimately create the new light reduction filtered image
            edit_city.append((r, g, b))

    new_city = Image.new("RGB", city.size)

    new_city.putdata(edit_city)

    new_city.save("pillow_light_pollution_reduction_city_filter.jpg")

    if choice2 == "y": # If the user says yes to the question, "Do you want the built-in detail pillow filter added onto the already
        # added light reduction filter?", then the built-in detail pillow filter will be added onto the "new_city" image, which is the 
        # name of the variable that originally created the new blank image that was the same size as the orginal image; then this new
        # blank image had the light reduction filtered RGB values added to it, so the "new_city" variable then represented the overall
        # new light reduction filtered image, so the code, "new_city = new_city.filter(ImageFilter.DETAIL)", applies the built-in 
        # detail pillow filter onto the light reduction filtered image
        new_city = new_city.filter(ImageFilter.DETAIL)

        new_city.save("pillow_light_pollution_reduction_city_filter_with_detail_filter.jpg")
    
    elif choice2 == "n":
        pass


# COLOUR ENHANCEMENT FILTER

colour = Image.open("pillow_colour.jpeg")

# Convert to RGB if necessary
if colour.mode == 'RGBA':
    colour = colour.convert('RGB')

colour_properties = [colour.format, colour.mode, colour.size, colour.width, colour.height]

colour_pixels = colour.load()  # Load pixel data

edit_colour = []  # List to store modified pixels

if choice == "c":  # Use "c" since your input uses 'c' for this filter
    for y in range(colour.height):
        for x in range(colour.width):
            r, g, b = colour_pixels[x, y]  # Get pixel RGB values

            # COLOUR ENHANCEMENT LOGIC

            # Increase saturation by pushing values away from average
            avg = (r + g + b) / 3

            r = int(r + (r - avg) * 2.0)  # Enhances the red colours and red shades by pushing the red RGB values away from the 
            # average RGB value, making the red colours and red shades to be more vibrant
            g = int(g + (g - avg) * 2.0)  # Enhance the green colours and green shades by pushing the green RGB values away from the 
            # average RGB value, making the green colours and green shades to become more vibrant
            b = int(b + (b - avg) * 2.0)  # Enhance the blue colours and blue shades by pushing the blue RGB values away from the 
            # average RGB values, making the blue colours and blue shades to become more vibrant

            # Step 2: Increase contrast (centered at 128)
            r = (r - 128) * 1.6 + 128
            g = (g - 128) * 1.6 + 128
            b = (b - 128) * 1.6 + 128

            # Slight brightness boost
            r = int(r * 1.2)
            g = int(g * 1.2)
            b = int(b * 1.2)

            # Clamp values between 0–255
            r = min(255, max(0, r))
            g = min(255, max(0, g))
            b = min(255, max(0, b))

            edit_colour.append((r, g, b))  # Store modified pixel

    new_colour = Image.new("RGB", colour.size)  # Create new image

    new_colour.putdata(edit_colour)  # Apply modified pixels

    new_colour.save("pillow_colour_enhancement_filter.jpg")  # Save result

    # INFRARED FILTER RED VERSION

# This a helper function that I created, to make it easier to restrict the RGB values of the pixels to be no less than 0 and no more than 255,
# so that the RGB values of the pixels don't go out of the valid RGB pixel range of 0-255, which if it did, an error would take place
# when trying to filter manipulate an image 
def clamp(value):
    return max(0, min(255, int(value)))

# ==================== INFRARED RED FILTER ====================
if choice == "i red":
    Thermal = Image.open("pillow_man.jpg")
    if Thermal.mode == 'RGBA': # Since the image was previously declared as the variable, "Thermal", the line of code 
        # "if Thermal.mode == 'RGBA':" checks to see if the image is an RGBA image, and if it is an RGBA image, then the image is 
        # converted into an RGB image, so the A (which is the alpha channel), is removed from the image, ultimately only
        # leaving RGB values for each pixel of the image
        Thermal = Thermal.convert('RGB')
    
    Therm_pixels = Thermal.load()
    edit_Thermal = []
    
    for y in range(Thermal.height):
        for x in range(Thermal.width):
            # Get's the RGB values of each looped through pixel
            pixel = Therm_pixels[x, y]
            r, g, b = pixel[0], pixel[1], pixel[2]
            
            # Calculates the average brightness of each looped through pixel by adding all 3 RGB values of a singular pixel together and 
            # then obviously dividing by 3 to get the average overall brightness of that singular pixel (which this will occur for each
            # looped through pixel of the image)
            avg = (r + g + b) // 3
            
            if avg <= 20:
                # If the average brightness of any singular pixel in the image is less than or equal to 20, then the r value in the 
                # RGB of the pixel, becomes the average value, while the g and b values in the RGB of the pixel becomes 0.
                r_new = avg
                g_new = 0
                b_new = 0
            elif avg <= 50:
                # If the average brightness of any singular pixel in the image is less than or equal to 50 but is greater than 20, then the
                # r value in the RGB of the pixel, becomes the average brightness calculated plus 100 added on, while the g and b values
                # in the RGB of the pixel becomes the average brightness of the pixel that was initially calculated divided by 3 and divided
                # by 4, in respective order (g value first, and b value second)
                r_new = avg + 100
                g_new = avg // 3
                b_new = avg // 4
            else:
                # If the average brightness of any singular pixel in the image is more than 50, then the r value in the RGB of the pixel
                # becomes whatever the original r value of the pixel was, plus 120 added on, with its value being restricted to be no more
                # than 255, so that no errors occur

                # For the g value in the RGB of the pixel, it becomes whatever the original g value of the RGB of the pixel originally was,
                # minus 80, with its value being restricted to be no less than 0, so that no errors occur

                # For the b value in the RGB of the pixel, it becomes whatever the original b value of the RGB of the pixel originally was,
                # minus 100, with its value being restricted to be no less than 0, so that no errors occur
                r_new = min(255, r + 120)
                g_new = max(0, g - 80)
                b_new = max(0, b - 100)
            
            edit_Thermal.append((clamp(r_new), clamp(g_new), clamp(b_new))) # The clamp function that I created above, is used here
            # just to FULLY ENSURE that none of the new RGB values as a result of the filter manipulation python programming above, is 
            # out of the plausible RGB value range of 0-255, so that no errors occur when trying to create the new infrared red filtered image
    
    outImage = Image.new("RGB", Thermal.size) # Creates a new blank image that is the same size as the original image, which will 
    # then be filled with the new RGB values of the pixels
    outImage.putdata(edit_Thermal) # This puts the new RGB values of the pixels, which are stored in the empty list that were defined 
    # as the variable, "edit_Thermal", into the new blank image, resulting in the creation of the new infrared red filtered image
    outImage.save("pillow_man_infrared_Red.jpg") # Saves the image as a .jpg file, with the name "pillow_man_infrared_Red.jpg"

# ==================== INFRARED GREEN FILTER ====================
elif choice == "i green":
    Thermal2 = Image.open("pillow_man.jpg")
    if Thermal2.mode == 'RGBA':
        Thermal2 = Thermal2.convert('RGB')
    
    Therm2_pixels = Thermal2.load()
    edit_Thermal2 = []
    
    for y in range(Thermal2.height):
        for x in range(Thermal2.width):
            pixel = Therm2_pixels[x, y]
            r, g, b = pixel[0], pixel[1], pixel[2]
            
            avg = (r + g + b) // 3 # Determines the average of the RGB values of each looped through pixel, which represents the 
            # brightness of each looped through pixel since the average of all 3 RGB values of a pixel, is the brightness of that pixel
            
            if avg <= 20:
                # If the average calculated RGB values (brightness) of any singular pixel in the image is less than or equal to 20, then the r value
                # of that singular pixel becomes 0, the g value becomes the brightness value, and the b value becomes 0, which will all
                # result in the dark areas of the image to become green coloured and green shaded
                r_new = 0
                g_new = avg
                b_new = 0
            elif avg <= 50:
                # If the average calculated RGB values (brightness) of any singular pixel in the iamge is less than or equal to 50
                # while being greater than 20, then the r value of that singular pixel becomes the average RGB value divided by 3,
                # the g value becomes the average RGB value (brightness) of the pixel plus 100, and the b value becomes the average RGB value
                # (brightness) of the pixel divided by 4, which will all result in the dark to mid areas of the image to become green coloured
                # and green shaded
                r_new = avg // 3
                g_new = avg + 100
                b_new = avg // 4
            else:
                # If the average calculated RGB values (brightness) of any singular pixel in the image is more than 50, then the r value of that 
                # singular pixel becomes the original r value of the pixel minus 80, with its value being restricted to be no less than 
                # 0, so that no errors occur

                # the g value of the pixel becomes the original g value of the pixel plus 120, with its value being restricted to be no
                # more than 255, so that no errors occur

                # the b value of the pixel becomes the original b value of the pixel minus 100, with its value being restricted to be no
                # less than 0, so that no errors occur
                r_new = max(0, r - 80)
                g_new = min(255, g + 120)
                b_new = max(0, b - 100)
            
            edit_Thermal2.append((clamp(r_new), clamp(g_new), clamp(b_new))) # The clamp function that I created above, is used here
            # just to FULLY ENSURE that none of the new RGB values as a result of the filter manipulation python programming above, is 
            # out of the plausible RGB value range of 0-255, so that no errors occur when trying to create the new infrared green 
            # filtered image
    
    outImage2 = Image.new("RGB", Thermal2.size) # Opens a new blank image that is the same size as the original image, as seen in the
    # "Thermal2.size" part of this line of code, which will then be filled with the new RGB values of the pixels which were gotten from
    # the filter manipulation python programming above, to create the new infrared green filtered image
    outImage2.putdata(edit_Thermal2) # This puts the new RGB values of the pixels, which are stored in the empty list that were 
    # defined as the variable, "edit_Thermal2", into the new blank image, resulting in the creation of the new infrared green filtered image
    outImage2.save("pillow_man_infrared_Green.jpg") # Saves the new infrared green filtered image as a .jpg file, with the name, 
    # "pillow_man_infrared_Green"

# ==================== INFRARED BLUE FILTER ====================
elif choice == "i blue":
    Thermal4 = Image.open("pillow_man.jpg")
    if Thermal4.mode == 'RGBA':
        Thermal4 = Thermal4.convert('RGB')
    
    Therm4_pixels = Thermal4.load()
    edit_Thermal4 = []
    
    for y in range(Thermal4.height):
        for x in range(Thermal4.width):
            pixel = Therm4_pixels[x, y]
            r, g, b = pixel[0], pixel[1], pixel[2]
            
            avg = (r + g + b) // 3 # Calculates the average RGB value of each looped through pixel, which represents the brightness of
            # each singular pixel
            
            if avg <= 20:
                # If the average RGB value (brightness) of any singular pixel in the image is less than or equal to 20, then both the r
                # and g values of that singular pixel become 0, while the b value becomes the average RGB value (brightness) of that
                # pixel
                r_new = 0
                g_new = 0
                b_new = avg
            elif avg <= 50:
                # If the average RGB value (brightness) of any singular pixel in the image is less than or equal to 50 while being
                # greater than 20, then the r value of that singular pixel becomes the average RGB value (brightness) of that pixel
                # divided by 4. The g value becomes the average RGB value (brightness) of that pixel divided by 3. The b value becomes
                # the average RGB value (brightness) of that pixel plus 100, which will all result in the dark to mid areas of the image
                # to become blue coloured and blue shaded
                r_new = avg // 4
                g_new = avg // 3
                b_new = avg + 100
            else:
                # If the average RGB value (brightness) of any singular pixel in the image is more than 50, then the r value of that 
                # singular pixel becomes the original r value of the pixel minus 100, with its value being restricted to be no less than 0
                # so that no errors occur. The g value of that singular pixel becomes the original g value of the pixel minus 80, with 
                # its value being restricted to be no less than 0, so that no errors occur. The b value of that singular pixel becomes the
                # original b value of the pixel plus 120, with its value being restricted to be no more than 255, so that no errors occur
                r_new = max(0, r - 100)
                g_new = max(0, g - 80)
                b_new = min(255, b + 120)
            
            edit_Thermal4.append((clamp(r_new), clamp(g_new), clamp(b_new))) # The clamp function that I created above, is used here just to
            # FULLY ENSURE that none of the new RGB values that were created from the filter python programming above, are out of the plausible
            # RGB value range of 0-255, so that no errors occur when trying to create the new infrared blue filtered image
    
    outImage4 = Image.new("RGB", Thermal4.size)
    outImage4.putdata(edit_Thermal4)
    outImage4.save("pillow_infrared_man_Blue.jpg")

# INFRARED PILLOW IN-BUILT EDGE ENHANCEMENT FILTER ONLY FOR THE RED VERSION OF THE INFRARED FILTER

if choice == "i red" and choice3 == "y":
    Thermal = Image.open("pillow_man.jpg")
    if Thermal.mode == 'RGBA':
        Thermal = Thermal.convert('RGB')

    Thermal_properties = [Thermal.format, Thermal.mode, Thermal.size, Thermal.width, Thermal.height]
    
    Therm_pixels = Thermal.load()
    
    edit_Thermal = []

    weightings = [.5, .4, .1]

    for y in range(Thermal.height):
        for x in range(Thermal.width):
            # Get's RGB values of each looped through pixel in the image
            pixel = Therm_pixels[x, y]
            r = pixel[0]
            g = pixel[1]
            b = pixel[2]
            
            # Calculate average of strictly the R and G values of each looped through pixel (the red and green values)
            avg = int((r + g) / 2) 
            
            # This applies the previous infrared red filter python programming logic that was used above, but this time, it's solely based
            # on the red and green values of each pixel, as the average that was calculated is strictly based on the red and green values
            # of the pixel
            if (r + g) / 2 <= 20:
                # If the average of the red and green values of any singular pixel in the image is less than or equal to 20, then the r
                # values of that singular pixel becomes the original b value of the pixel, while the g and b values of that singular pixel
                # becomes 0, which will result in the dark areas of the image to become red coloured and red shaded
                r = b
                g = 0
                b = 0
            elif (r + g) / 2 <= 25:
                # If the average of the red and green values of any singular pixel in the image is less than or equal to 25 while being
                # greater than 20, then the r value of that singular pixel becomes the original b value of the pixel minus 15, while the
                # green and blue values of that singular pixel becomes the average of the red and green values of that pixel, which will
                # result in the dark areas of the image to become red coloured and red shaded, but with a slightly less intense red colour
                # and red shade than the if statement above
                r = b - 15
                g = avg
                b = avg
            elif (r + g) / 2 <= 30:
                # If the average of the red and green values of any singular pixel in the image is less than or equal to 30 while being
                # greater than 25, then the r value of that singular pixel becomes the original b value of that same pixel minus 30, 
                # while the g and b values of that singular pixel becomes the average of the red and green values of that pixel,
                # which will all result in the dark areas of the image to become red coloured and red shaded, but with a slightly less
                # intense red colour and red shade than the if statement above, since the r value is reduced by 30 here instead of by 15
                # as seen in the above if statement
                r = b - 30
                g = avg
                b = avg
            elif (r + g) / 2 <= 35:
                # If the average of the red and green values of any singular pixel in the image is less than or equal to 35 while 
                # being greater than 30, then the r value of that singular pixel becomes the original b value of that same pixel 
                # minus 45, while the g and b values of that singular pixel becomes the average of the red and green values of that 
                # pixel, which will all result in the dark areas of the image to become red coloured and red shaded, but with a 
                # slightly less intense red colour and red shade than the if statement above, since the r value is reduced by 45 here 
                # instead of by 30 as seen in the above if statement
                r = b - 45
                g = avg
                b = avg
            elif (r + g) / 2 <= 40:
                # If the average of the red and green values of any singular pixel in the image is less than or equal to 40 while 
                # being greater than 35, then the r value of that singular pixel becomes the original b value of that same pixel 
                # minus 60, while the g and b values of that singular pixel becomes the average of the red and green values of that 
                # pixel, which will all result in the dark areas of the image to become red coloured and red shaded, but with a 
                # slightly less intense red colour and red shade than the if statement above, since the r value is reduced by 60 here 
                # instead of by 45 as seen in the above if statement
                r = b - 60
                g = avg
                b = avg
            elif (r + g) / 2 <= 45:
                # If the average of the red and green values of any singular pixel in the image is less than or equal to 45 while 
                # being greater than 40, then the r value of that singular pixel becomes the original b value of that same pixel 
                # minus 75, while the g and b values of that singular pixel becomes the average of the red and green values of that 
                # pixel, which will all result in the dark areas of the image to become red coloured and red shaded, but with a 
                # slightly less intense red colour and red shade than the if statement above, since the r value is reduced by 75 here 
                # instead of by 60 as seen in the above if statement
                r = b - 75
                g = avg
                b = avg
            elif (r + g) / 2 <= 50:
                # If the average of the red and green values of any singular pixel in the image is less than or equal to 50 while 
                # being greater than 45, then the r value of that singular pixel becomes the original b value of that same pixel 
                # minus 90, while the g and b values of that singular pixel becomes the average of the red and green values of that 
                # pixel, which will all result in the dark areas of the image to become red coloured and red shaded, but with a 
                # slightly less intense red colour and red shade than the if statement above, since the r value is reduced by 90 here 
                # instead of by 75 as seen in the above if statement
                r = b - 90
                g = avg
                b = avg
            else:
                # If the average of the red and green values of any singular pixel, that is being looped through in the image, is 
                # more than 50, then the r, g, and b values of that singular pixel becomes the integer value of the original r value of the pixel
                # multiplied by 0.6, plus the original b value of the pixel multiplied by 0.3, plus the original g value of the pixel
                # multiplied by 0.1, which will all result in the bright areas of the image becoming red coloured and red shaded
                totpixel = (r * 0.6 + b * 0.3 + g * 0.1)
                r = int(totpixel)
                g = int(totpixel)
                b = int(totpixel)
            
            # Used to make sure that the new modified RGB values of each pixel in the soon to be new image, will be no less than 0 and
            # no more than 255, so that no error occurs, as 0-255 is the valid RGB value range for each pixel of an image
            r = max(0, min(255, r))
            g = max(0, min(255, g))
            b = max(0, min(255, b))
            
            # Adds the new, modified RGB values of each looped through pixel into the empty list that was initially defined as the 
            # variable, "edit_Thermal", which will later be used to create the new filtered image
            edit_Thermal.append((r, g, b))

    # Creates a new blank image that is the same size as the original image
    outImage5 = Image.new("RGB", Thermal.size)
    outImage5.putdata(edit_Thermal) # Inputs the new, modified RGB values of each looped through pixel that was originally stored in
    # the empty list, into the new blank image that is the same size as the original image, resulting in the creation of the new 
    # infrared red filtered image
    
    # This applies the built-in edge enhance pillow filter onto the new infrared red filtered image, which will result in the edges of
    # the image to be enhanced, thus creating the effect of the infrared red filter to be more intense and more visible
    outImage5 = outImage5.filter(ImageFilter.EDGE_ENHANCE)
    
    # Saves the new, infrared red filtered image with the built-in edge enhance pillow filter applied onto it, as a .jpg file,
    # with the name of the file being "pillow_man_infrared_red_filter_with_edge_enhance_filter.jpg"
    outImage5.save("pillow_man_infrared_red_filter_with_edge_enhance_filter.jpg")