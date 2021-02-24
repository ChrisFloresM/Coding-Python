#-----------Christian Flores----01/02/2021
#Codigo que imprime oraciones con mi lista
cars = ["Spark", "Onix", "Cavalier"]
sentence_1 = f"I would like to buy a {cars[0]} as my first car"
sentence_2 = f"I would love to one day have either an {cars[1]} or a {cars[2]}"
print(sentence_1)
print(sentence_2)


lista_2 = ["Carlos", "Pepe", "Luis"]
print(lista_2)
lista_2.insert(1, "Miguel")
print(lista_2)
lista_2.append("Lola")
print(lista_2)

#Eliminar elementos de una lista
del cars[0]
print(cars)

#eliminar con .pop()
deleted_artist = lista_2.pop()
print(lista_2)
print(deleted_artist)

#.pop para un elemento específico
print(f"My favorite artist is {lista_2.pop(0).title()}")
lista_2.insert(0, "Eliot") 
print(lista_2)

#Metodo remove
to_remove = "Carlos"
lista_2.remove(to_remove)
print(lista_2)
print(f"Ya no suelo escuchar mucho a {to_remove}")
