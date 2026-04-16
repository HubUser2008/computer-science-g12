fruits = ["apple", "orange", "grape", "mango", "watermelon", "banana"]
''' print(fruits)
'''
# using list methods, you have to use list.method(whatever you're trying to do (element within the array)
# Example seen below:
fruits.remove("banana")
''' print(fruits)
'''

fruits.insert(1, "cucumber") # '1' represents the index number of the array that you want to put your specified option in. Index number 1 of this
# array is between "apple" and "orange" since "apple" represents index number 0 and "orange" represents index number 2
''' print(fruits)
'''

check_basket = input("What fruit are you looking for?: ")
'''
for fruit in fruits:
    if check_basket == fruit:
        print(check_basket, "is in the basket")
    else:
        print("That fruit is not in the basket for now")
        fruits.insert(fruit)
        print(check_basket, "is now in the basket")
'''
if check_basket in fruits:
    print("The fruit is there")
else:
    fruits.insert(3, check_basket) #".append" is a function in python that adds another element to an array
print(fruits)

