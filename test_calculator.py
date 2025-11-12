# https://github.com/zachhae/lab11-ZH-AV
# Partner 1: Zach Haedike
# Partner 2: Aniruth Venkedes

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self):  # 3 assertions
        self.assertEqual(add(5, 2), 7)
        self.assertEqual(add(-5, -10), -15)
        self.assertEqual(add(-5, 10), 5)

    def test_subtract(self):  # 3 assertions
        self.assertEqual(subtract(10, 1), 9)
        self.assertEqual(subtract(-2, -3), 1)
        self.assertEqual(subtract(1, 10), -9)

    ######## Partner 1
    def test_multiply(self):  # 3 assertions
        self.assertEqual(mul(15, 3), 45)
        self.assertEqual(mul(2, 4), 8)
        self.assertEqual(mul(12, 12), 144)

    def test_divide(self):  # 3 assertions
        self.assertAlmostEqual(div(2.0, 5.0), 2.5)
        self.assertAlmostEqual(div(5, 45), 9)
        self.assertAlmostEqual(div(12, 144), 12)

    ######## Partner 2
    def test_divide_by_zero(self):  # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 17)

    def test_logarithm(self):  # 3 assertions
        self.assertEqual(logarithm(10, 100), 2.0)
        self.assertEqual(logarithm(2, 2), 1.0)
        self.assertEqual(logarithm(2, 8, ), 3.0)

    ######## Partner 1
    def test_log_invalid_argument(self):  # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self):  # 3 assertions
        self.assertEqual(hypotenuse(4, 3), 5)
        self.assertEqual(hypotenuse(12, 5), 13)
        self.assertEqual(hypotenuse(-6, 8), 10)

    def test_sqrt(self):  # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-5)

        self.assertEqual(square_root(144), 12)
        self.assertEqual(square_root(1), 1)

# Do not touch this
if __name__ == "__main__":
    unittest.main()