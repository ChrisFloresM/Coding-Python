#Christian Flores 10/02/2021
#Diccionario de listas
favorite_palces = {"Chris": ["Japon", "Italia", "Canada"], "Diana": ["Bahamas", "Egipto", "Italia"], "Alonso": ["Mexico", "China", "Peru"]}

for name, places in favorite_palces.items():
    print(f"\n{name}'s favorite places are:")
    for place in places:
        print(f"\t{place}")
        