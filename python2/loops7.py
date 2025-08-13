# keep asking the user for input until they enter a number between 1 to 10

while True:
    num = int(input("enter the number from one to ten:"))
    if 0<num<=10:
        print(num)
        break
    else:
        print("invalid number , try again...!")
    


print("done")
