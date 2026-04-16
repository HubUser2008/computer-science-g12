# Generate 7 letters and check if a word is produced once 7 letters has been generated. If the word is valid, print "Valid word"
# if the word is not valid, print "Not a valid word".

import random

# Generate 7 letters
def generate_letters():
    letters = ["E", "V", "I", "D", "E", "N", "T"]
    return random.sample(letters, 7)

# Check if word appears in chronological order
def check_word(word, random_letters):
    word = word.upper()
    
    letter_index = 0
    for letter in random_letters:
        if letter == word[letter_index]:
            letter_index += 1
            if letter_index == len(word):
                print("Valid word")
                return True
    
    print("Not a valid word")
    return False


# MAIN PROGRAM
random_letters = generate_letters()
print("The letters generated are:", random_letters)

user_word = input("Enter a word: ")
check_word(user_word, random_letters)
