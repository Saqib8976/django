# movies tickets priced based on age:12$ for adult (18 and over), 8$ for children. everyone gets 2$ discount on wednesday

age = int(input("enter your age:"))
day = "wednesday"

price = 12 if age > 18 else 8

if day == "wednesday":
    price -= 2

print(f"your ticket price is {price}")
