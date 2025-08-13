# check if all elements in a list are unique if a dublicate is found exit the loop and print the dublicate

l = ["apple", "banana", "orange", "banana", "mango"]

for i in l:
    if l.count(i) == 2:
        print(i)
        break

# another same way but add unique item to set until dublicate item is found

items = ["apple", "banana", "orange", "banana", "mango"]

unique_item = set()

for item in items:
    if item in unique_item:
        print(item)
        break
    unique_item.add(item)

print(unique_item)
