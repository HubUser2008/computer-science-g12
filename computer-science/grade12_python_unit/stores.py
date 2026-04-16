import random, string

# The variable called "my_store" underneath, is assigned a library where the key is the name of the item and the value is the price
# of the item

my_store = {"apple": 2.34, "banana": 12.00, "orange": 2.00, "beef": 15.00, "grape": 0.25, "celery": 2.00, "strawberry": 0.30}
print(my_store.keys())
# Loop through all the items declared to be in the variable, "my_store" and discount the price of each item by 20%
# and print the new price of each item after the discount of 20% has been applied
for item in my_store.keys(): # this for loop will access each item in the variable, "my_store" and it will apply the 20% discount to each item
    my_store[item] = my_store # this line will apply the 20% discount to each item in the variable, "my_store"
    print(my_store[item])
    


# Use the shortcut, Ctrl + Alt + Down Arrow to select multiple lines and comment them out at the same time

#print(my_store.get("grape"))
#print(my_store["grape"])
#print(my_store.get("grape")["price"])
#print(my_store["grape"]["price"])