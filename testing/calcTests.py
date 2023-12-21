import unittest
import calculator as Calc

class TestCalc(unittest.TestCase):

    def test_invalid_operation(self):
        self.assertRaises(ValueError, Calc.MyCalculator, 1, 1, 'a')
        self.assertRaises(ValueError, Calc.MyCalculator, 1, 1, '1')
        self.assertRaises(ValueError, Calc.MyCalculator, 1, 1, 2)
        self.assertRaises(ValueError, Calc.MyCalculator, 1, 1, [])

    def test_add(self):
        self.assertEqual(Calc.MyCalculator(4, 7, '+'), 11)
        self.assertEqual(Calc.MyCalculator(5, -3, '+'), 2)
        self.assertEqual(Calc.MyCalculator(-4, 2, '+'), -2)
        self.assertEqual(Calc.MyCalculator(-4, -6, '+'), -10)

    def test_subtract(self):
        self.assertEqual(Calc.MyCalculator(8,5, '-'), 3)
        self.assertEqual(Calc.MyCalculator(8,-5, '-'), 13)
        self.assertEqual(Calc.MyCalculator(-8,5, '-'), -13)
        self.assertEqual(Calc.MyCalculator(-8,-5, '-'), -3)

    # TODO: Add Tests for Multiplication and Division (incl divide by 0)

    def test_invalid_numbers(self):
        self.assertRaises(TypeError, Calc.MyCalculator, "g", 1, '+')
        self.assertRaises(TypeError, Calc.MyCalculator, "g", "y", '+')
        self.assertRaises(TypeError, Calc.MyCalculator, "g", "hello", '+')
        self.assertRaises(TypeError, Calc.MyCalculator, "7", 1, '+')
        self.assertRaises(TypeError, Calc.MyCalculator, 5, [], '+')

if __name__== "__main__":
    unittest.main()