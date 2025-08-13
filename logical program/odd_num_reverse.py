num = 20
while num > 0:
    if num % 2 != 0:
        print(num)
    num -= 1
print("\n")
# another way using while
a = 19  # 10th odd number formula to find odd 2*10-1

while a > 0:
    print(a)
    a -= 2

# using for loop
# Generate the first 10 odd numbers in reverse order
# The 10th odd number is 19 (2*10 - 1)
# The 1st odd number is 1 (2*1 - 1)
# We iterate from 19 down to 1, stepping by -2 to get only odd numbers
for odd_num in range(19, 0, -2):
    print(odd_num)
