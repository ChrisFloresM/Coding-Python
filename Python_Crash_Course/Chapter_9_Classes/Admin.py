#Christian Flores 14/02/2021

"""Archvio con la clase Admin"""

from User import Users as Us
class Admin(Us):

    def __init__(self, first_name, last_name, age):
        """Metodo constructor"""
        super().__init__(first_name, last_name, age)
        self.privileges = Privileges()


class Privileges:

    def __init__(self):
        """Metodo constructor"""
        self.privileges = ["Can add posts", "Can delete posts", "Can be user"]

    def show_privileges(self):
        """Metodo que muestra los privilegios de admin"""
        print("\nAdmin privileges: ")
        for privilege in self.privileges:
            print(privilege)
    