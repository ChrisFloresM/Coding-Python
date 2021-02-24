#-----------Christian Flores----08/02/2021
#contar hasta 21 usando listas y for
count = list(range(1,21))
for number in count:
    print(number, end="\t")
print("")

#lista de numberos de uno a un millon e imprimiendo
#count = list(range(1, 1000001))
#for number in count:
#    print(number, end= "\t")
#print("")

#min y max de un millon asi como la suma de todos los numeros
print("")
print(f"El valor minimo es: {min(count)}")
print(f"El valor maximo es: {max(count)}")
sum = 0
for number in count:
    sum += number
print(f"La suma de los numeros es {sum}\n")

#numeros impares del 1 al 20
odds = list(range(1,21,2))
for number in odds:
    print(number)

#multiplos de 3
multiplos = list(range(3, 31, 3))
for number in multiplos:
    print(number)

#cubicos
cubos = [number**3 for number in range(1, 11)]
print(cubos)

#cubicos numero 2
numeros = list(range(1,11))
for number in numeros:
    print(number**3)

