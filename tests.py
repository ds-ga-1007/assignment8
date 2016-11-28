'''
Created on Nov 27, 2016

@author: danielamaranto
'''
import unittest
import numpy as np
from position_outcomes import *

'''Given that all my functions rely on randomly generated data, my tests either
confirm whether or not the functions work based on probabilities with large numbers
of trials or they confirm that functions output the correct format of data.
I found the assertAlmostEqual method from the python documentation website.
https://docs.python.org/2/library/unittest.html
'''

class Test(unittest.TestCase):
    
    def testShareResult(self):
        result = [share_result() for i in list(range(10000))]
        proportion_true = sum(result)/10000
        self.assertAlmostEqual(proportion_true, 0.51, 2)

    def testCumulative(self):
        result = np.array([cumu_ret(1) for i in list(range(100000))])
        outcome = result.mean()
        self.assertAlmostEqual(outcome, 1020, -2)      #Expected value of 1 share is .51 * 2000, or 1020
        

if __name__ == "__main__":
    unittest.main()