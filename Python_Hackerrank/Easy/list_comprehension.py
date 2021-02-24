#Chris Flores: 09/02/2021

#Ejercicio de list comprehensions

#list = [num**2 for num in (range(20))] -> list comprehension
x, y, z, n = (int(input()) for _ in range(4))
valid_permutation = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]
print(valid_permutation)
