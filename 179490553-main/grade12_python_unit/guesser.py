import random

number_you_guess = int(input("Enter a number between 1 and 100: "))
random_number = random.randint(1, 100)
random_hint = random.randint(1, 20)
print("Your hint is that: your number is between", random_hint, "and", random_number)

while number_you_guess != random_number:
    if number_you_guess < random_number:
        print("Too low!")
    elif number_you_guess > random_number:
        print("Too high!")
    else: 
        break
    number_you_guess = int(input("Try again: "))
    print("You correctly guessed the right number! Amazing Job!")