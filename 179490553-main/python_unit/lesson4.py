input1 = str(input("Provide a SINGULAR word: "))
input2 = str(input("Provide another SINGULAR word: "))

#Concatenation of both inputs (input1 and input2) using addition
input3 = input1 + input2

print(input3)

#Concatenation of both inputs (input1 and input2) using 'join'
'''
input1_2 = " ".join([input1, input2])
'''
# Determine the number of vowels for an inputted word, inputted by the user
'''
def count_vowels(input1):
    vowels = ["a","e","i","o","u"]
    return sum(1 for char in input1 if char in vowels)

vowel_count = count_vowels(input1)
print(f"The word {input1} contains {vowel_count} vowel(s)")
'''
# 2nd method to determine the number of vowels for an inputted word by the user
input1.lower()
count = 0
vowels = ["a","e","i","o","u"]

for letter in input1:
    if letter in vowels:
        count+=1

print(f"There are {count} vowel(s) in the word")

# Capitalize all the letters of the word that the user inputted BY USING A SPECIFIC STRING METHOD
capitalized_word = input1.upper() #The 'upper()' string method is a specific string method in python that converts all the letters of a string
# which is a word, to uppercase. (E.g. input1 = gaming -> capitalized_word = gaming.upper() -> printf(f"The capitalized word is: {capitalized_word}"
# The return value of this example code would be "GAMING" since the 'upper()' string method capitalizes each letter of a string, which in this
# case is the word, "gaming"))
print(f"The capitalized word is: {capitalized_word}")

# Printing the middle letter of the word
if len(input1) % 2 == 0:
    middle_letters = input1[len(input1)//2 - 1 : len(input1)//2 + 1]
else:
    middle_letters = input1[len(input1)//2]

print(f"The middle letter(s) are: {middle_letters}")
