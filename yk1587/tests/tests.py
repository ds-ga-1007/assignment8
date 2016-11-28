import unittest
from program.simulations import *
from program.exceptions import *

class SimpleTest(unittest.TestCase):
    
    def test_positions(self):
        """unit test for position input"""
        self.assertEqual(trialInput([1,10,100,1000],10000).positionList, [1,10,100,1000])
        self.assertEqual(trialInput([1,10],10000).positionList, [1,10])
        with self.assertRaises(InvalidListError):
            trialInput(1,10000)
        with self.assertRaises(PositionError):
            trialInput([1,3,5],10000)
    
    def test_numTrials(self):
        """unit test for num_trials"""
        self.assertEquals(trialInput([1,10,100,1000],10000).num_trials, 10000)
        self.assertEquals(trialInput([1,10,100,1000],100).num_trials, 100)
        with self.assertRaises(IntegerError):
            trialInput([1,10,100,1000],5.7)
        


if __name__ == '__main__':
    unittest.main()