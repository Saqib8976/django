# print star pattern
for i in range(1, 5):
    print("*"*i)

for i in range(5, 0, -1):
    print("*"*i)


for i in range(1, 5):
    for j in range(i+1):
        print("*", end="")
    print()

for i in range(1, 5):
    for j in range(5-i):
        print("*", end="")
    print()
