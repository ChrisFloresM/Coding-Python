#Christian Flores 11/02/2021
topping = ""
while topping != "quit":
    request = "\nType a new topping for your pizza"
    quit_advice = " or ype quit to finish adding toppings: "
    topping = input(request+quit_advice)
    if topping != "quit":
        print(f"\nAdding {topping} to your pizza")
