#Christian Flores 14/02/2021

"""Modulo que almacena la clase Dice"""

from random import randint

class Dice:
    
    def __init__(self, sides=6):
        """Metodo constructor"""
        self.sides = sides
    
    def roll_dice(self):
        """Metodo para tirar el dado"""
        print(randint(1, self.sides))

