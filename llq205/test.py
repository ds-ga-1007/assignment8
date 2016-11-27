
# coding: utf-8

# In[ ]:

import unittest
from investment import *

# $ python -m unittest -v test.py

class Tests(unittest.TestCase):
    def testInvestment(self):
        """Tests for class Investment"""
        self.assertEqual(investment(100, 10).positions, 100)
        self.assertEqual(investment(100, 10).num_trials, 10)
        self.assertEqual(investment(100, 10).position_value, 10)
            
    def testSimulate(self):
        """Tests for function Simulate"""
        self.assertTrue(len(investment.simulate(investment(100, 10))) == 10)
        self.assertTrue(all(investment.simulate(investment(100, 10))) <= 1)
        self.assertTrue(all(investment.simulate(investment(100, 10))) >= -1)

if __name__ == "__main__":
    unittest.main()

