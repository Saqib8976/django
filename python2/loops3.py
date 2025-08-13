# print the multiplication table for a given number upto 10, but skip the 5th iteration

number = 5

for i in range(1, 11):
    if i == 5:
        continue
    print(f"{number}x{i}={number*i}")
