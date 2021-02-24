#Christian Flores 11/02/2021

new_person = True
while new_person:
    age = int(input("Imput the person's age: "))
    print("\n")
    if age < 3:
        print("Your ticket is free")
        new_input = input("Add a new person? Y/N: ")
        if new_input.upper() == "Y":
            new_person = True
        else:
            new_person = False
        continue
    elif age < 12:
        ticket = 10
    else:
        ticket = 15
    print(f"Your ticket is ${ticket}")
    new_input = input("Add a new person? Y/N: ")
    if new_input.upper() == "Y":
        new_person = True
    else:
        new_person = False