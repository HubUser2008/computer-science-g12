import math

import math as mt # This shortens the name of the imported "math". It's just the same thing as math but now math is aka mt (also known as "mt")
# This line of code just gives "math" a nickname which is "mt" to shorten the code and to make it so that you don't have to type math each time
# whenever you want to use a function for math

# from math import * - THIS takes all the math functions and acts as if the entire library is in your file, with the file being "funcs.py" in this
# case.

# print(mt.ceil(0.00000000000000000001)) - THE ".ceil()" function alwyas ROUNDS up. It takes a number and rounds up to the nearest integer
# It doesn't follow the normal rounding rules of only rounding up at 0.5 or higher, it ALWAYS ROUNDS UP
def cousinprime(num1, num2): #'cousinprime' are prime numbers that differ by 4 (e.g. 7 and 11, and 13 and 17)
    if (num2 - num1)%4==0:
        print(f"{num1} and {num2} are cousinprimes")
    else:
        print(f"{num1} and {num2} are not cousineprimes")
        pass

#def modulus

if __name__ == '__main__': # Defines thie file as the main file for these functions to run, so therefore, even if this file is called in another
    # file (as it's called in the 'functiontest.py' file), it'll only run the specific return values that are identified with this line of code
    # while the other file (the 'functiontest.py' file) will only run the specific return value that was typed in the 'functiontest.py'
    # This specific line of code is called a "main specific testing"
    cousinprime(25,29)
    cousinprime(30,34)
    print(mt.ceil(0.00000000000000000001))
