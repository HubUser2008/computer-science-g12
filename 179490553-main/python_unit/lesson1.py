# In python, you do underscores when naming variables INSTEAD of capital case like you did back in C programming (e.g. name_variable_now = 10
# INSTEAD OF nameVariableNow = 10)

# The '#' symbol is used to make a comment in python
# print("I hate the public bus")
''' # the triple quotation marks (as seen to the left of this message) is used to comment out multiple lines in python
my_msg = "I hate the public bus"
print(my_msg)

a = 5
b = 7.1
c = "wow"
print(a+b)
print(a+c)
'''
# Determines if the number inputed by the user is positive or negative or zero (0)
'''num = int(input("Provide a number to analyze: "))
if num>0:
    print("Your number is positive")
elif num<0:
    print("Your number is negative")
else:
    print("Your number is 0")
'''
# This entire commented out code is the long-form way on how to determine if a year is a leap year or not
''' num = int(input("Provide a number: "))
if num%400==0:
    print("This year is a leap year")
elif num%100==0:
    print("This year is a leap year")
elif num%4==0:
    print("This year is a leap year")
else:
    print("This year is NOT a leap year")
'''
num = int(input("Provide a number: "))
if num%4 and num%400:
    print("This year is NOT a leap year")
else:
    print("This year IS a leap year")
