'''
Created on Nov 28, 2016

@author: sj238
'''
import unittest
from investment_simulation import *

class Test(unittest.TestCase):
    """
    This is the unit-test class that runs tests with expected outcomes
    Run the test in the project's root directory
    with the following command:
        $ python -m unittest discover
    """
    def test_Investment(self):
        '''
        This is the unit tests for the investment constructor that pass input to arguments positoins and num_trials
        '''
        self.assertEqual(Investment([1, 10, 100, 1000], 10000).positions, [1, 10, 100, 1000])
        self.assertEqual(Investment([1, 10, 100, 1000], 10000).num_trials, 10000)
    
    def test_simulation(self):
        """
        This is the unit tests for testing simulation method.
        
        """
        positions = [1, 10, 100,1000]
        num_trials = 10000
        result = Investment(positions, num_trials)
        result = result.simulation(positions, num_trials) 
        for pos in positions:
            self.assertEqual(len(result[pos]), num_trials)
            self.assertTrue(result[pos].all() == 1 or result[pos].all() == -1)
            
            
if __name__ == "__main__":
    unittest.main()