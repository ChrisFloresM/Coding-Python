#-----------Christian Flores----08/02/2021
#Imprime los primeros 3 items de una lista
list = ["carros", "camiones", "musica", "gatos", "tiburones"]
print(f"The first three items in the list are:")
for item in list[:3]:
    print(item, end=" // ")
print("\n")
#añadiendo pizzas y copiando listas
pizzas = ["Pepperoni", "Cheddar", "tuna"]
for pizza in pizzas:
    print(f"I like {pizza.title()} pizza")
print("")
friends_pizza = pizzas[:]
pizzas.append("jamon")
friends_pizza.append("camaron")
print("My favourite pizzas are: ")
for pizza in pizzas:
    print(pizza, end = " // ")
print("\n")
print("My friend's favourite pizzas are: ")
for pizza in friends_pizza:
    print(pizza, end = " // ")
print("\n")    
