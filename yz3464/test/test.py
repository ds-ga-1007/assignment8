'''
Created on Nov 28, 2016

@author: twff
'''
import unittest
from assignment8.investment import *

class Test(unittest.TestCase):
    def setUp(self):
        pass
    def test_class(self):
        i = investment(1,1)
        j = investment(100,1000)
    
    def test_eq(self):
        self.assertEqual(investment(1,1).num_trials, investment(1,1).num_trials)
        self.assertEqual(len(investment.simulateInvestment((investment(10,100)))),10)
    
    def test_constructor(self):
        invest = investment(10000,10)
        self.assertEqual(invest.positions,10)
        self.assertEqual(invest.num_trials,10000)
    
    def test_simualteInvestment(self):
        invest1 = investment(100,10)
        invest2 = investment(10,1000)
        self.assertEqual(len(investment.simulateInvestment(invest1)), 100)
        self.assertEqual(len(investment.simulateInvestment(invest2)), 10)
        self.assertTrue(all(investment.simulateInvestment(invest1))>=-1)
        self.assertTrue(all(investment.simulateInvestment(invest2))>=-1)
        self.assertTrue(all(investment.simulateInvestment(invest1))<=1)
        self.assertTrue(all(investment.simulateInvestment(invest2))<=1)
               
if __name__ == "__main__":
    unittest.main()