
# coding: utf-8

# In[ ]:
#This is a simple test whihc can check the user_input and simulation.
import unittest
from investment import *

class SimpleTest(unittest.TestCase):

    #Test for the class investment and check the positions and num_trials.
    def testinvestment(self):
        self.assertEqual(investment([1,10,100,1000],1000).positions, [1,10,100,1000])
        self.assertEqual(investment([1,10,100,1000],1000).num_trials, 1000)
        
     #Test for the function simulate.   
    def testsimulate(self):
    
        self.assertTrue(len(investment.simulate(investment([1,10,100,1000],1000))[0]) == 1000)
        self.assertTrue(len(investment.simulate(investment([1,10,100,1000],1000))[1]) == 1000)
        self.assertTrue(len(investment.simulate(investment([1,10,100,1000],1000))[2]) == 1000)
        self.assertTrue(len(investment.simulate(investment([1,10,100,1000],1000))[3]) == 1000)
        
        self.assertTrue(all(investment.simulate(investment([1,10,100,1000],1000))[0]) <= 1)
        self.assertTrue(all(investment.simulate(investment([1,10,100,1000],1000))[1]) <= 1)
        self.assertTrue(all(investment.simulate(investment([1,10,100,1000],1000))[2]) <= 1)
        self.assertTrue(all(investment.simulate(investment([1,10,100,1000],1000))[3]) <= 1)
        
        self.assertTrue(all(investment.simulate(investment([1,10,100,1000],1000))[0]) >= -1)
        self.assertTrue(all(investment.simulate(investment([1,10,100,1000],1000))[1]) >= -1)
        self.assertTrue(all(investment.simulate(investment([1,10,100,1000],1000))[2]) >= -1)
        self.assertTrue(all(investment.simulate(investment([1,10,100,1000],1000))[3]) >= -1)
        
if __name__ =="__main__":
    unittest.main()     

