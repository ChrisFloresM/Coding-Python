#Christian Flores 14/02/2021

"""Codigo que almacena la clase Users"""

class Users:

    #Este es el método constructor
    def __init__(self, first_name, last_name, age):
        """Inicializar atributos del usuario"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        print("\nUser information: ")
        print(f"first name: {self.first_name}")
        print(f"last name: {self.last_name}")
        print(f"age: {self.age}")

    def greet_user(self):
        print(f"Hi {self.first_name} {self.last_name}, have a good day today!")