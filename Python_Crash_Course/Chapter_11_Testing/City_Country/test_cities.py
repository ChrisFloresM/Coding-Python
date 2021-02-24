#Christian Flores 15/02/2021

import unittest

from city_functions import formatted_city_name as fcn

class FormattedCityTestCase(unittest.TestCase):
    """Test for city_functions.py"""

    def test_city_country(self):
        """Do 'Santiago, Chile' work?"""
        formatted_output = fcn("santiago", "chile")
        self.assertEqual(formatted_output, "Santiago, Chile")


    def test_city_country_population(self):
        """Do 'Santiago, Chile - population 5000000' work?"""
        formatted_output = fcn("santiago", "chile", 5000000)
        self.assertEqual(formatted_output, "Santiago, Chile - Population 5000000")


if __name__ == "__main__":
    unittest.main()