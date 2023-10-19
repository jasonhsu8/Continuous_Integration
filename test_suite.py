import unittest
from subtract_numbers_function import subtract_numbers

class testFunction(unittest.TestCase):

    def test_subtraction(self):
        result = subtract_numbers(5, 4)
        self.assertEqual(result, 1)
    
    def test_subtraction_negative_numbers(self):
        result = subtract_numbers(6, -2)
        self.assertEqual(result, 8)

    def test_subtraction_float_numbers(self):
        result = subtract_numbers(7.5, 2.5)
        self.assertAlmostEquals(result, 5.0, places=2 )

if __name__ == '__main__':
    unittest.main()
