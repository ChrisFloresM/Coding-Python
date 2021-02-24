#Christian Flores 10/02/2021
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
#Creamos una lista para guardar los iterables de forma ordenada
num_list = []
[num_list.append(num) for num in arr]

#Eliminamos elementos repetidos
setted_list = set(num_list)

#Creamos el set en un objeto lista y lo ordenamos
num_list = list(setted_list)
num_list.sort()

#Imprimimos el segundo valor mayor de la lista filtrada y ordenada
print(num_list[-2])
