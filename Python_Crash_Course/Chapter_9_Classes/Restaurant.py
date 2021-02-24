#Christian Flores 13/02/2021

"""Archivo con la clase Restaurant"""

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