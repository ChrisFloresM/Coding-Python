#Christian Flores 12/02/2021

persons = {}
poll = True

while poll:
    name = input("\nWhat is your name: ")
    place = input("If you could visit one place in the world, where would you go?: ")

    persons[name] = place

    answer = input("Whould you like to pass the poll to another person? (yes/no): ")
    if answer.lower() == "no":
        poll = False
    
print("\n")
for name, place in persons.items():
    print(f"{name} whould like to visit {place}")

