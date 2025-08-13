# import rendome module to generate choise
import random

subjects = ["sharukh khan", "amir kahan", "cat", "dog",
            "monkeys", "prime minister modi", "auto driver from mumbai"]


actions = ["launches", "cancels", "orders", "jump over the rope",
           "sleeping", "declare war on USA", "eats"]

places = ["at redfort",
          "inside parliment",
          "at india gate",
          "During ipl match",
          "in mumbai local tarin",
          "at ganga ghat",
          "a plate of samosa"
          ]

# start the headline generation
while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place = random.choice(places)

    headline = f"BREAKING NEWS: {subject} {action} {place}"
    print('\n'+headline)

    user_choice = input("do you want to generate another headline? (Yes/No):").strip().lower()
    if user_choice == "no":
        break

#print good bye message
print("\n thanks for using the fake news headline generator...!")