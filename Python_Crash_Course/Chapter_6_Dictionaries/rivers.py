#Christian Flores 10/02/2021

rivers = {"Nilo": "Egypt", "Bravo": "USA", "Amazonas": "Brazil"}
for k, v in rivers.items():
    print(f"The {k} runs throught {v}")

print("\nRivers: ")
for k in rivers.keys():
    print(k)
print("\nCountries: ")
for v in rivers.values():
    print(v)