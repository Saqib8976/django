print("Welcome to my computer quiz...!")

playing = input("Do you want to play? (yes or no): ").lower()


if playing != "yes":
    print("okay good bye :( ")
    quit()

print("okay lets play :)")
score=0

answer = input("what does CPU stand for? ").lower()

if answer == "central processing unit":
    print("answer is correct!")
    score+=1
else:
    print("answer is incorrect!")


answer = input("what does GPU stands for? ").lower()

if answer == "graphics processing unit":
    print("answer is correct!")
    score+=1
else:
    print("answer is incorrect!")



answer = input("what does RAM stands for? ").lower()

if answer == "rendom access memory":
    print("answer is correct!")
    score+=1
else:
    print("answer is incorrect!")



answer = input("what does PSU stands for? ").lower()

if answer == "power supply":
    print("answer is correct!")
    score+=1
else:
    print("answer is incorrect!")

print("You got "+str(score)+" answers correct...!")
print("You got "+str((score/4)*100)+"%")    # 4 is total questions asked , here we calculate percentage
