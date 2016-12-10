from investment import *
import unittest

class tests(unittest.TestCase):
    def test_investment(self):
        """
        Tests to make sure that the class investment yields correct output for given input 
        """
        
        self.assertEqual(investment([1,10,100], 100).positions, [1,10,100])
        self.assertEqual(investment([1,10,100],100).num_trials, 100)
        
        self.assertEqual(investment([1,100],1000).positions, [1,100])
        self.assertEqual(investment([1,100],1000).num_trials,1000)

        
