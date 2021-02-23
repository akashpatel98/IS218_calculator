import unittest
from Calculator import Calculator


class MyTestCase(unittest.TestCase):

    def test_instantiate_calculator(self):
        calculator = Calculator()
        self.assertIsInstance(calculator, Calculator)

    def test_results_property_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.result, 6)

    def test_add_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.add(3, 3), 6)


if __name__ == '__main':
    unittest.main()
