#Christian Flores 11/02/2021
#Día 2: Operadores
#Obtener el precio total
import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    total_tip = tip_percent * meal_cost/100 
    total_tax = tax_percent * meal_cost/100
    print(round(meal_cost + total_tip + total_tax))

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)