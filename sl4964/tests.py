'''
Created on Nov 27, 2016

@author: ShashaLin
'''
import unittest
from Functions import cumu_return, repeat, makefig, save_results
import numpy as np
import matplotlib.pyplot as plt

class Test(unittest.TestCase):


    def testReturn(self):
        self.assertTrue(cumu_return (100, 10) <= 200*10 and cumu_return (100, 10) >= 0)
        self.assertTrue(cumu_return (10, 100) <= 20*100 and cumu_return (10, 100) >= 0)
    
    def testRepeat(self):
        self.assertTrue(-1 <= repeat(10, 100, 10).all() <= 1)
        self.assertTrue(-1 <= repeat(100, 1, 1000).all() <= 1)
    
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
        unittest.main()