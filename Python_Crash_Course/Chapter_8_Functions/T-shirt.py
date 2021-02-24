#Christian Flores 12/02/2021

#Ejercicio 1 y 2: T-Shirt and Large Shirt
def make_shirt(size = "Large", text_to_print = "I Love Python"):
    """Print a size and a message for a shirt"""
    print(f"\nYour T-shirt will be size {size} and it will say '{text_to_print}' on it!")

make_shirt(32, "Hello World!")
make_shirt(text_to_print = "I <3 Cookies!", size = 20)
make_shirt()
make_shirt("medium")
make_shirt("Extra_large", "Don't look at me!!")

#Ejercicio 3: Cities
def describe_city(name, country = "Mexico"):
    """Print a city and its country"""
    print(f"{name.title()} is in {country.title()}")

describe_city("Colima")
describe_city("Zapopan")
describe_city("New York", country = "United States")