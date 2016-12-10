'''
Unittest

Created on Nov 27, 2016
@author:Zhiqi Guo
@email: zg475@nyu.edu
'''
import unittest
import numpy as np
from investment import investment

class Test(unittest.TestCase):
    def setup(self):
        pass

    def test_init(self):
        self.assertEqual(investment(1,10000).num_positions, 1)
        self.assertEqual(investment(1,10000).num_trials, 10000)
        self.assertEqual(investment(1,10000).position_value, 1000/1)
    
    def test_get_cumu_ret(self):
        self.assertEqual(type(investment(10,10000).get_cumu_ret()), np.float64)
        self.assertTrue(investment(10,10000).get_cumu_ret() >= 0)
    
    def test_get_daily_ret(self):
        self.assertEqual(len(investment(100,1000).get_daily_ret()),investment(100,1000).num_trials)
        self.assertTrue( all((i<= 1 for i in investment(100,1000).get_daily_ret())))
        self.assertTrue( all((i>=-1 for i in investment(100,1000).get_daily_ret())))
    
    
if __name__ == "__main__":
    unittest.main()