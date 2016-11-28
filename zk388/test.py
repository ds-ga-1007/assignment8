'''
Created on Nov 28, 2016

@author: Zahra Kadkhodaie
'''

'''All the tests pass successfully. Run time is almost 0.3 s on average.'''

import unittest
from investment import *
from total_gain import *

class Test(unittest.TestCase):

    '''Test the investment class'''
    def testInvestment1(self):
        #Test whether invalid input are filter in the investment class
        self.assertRaises(Not_a_Valid_Position, investment, 99) 
        self.assertRaises(Not_a_Valid_Position, investment, -10) 
        self.assertRaises(Not_a_Valid_Position, investment, 'blah') 
        self.assertRaises(Not_a_Valid_Position, investment, [10,100]) 


    def testInvestment2(self):
        #Test the position attribute 
        self.assertEqual(investment(10).position, 10 )
        self.assertEqual(investment(1000).position, 1000 )

    def testInvestment3(self):
        #Test the position_value attribute 
        self.assertEqual(investment(1000).position_value, 1)
        self.assertEqual(investment(10).position_value, 100)

       
        
    def testInvestment4(self):
        #Test the daily_outcome method. Because the outcome of this method is random, we cannot test it directly. So I just test its properties
        self.assertTrue(investment(10).daily_outcome().shape == (10, 1))
        self.assertTrue(investment(100).daily_outcome().shape == (100, 1))
        
    def testInvestment5(self): 
        #Test the daily_outcome method. Because the outcome of this method is random, we cannot test it directly. So I just test its properties
        self.assertTrue(investment(10).daily_outcome()[5] in [200,0])
        self.assertTrue(investment(1).daily_outcome()[0] in [2000,0])

    def testInvestment6(self):
        #Test the daily_gain method. Because the outcome of this method is random, we cannot test it directly. So I just test its properties
        self.assertTrue(investment(10).daily_gain() <= 1 and investment(10).daily_gain() >= -1 )   
        self.assertTrue(investment(1000).daily_gain() <= 1 and investment(10).daily_gain() >= -1 )   
      
      
    '''Test the total_gain function''' 
    def testTotal_gain1(self):
        #Again because this function's output is random, instead of testing the output directly, we test some properties of the output.
        self.assertTrue(total_gain(100,3).shape == (3,1))  
        self.assertTrue(total_gain(10,31).shape == (31,1))  
        self.assertTrue(total_gain(1,10000).shape == (10000,1))  

    def testTotal_gain2(self):
        self.assertTrue(total_gain(100,3)[0] <= 1 and total_gain(100,3)[0] >= -1)  
        self.assertTrue(total_gain(10,10)[9] <= 1 and total_gain(10,10)[9] >= -1)  
        self.assertTrue(total_gain(1, 10)[5] <= 1 and total_gain(1, 10)[5] >= -1)   
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()