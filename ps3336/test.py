'''
Created on Nov 23, 2016
@author: peimengsui
@desc: test the investment class
'''
import unittest
from investment import investment

class Test(unittest.TestCase):
    def test_constructor(self):
        self.assertEqual(investment(10,10).num_positions,10)
        self.assertEqual(investment(10,10).num_trials,10)
        self.assertEqual(investment(10,10).position_value,100)

    def test_simulate(self):
        self.assertEqual(len(investment.simulate(investment(10,10))),10)
        self.assertTrue(all(investment.simulate(investment(10,10))>=-1))
        self.assertTrue(all(investment.simulate(investment(10,10))<=1))
        
if __name__ == "__main__":
    unittest.main()