#Christian Flores 12/02/2020

sandwich_orders = ["jamon", "cheese", "pastrami", "Tuna", "Salami","pastrami", "chicken", "pastrami"]
finished_sandwich = []

if "pastrami" in sandwich_orders:
    print("Sorry, we ran out of pastrami sandwich")
    while "pastrami" in sandwich_orders:
        sandwich_orders.remove("pastrami")
        
print("\n")
while sandwich_orders:
    sandwich_beeing_made = sandwich_orders.pop()
    print(f"I'm doing the {sandwich_beeing_made} sandwich right now")
    finished_sandwich.append(sandwich_beeing_made)

print("\n")
for sandwich in finished_sandwich:
    print(f"The {sandwich} sandwich is ready!")

