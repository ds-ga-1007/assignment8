from tools.investment import *
import unittest

class investmentTest(unittest.TestCase):
    """
    Test functions in class investment.
    Assume that the type of all inputs are correct; otherwise, 
    functions in exceptions will find the invalid input.
    """
    def test_position(self): 
        self.assertEqual(investment(10,100).position,10)
        self.assertEqual(investment(100,100).position,100)
        
    def test_num_trials(self):
        self.assertEqual(investment(10,10).num_trials,10)
        self.assertEqual(investment(10,100).num_trials,100)
    
    def test_position_value(self):
        self.assertEqual(investment(10,100).position_value(),100)
        self.assertEqual(investment(100,100).position_value(),10)
        
    def test_cumu_ret(self):
        self.assertTrue(investment(10,10).cumu_ret() >= 0)
        self.assertTrue(investment(10,100).cumu_ret() >= 0)
        
    def test_daily_ret(self):
        self.assertTrue(investment(10,100).daily_ret() <= 1)
        self.assertTrue(investment(10,100).daily_ret() >= -1)
        
    def test_simulation(self):
        self.assertEqual(len(investment(10,100).simulation()), 100)
        self.assertEqual(len(investment(10,1000).simulation()), 1000)
        
        
if __name__ == "__main__":
    unittest.main()