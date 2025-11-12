# https://github.com/zachhae/lab11-ZH-AV
# Partner 1: Zach Haedicke
# Partner 2: Aniruth Venkedesh


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
    # ##########################

    ######## Partner 1
    # def test_multiply(self): # 3 assertions
    #     fill in code

    # def test_divide(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self):  # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 17)

    def test_logarithm(self):  # 3 assertions
        #     fill in code
        self.assertEqual(logarithm(10, 100), 2.0)
        self.assertEqual(logarithm(2, 2), 1.0)
        self.assertEqual(logarithm(2, 8, ), 3.0)
    # ##########################
    
    ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code

    # def test_sqrt(self): # 3 assertions    def test_divide_by_zero(self): # 1 assertion
    #     #     # call division function inside, example:
    #     #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     #     div(0, 5)
    #     #     fill in code
    #         with self.assertRaises(ZeroDivisionError):
    #             div(0,17)
    #
    #     def test_logarithm(self): # 3 assertions
    #     #     fill in code
    #         self.assertEqual(logarithm(10,100),2.0)
    #         self.assertEqual(logarithm(2,2), 1.0)
    #         self.assertEqual(logarithm(2,8,),3.0)
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()