#Christian Flores 15/02/2021

class Employee:

    def __init__(self, first_name, last_name, annual_salary):
        """Constructor de la clase"""
        self.first_name = first_name
        self.last_name = last_name
        self.salary = annual_salary


    def give_raise(self, salary_rise=5_000):
        """Dar un aumento al empleado"""
        self.salary += salary_rise

    


