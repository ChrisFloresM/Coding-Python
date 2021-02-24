#Christian Flores 15/02/2021

def formatted_city_name(city, country, population=""):
    """Funcion que da formato al nombre y pais de una ciudad"""
    if population:
        formatted_name = f"{city}, {country} - population {population}"
    else:
        formatted_name = f"{city}, {country}"
    return formatted_name.title()

