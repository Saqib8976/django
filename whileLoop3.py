# print the elemenets of the following list using loop [1,4,9,16,25,36,49,64,81,100]
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
i = 0
while i < len(nums):
    print(nums[i])  # to print element of list we provide  indexing num[0]
    i += 1


print(len(nums))  # return total number of element present in list


# search for a number X in this tuple using loop
num = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

i = 0
x = 49
while i < len(num):
    if (num[i] == x):
        print("found at index", i)
    else:
        print("finding")
    i += 1
