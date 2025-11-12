import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(15,3),45)
        self.assertEqual(mul(2, 4), 8)
        self.assertEqual(mul(12, 2), 144)

    def test_divide(self): # 3 assertions
        self.assertAlmostEqual(div(5.0,2.0), 2.5)
        self.assertAlmostEqual(div(45, 5), 9)
        self.assertAlmostEqual(div(144, 12), 12)

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0,5)
            logarithm(-2, 100)
            logarithm(-4,0)
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(4,3), 5)
        self.assertEqual(hypotenuse(12, 5), 13)
        self.assertEqual(hypotenuse(-6, 8), 10)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-5)
            square_root(-10)

        self.assertEqual(square_root(144), 12)
        self.assertEqual(square_root(1), 1)
        self.assertEqual(square_root(36), 6)

    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()