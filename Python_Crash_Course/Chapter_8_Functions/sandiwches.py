#Christian Flores 12/02/2021

def make_sandwich(*items):
    print("\n")
    for item in items:
        print(f"Adding: {item}")
    print("Your sandwich is ready!")

make_sandwich("Jamon", "Queso", "Mayonesa", "Lechuga", "jitomate", "Pollo")
make_sandwich("Salami", "Mayonesa", "Aderezo", "BBQ", "Pepinillos")


