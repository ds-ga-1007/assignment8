'''

@author: jonathanatoy
'''
import unittest
import investment
import numpy as np

class Test(unittest.TestCase):


    def investmentTest(self):
        '''
        Tests whether investment positions and position_value are correctly associated
        '''
        
        position = 10
        my_investment = investment.investment(position)
        self.assertEqual(my_investment.position_value, 100.)
        
    def gambleTest(self):
        '''
        Tests whether gamble function outputs are within reasonable bounds.
        '''
        positions = [1, 10, 100, 1000]
        my_investment = investment.investment(positions)
        le2000 = np.all(my_investment.gamble() <= 2000)
        ge0 = np.all(my_investment.gamble() >= 0)
        self.assertEqual(True, np.all([ge0, le2000]))

if __name__ == "__main__":
    unittest.main()