x=0
#Fizz buzz, Fizz on numbers divisible by 3, Buzz on numbers divisible by 5, and Fizz Buzz on numbers divisible by 3 and 5
''' while x<31:
    if x%3==0:
        print("Fizz")
    elif x%5==0:
        print("Buzz")
    elif x%3==0 and x%5==0:
        print("Fizz Buzz")
    else:
        print(x)
    x+=1
''' # "immutable" means that something can't change its form, so a range function is an immutable sequence type, meaning that a range function
# cannot change its form
# x = range(2, 172, 3) (This range function starts at 2, adds up by 3 each time until it get's as numerically close to 172 without being exactly
# 172 or passing it. The middle number of a range is the maximum numerical value of the range function that the last number cannot be equal to
# or exceed. For this range function, as each integer is getting added by 3 each time, the last number cannot be equal to or greater than 172)
# for n in x:
#    print(n)

x = range(5, 172, 7)
counter = 0
for n in x: if counter < 2:
    counter+=1
    print(n)
