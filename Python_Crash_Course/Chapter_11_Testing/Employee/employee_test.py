#Christian Flores 15/02/2021

import unittest

from employee import Employee

class TestEmployee(unittest.TestCase):
    """Tests para la clase Employee"""

    def setUp(self):
        """Crear una instancia de la clase"""
        self.custom_raise = 7000
        self.my_employee = Employee("Chris", "Flores", 1000)


    def test_give_default_raise(self):
        """test de un aumento por default de 5000"""
        self.my_employee.give_raise()
        self.assertEqual(self.my_employee.salary, 6000)


    def test_give_custom_raise(self):
        """test de un aumento personalizado de 7000"""
        self.my_employee.give_raise(self.custom_raise)
        self.assertEqual(self.my_employee.salary, 8000)
    
if __name__ == "__main__":
    unittest.main()

