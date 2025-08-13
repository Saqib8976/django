# wap to add odd numbers from 1 to 50 using loop

sum = 0
for i in range(1, 51, 2):
    sum += i

print(sum)

# now use while loop

a = 1
total = 0

while a <= 50:
    if a % 2 != 0:
        total += a
    a += 1

print(total)

# another way
i = 1
add = 0
while i <= 50:
    add += i
    i += 2
print(add)


# add first 10 odd number in reverse order

b = 20
t = 0

while b > 0:
    if b % 2 != 0:
        t += b
    b -= 1
print(t)

# using for loop
total_sum = 0
# Generate the first 10 odd numbers in reverse order
# The 10th odd number is 19 (2*10 - 1)
# The 1st odd number is 1 (2*1 - 1)
# We iterate from 19 down to 1, stepping by -2 to get only odd numbers
for odd_num in range(19, 0, -2):
    total_sum += odd_num

print(f"The sum of the first 10 odd numbers in reverse order is: {total_sum}")
