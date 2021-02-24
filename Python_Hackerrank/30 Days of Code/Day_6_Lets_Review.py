#Christian Flores 15/02/2021
#Día 6: Let's Review
#Separar un string en sus componentes pares e impares

def dividir_string(my_string):
    """Funcion que divide los strings en pares e impares"""
    evens = my_string[::2]
    odds = my_string[1::2]
    return evens, odds

#Primero recibimos las entradas
T = int(input())
strings = []
[strings.append(input()) for _ in range(T)]

#Mandamos a llamar la funcion para dividir los strings en pares e impares, aplicando a cada string ingresado
for string in strings:
    evens, odds = dividir_string(string)
    print(f"{evens} {odds}")
    


