'''
Created on Nov 28, 2016

@author: sunyifu
'''
import unittest
from investment import *

class Test(unittest.TestCase):


    def test_constructor(self):
        self.assertEqual(investment(10,10000).position, 10)
        self.assertEqual(investment(10,1000).num_trials, 1000)
        self.assertEqual(investment(10,10000).position_value, 100)
    
    
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()