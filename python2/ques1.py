# classify a person's age group child(<13) teanager(13-19) adult(20-59) and senior(60+)

person = int(input("enter your age: "))
if person < 13:
    print("you are child.")
elif 13 <= person <= 19:
    print("teanager...!")
elif 20 <= person <= 59:
    print("adult...!")
else:
    print("senior...!")
