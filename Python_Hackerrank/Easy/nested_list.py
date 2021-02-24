if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

#Crear una lista para almacenar solo los puntajes 
scores = []
[scores.append(student[1]) for student in students]

#Filtramos los valores repetidos y los ordenamos
setted_scores = set(scores)
scores = list(setted_scores)
scores.sort()
print(scores)

#Buscamos los nombres validos y los guardamso en una lista
valid_names = [student[0] for student in students if student[1] == scores[1]]

#Imprimimos los nombres correctos
valid_names.sort()
[print(name) for name in valid_names]

