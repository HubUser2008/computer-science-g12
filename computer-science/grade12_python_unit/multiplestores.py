import random, string

def restock(store, item):
    # if the item is low in the store, then restock it to 50; low = less than 10
    if store[item] < 10:
        store[item] = 50
        pass

uppercase = string.ascii_uppercase
print(uppercase)
# make a list of all the stores
store_lst = []
for i in uppercase[:10]:
    store_lst.append("store"+i)
# print(store_lst)
sale = ["apples", "bananas", "cans", "durians", "eggplants", "falafels"]
stores = {}

for sto in store_lst:
    stores.update({sto:{}})
    for item in sale:
        stores[sto].update({item:random.randint(0,50)})

for store in stores.keys():
    for item in stores[store].keys():
        restock(stores[store], item)
        pass

print(stores)



'''all_stores = {"store1", "store2", "store3", "store4", "store5"}
#store1 = {"apple": 2.34, "banana": 12.00, "orange": 2.00, "beef": 15.00, "grape": 0.25, "celery": 2.00, "strawberry": 0.30}
#store2 = {"apple": 1.00, "banana": 10.00, "orange": 1.50, "beef": 12.00, "grape": 0.20, "celery": 1.50, "strawberry": 0.25}
#store3 = {"apple": 2.00, "banana": 11.00, "orange": 1.80, "beef": 14.00, "grape": 0.22, "celery": 1.80, "strawberry": 0.28}
#store4 = {"apple": 1.50, "banana": 9.00, "orange": 1.20, "beef": 10.00, "grape": 0.18, "celery": 1.20, "strawberry": 0.20}
#store5 = {"apple": 2.50, "banana": 13.00, "orange": 2.50, "beef": 16.00, "grape": 0.30, "celery": 2.50, "strawberry": 0.35}
'''
