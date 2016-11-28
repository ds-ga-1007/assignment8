'''
Created on 2016年11月28日

@author: chenfanglin
'''
import unittest
from daily_ret import *


class Test(unittest.TestCase):
    '''
    The Test class provides unit tests for the functions daily_ret_trial(), daily_ret(), and result().
    '''
    
    def test_daily_ret_trial(self):
        self.assertIn(daily_ret_trial(1), [-1.0, 1.0])
        self.assertTrue(-1.0 <= daily_ret_trial(10) <= 1.0)
        self.assertTrue(-1.0 <= daily_ret_trial(100) <= 1.0)
        self.assertTrue(-1.0 <= daily_ret_trial(1000) <= 1.0)
        
    def test_daily_ret(self):
        self.assertTrue(all([-1.0 <= ret <= 1.0 for ret in daily_ret(1, 10000)]))
        self.assertTrue(all([-1.0 <= ret <= 1.0 for ret in daily_ret(1000, 20)]))
        
    def test_result(self):
        self.assertEqual(result(10, 10000)[0], 10)
        self.assertTrue(-1 <= result(10, 10000)[1] <= 1)
        self.assertTrue(0 <= result(10, 10000)[2] <= 1)
        
        self.assertEqual(result(100, 55)[0], 100)
        self.assertTrue(-1 <= result(100, 55)[1] <= 1)
        self.assertTrue(0 <= result(100, 55)[2] <= 1)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()