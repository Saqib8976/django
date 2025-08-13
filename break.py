i = 1
while i <= 5:
    print(i)
    if (i == 3):
        break
    i += 1

print("end of loop...")

num = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

i = 0
x = 49
while i < len(num):
    if (num[i] == x):
        print("found at index", i)
        break
    else:
        print("finding")
    i += 1
