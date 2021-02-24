#Christian Flores 10/02/2021
#Diccionario de diccionarios
cities = {"Mexico": {"country": "Mexico", "population": 7, "fact":"Deliciois food"}, "Colima": {"country": "Mexico", "population": 2, "fact":"Tuba"}, "Guadalajara": {"country": "Mexico", "population": 5, "fact":"Nice weather"}}

for city, data in cities.items():
    print(f"\nCity: {city}")
    for k, v in data.items():
        print(f"\t{k}: {v}")