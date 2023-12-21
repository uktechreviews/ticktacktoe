import unittest
import calculator as Calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        result = Calc.MyCalculator(4, 7)
        self.assertEqual(result, 11)

    def test_negatives(self):
        result = Calc.MyCalculator(-5,8)
        self.assertEqual(result, 3)

    def test_with_letters(self):
        result = Calc.MyCalculator("f", "g")
        self.assertEqual(result, 0)

if __name__== "__main__":
    unittest.main()