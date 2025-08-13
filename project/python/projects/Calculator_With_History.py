import re
History_File = "history.txt"


def show_history():
    file = open(History_File, 'r')
    lines = file.readlines()
    if lines == 0:
        print("No history found...!")
    else:
        for line in reversed(lines):
            print(line.strip())
    file.close()


def clear_history():
    file = open(History_File, "w")
    file.close()
    print("History is cleared...!")


def save_history(equation, result):
    file = open(History_File, 'a')
    file.write(equation+"="+str(result)+'\n')
    file.close()


def calculate(user_input):
    match = re.match(
        r"\s*(\d+(?:\.\d+)?)\s*([\+\-\*/])\s*(\d+(?:\.\d+)?)\s*$", user_input)
    if not match:
        print("invalid input.!! enter valid input (eg. 8+8)")
        return

    num1 = float(match.group(1))
    op = match.group(2)
    num2 = float(match.group(3))

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 == 0:
            print("You can't divide by zero")
            return
        result = num1 / num2

    if result == int(result):
        result = int(result)
    print(f"result: {result}")
    save_history(user_input, result)


def main():
    print("---Simple calculator (type history,clear or exit)---")
    while True:
        user_input = input(
            "enter calculation (+,-,*,/) or command history , clear and exit:")
        if user_input == "exit":
            print("good bye...!")
            break
        elif user_input == "history":
            show_history()
        elif user_input == "clear":
            clear_history()
        else:
            calculate(user_input)


main()
