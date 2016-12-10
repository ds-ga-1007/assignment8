"""
Date: Nov 28, 2016
Author: Chloe Meng(lm3226)
Description: This program provides the unit test for daily_investment_return.
"""
import unittest
from daily_investment_return import *

class test_daily_investement_return(unittest.TestCase):
    def test_daily_investement_return_class(self):
        with self.assertRaises(InvalidUserInputException):
            daily_investment_return([1101001000],10)
        with self.assertRaises(InvalidUserInputException):
            daily_investment_return([1, 10, 100, 1000],-10)

if __name__ == "__main__":
    unittest.main()
