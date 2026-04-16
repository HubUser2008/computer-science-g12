import random

length = 10
my_nums=[]
for i in range(length):
    my_nums.append(random.randint(0,9))
    print(my_nums[i])

print (my_nums)

# Print occurrences using count method
for num in range(10): # This is a for loop that iterates (passes) through each number within the array which we know has a length of 10, which
# is represented as '(10)'. The loop variable 'num' takes each value from the number sequence (the array), one at a time
    print(f"Number {num}: {my_nums.count(num)} time(s)") # 'my_nums.count(num)'counts how many times that the value 'num' appears in the list
# 'my_nums'. 'count' is a built-in list method in Python; it takes one argument (in this case, 'num') and returns the number occurrences of that
# value in the list

#'print(f"Number {num}: {my_nums.count(num)} time(s)")' prints the occurrence of each number from 0-9 in a formatted string. An f-string, which
# is represented as 'f' allows you to embed expressions (like 'num' and 'my_nums.count(num) inside curly brackets '{}' in a string
# The output dynamically displays the value of num and how many times num appears in my_nums
# This loop systematically checks and prints how many times each number (from 0 to 9) appears in my_nums
