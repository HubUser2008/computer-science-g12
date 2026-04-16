import string
import random

all_alpha = string.ascii_letters
exclude_letters = ["D", "F", "I", "O", "Q", "U"]
letters = string.ascii_letters
first_letters = ["A", "B", "C", "E", "G", "H", "J", "K", "L", "M", "N", "P", "R", "S", "T", "V", "X", "Y"]
excludefirst_letters = ["W", "Z"]

for letters in string:
    if letters:
        print("This letter/s must be avoided at all costs. Stop it now.")
    else:
        print("This ltter/s is plausible. Well done.")

# The first letter of the Canadian Postal Code cannot include W or Z

