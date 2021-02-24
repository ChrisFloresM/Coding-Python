#Christian Flores 15/02/2021
import json

filename = "Chapter_10_Text_Exceptions/fav_num.txt"

try: 
    with open(filename) as f:
        number = json.load(f)
except FileNotFoundError:
    number = input("Tell me your favorite number: ")
    with open(filename, "w") as f:
        json.dump(number, f)
else:
    print(f"Your favorite number is: {number}")

