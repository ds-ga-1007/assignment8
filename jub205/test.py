"""
Created on Fri Nov 25 2016

@author: jinubak/jub205
@desc: This file contains unittest for investmentsimulator.py
"""

import unittest
from investmentsimulator import *

class MyTest(unittest.TestCase):
    
    def test_position_format(self):
        self.assertEqual(format_position_input('[1,10,100,1000]'),[1,10,100,1000])
        self.assertEqual(format_position_input('[100]'),[100])
        self.assertEqual(format_position_input('[20,30,40,50]'),[20,30,40,50])
        self.assertRaises(SystemExit,format_position_input,'[1,10,100,1000,a]')
        self.assertRaises(SystemExit,format_position_input,'[10a,20,30]')
        self.assertRaises(SystemExit,format_position_input,'[1 10 100 1000]')
        
    def test_num_trials_format(self):
        self.assertEqual(format_num_trials('1000'),1000)
        self.assertEqual(format_num_trials('100'),100)
        self.assertEqual(format_num_trials('10000'),10000)
        self.assertRaises(SystemExit,format_num_trials,'[1,10,100,1000,a]')
        self.assertRaises(SystemExit,format_num_trials,'1000a')
        self.assertRaises(SystemExit,format_num_trials,'hundred')
    
    def test_investmentportfoliio1(self):
        '''
        Testing 1000 shares worth $1 each, 10000 simulations
        '''
        portfolio = InvestmentPortfolio(1000,10000)        
        self.assertEqual(portfolio.position,1000)
        self.assertEqual(portfolio.position_value,1)
        self.assertEqual(portfolio.num_trials,10000)
        self.assertEqual(len(portfolio.cumu_ret),0)
        self.assertEqual(len(portfolio.daily_ret),0)
        
        portfolio.InvestmentSimulation()
        portfolio.compute_mean()
        portfolio.compute_std_dev()
        self.assertEqual(len(portfolio.cumu_ret),10000)
        self.assertEqual(len(portfolio.daily_ret),10000)
        self.assertNotEqual(portfolio.mean,0.0)
        self.assertNotEqual(portfolio.std_dev,0.0)
        
    def test_investmentportfoliio2(self):
        '''
        Testing 10 shares worth $100 each, 100 simulations
        '''
        portfolio = InvestmentPortfolio(10,100)        
        self.assertEqual(portfolio.position,10)
        self.assertEqual(portfolio.position_value,100)
        self.assertEqual(portfolio.num_trials,100)
        self.assertEqual(len(portfolio.cumu_ret),0)
        self.assertEqual(len(portfolio.daily_ret),0)
        
        portfolio.InvestmentSimulation()
        portfolio.compute_mean()
        portfolio.compute_std_dev()
        self.assertEqual(len(portfolio.cumu_ret),100)
        self.assertEqual(len(portfolio.daily_ret),100)
        self.assertNotEqual(portfolio.mean,0.0)
        self.assertNotEqual(portfolio.std_dev,0.0)   
        
if __name__ == '__main__':
    unittest.main()
