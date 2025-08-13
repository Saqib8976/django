# count the positive numbers in the given list
numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
positive_num_count = 0

for i in numbers:
    if i > 0:
        positive_num_count += 1
print("final count of positive number is", positive_num_count)
