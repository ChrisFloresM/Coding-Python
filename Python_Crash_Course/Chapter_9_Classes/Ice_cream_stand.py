#Christian Flores 14/02/2021
#Herencia 
class Restaurant:
    """A restaurant class here"""

    def __init__(self, restaurant_name, cuisine_type):
        """Inicializar los atributos"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Describir el restaurante"""
        print(f"\nRestaurant name is {self.restaurant_name} and its cuisine type is {self.cuisine_type}")

    def open_restaurant(self):
        """Simula que abre el restaurante"""
        print(f"\nThe resturant {self.restaurant_name} is now open!")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        """Constructor para la clase IceCreamStand"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["Chocolate", "Vanilla", "Strawberryes"]

    def display_flavor(self):
        """Metodo que muestra los sabores disponibles"""
        print("\nWe currently count with the next flavors:")
        for flavor in self.flavors:
            print(f"{flavor}")

deli_ice = IceCreamStand("Deli-Ice", "Ice Cream")
deli_ice.describe_restaurant()
deli_ice.display_flavor()


    
