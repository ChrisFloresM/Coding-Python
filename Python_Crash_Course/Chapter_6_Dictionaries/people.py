#Christian Flores 10/02/2021
#Creando una lista de diccionarios
person_1 = {"fname": "Chris", "last_name":"Flores", "age": 22, "city": "Colima"}
person_2 = {"fname": "Luis", "last_name":"Perez", "age": 21, "city": "Durango"}
person_3 = {"fname": "Luisa", "last_name":"Sanchez", "age": 24, "city": "Coahuila"}

people = [person_1, person_2, person_3]

for person in people:
    print(f"\nname: {person['fname']}")
    print(f"last_name: {person['last_name']}")
    print(f"age: {person['age']}")
    print(f"city: {person['city']}")
