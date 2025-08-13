# check if a number is prime or not

num = 28

is_prime = True

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
print(is_prime)