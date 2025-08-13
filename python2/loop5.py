# given a string , find the first non repeated character...?

input_str = "teeters"

for char in input_str:
    if input_str.count(char) == 1:
        print(f"1st non repeating character in string is {char}")
        break
