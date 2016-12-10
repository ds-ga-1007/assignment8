'''
    This module is the unit test for investment.py program.
'''

import unittest
import numpy as np
from investment import Investment

class TestInvestment(unittest.TestCase):

    def calcPositionValue(self):
        inv = Investment('[1, 10, 100, 1000]', 100, 17)
        inv.setSeed()
        inv.calcPositionValue()
        self.assertEqual(inv.position_value, np.array([1000, 100, 10, 1]))

    def calcCumulativeReturn(self):
        inv = Investment('[1, 10, 100, 1000]', 100, 17)
        inv.setSeed()
        inv.calcPositionValue()
        inv.calcCumulativeReturn()
        inv.calcDailyReturn()
        inv.calcDailyReturnMean()
        self.assertEqual(np.round(inv.daily_mean, 4), np.array([0.1, 0.024, 0.0212, 0.0177]))


    def calcCumulativeReturn(self):
        inv = Investment('[1, 10, 100, 1000]', 100, 17)
        inv.setSeed()
        inv.calcPositionValue()
        inv.calcCumulativeReturn()
        inv.calcDailyReturn()
        inv.calcDailyReturnMean()
        inv.calcDailyReturnStd()
        self.assertEqual(inv.daily_std, np.array([0.995 , 0.3829, 0.1005, 0.0346]))

if __name__ == '__main__':
    unittest.main()
