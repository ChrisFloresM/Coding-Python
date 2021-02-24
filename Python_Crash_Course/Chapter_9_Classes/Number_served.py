#Christian Flores 13/02/2021

class Restaurant:
    """A restaurant class here"""

    def __init__(self, restaurant_name, cuisine_type):
        """Inicializar los atributos"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Describir el restaurante"""
        print(f"\nRestaurant name is {self.restaurant_name} and its cuisine type is {self.cuisine_type}")

    def open_restaurant(self):
        """Simula que abre el restaurante"""
        print(f"\nThe resturant {self.restaurant_name} is now open!")

    def set_number_served(self, served):
        """Metodo que coloca el numero de personas servidas"""
        self.number_served = served

    def increment_served(self, increment):
        """Metodo que incrementa el numero de personas servidas"""
        self.number_served += increment

restaurant = Restaurant("Los desayunos", "desayunos")
print(restaurant.number_served)
restaurant.number_served = 10
print(restaurant.number_served)
restaurant.set_number_served(5)
print(restaurant.number_served)
restaurant.increment_served(23)
print(restaurant.number_served)