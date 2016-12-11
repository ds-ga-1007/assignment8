'''
Created on Nov 28, 2016

@author: Jingyi Su
This module performs the unit test for Investment module
'''
import unittest
from Investment import Investment

class Test(unittest.TestCase):


    def test_init(self):
        '''
        test the initialization of investment class, ie. the assignment of position and num_trials
        '''
        self.assertEqual(Investment.investment([1,10,100,1000],100).positions,[1,10,100,1000])
        self.assertEqual(Investment.investment([1,10,100,1000],100).num_trials,100)
    
    def test_investment_return(self):
        '''
        test the investment return (daily) calculation function
        '''
        investment=Investment.investment(10,1000)
        daily_return=investment.investment_return(10)
        self.assertEqual(len(daily_return),1000)
        self.assertGreaterEqual(daily_return.all(), -1)
        self.assertLessEqual(daily_return.all(), 1)


if __name__ == "__main__":
    unittest.main()