#Christian Flores 10/02/2021

glossary = {"Dog": "Men's best friend", "Cat": "Men's best partner", "Bird": "Men's best pana"}
for k, v in glossary.items():
    print(f"{k}: {v}")
    
glossary["fish"] = "Men's best water friend"
glossary["mosquito"] = "Men's worst enemy"
print("\n")
for k, v in glossary.items():
    print(f"{k}: {v}")
