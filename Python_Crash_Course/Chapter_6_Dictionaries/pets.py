#Christian Flores 10/02/2021
#Diccionarios de mascotas
manchas = {"animal":"dog", "owner":"Chris" }
lucas = {"animal":"fish", "owner":"Luis"}
porfirio = {"animal":"cat", "owner":"Diana"}

pets = [manchas, lucas, porfirio]

for pet in pets:
    print(f"\nAnimal: {pet['animal'].title()}")
    print(f"Owner: {pet['owner'].title()}")
