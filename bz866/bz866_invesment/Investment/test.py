'''
Created on 2016年12月4日

@author: bz866
'''
import unittest
from Investment.investment import *

class tests(unittest.TestCase):

    
    '''test the initialization of investment stimulation'''
    def test_constructor(self):

        self.assertEqual(trialInput([1, 10, 100], 1000).positions, [1, 10, 100])
        self.assertEqual(trialInput([1, 10, 100], 1000).num_trials, 1000)
    
    def test_stimulate(self):

        '''test stimulate method'''
        a = trialInput([1, 10, 100], 1000)
        result = a.stimulate([1000.0, 100.0, 10.0], 1000) 

        self.assertEqual(len(result[1]), 1000)
        self.assertEqual(len(result[10]), 1000)
        self.assertEqual(len(result[100]), 1000)

        self.assertTrue(result[1].all() <= 1)
        self.assertTrue(result[1].all() >= -1)

        self.assertTrue(result[10].all() <= 1)
        self.assertTrue(result[10].all() >= -1)

        self.assertTrue(result[100].all() <= 1)
        self.assertTrue(result[100].all() >= -1)

if __name__ == "__main__":
    unittest.main() 
