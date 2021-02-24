#Christian Flores 12/02/2021

def build_profile(name, last_name, **profile):
    """Funcion que crea un diccionario con mi perfil"""
    profile["name"] = name
    profile["last name"] = last_name
    print(profile)

build_profile("Christian", "Flores", Hobbie = "Videogames", Age = 22, Gender = "Male")
