# Author: Leslie Huang (lh1036) 
# Description: Unit tests for methods in the InvestmentPositions class

import unittest
import numpy as np
from investment.positions import InvestmentPositions
from investment.exceptions import *

np.random.seed(123) # must set seed in order to unit test functions depending on rand num generation

class InvestmentPositionsTests(unittest.TestCase):
    '''
    Tests for InvestmentPositions methods
    Please note that the seed was set above to generate a fixed sequence of random numbers,
    which were used to generate constants that are used in the Asserts below.
    Although hard coding values in an Assert statement is not ideal, these values must be hard
    coded in order to unit test methods that use random number generation
    '''
            
    def test_simulate_one_share(self):
        '''
        Test that simulation of 1-day-return for 1 share returns 2 * value when
        randnum is fixed as > 0.49 (doubles your investment)
        '''
        position_1000 = InvestmentPositions(1, 1000)
        self.assertEqual(position_1000.simulate_one_share(), 2000)
        # the second value must be hard coded based on the seeded sequence of random nums
    
    def test_one_day_return(self):
        '''
        Test that one_day_return() generates the correct sum of returns from 1 day of holding
        '''
        position_1000 = InvestmentPositions(1, 1000)
        self.assertEqual(position_1000.one_day_return(), 0)
        # the second value must be hard coded based on the seeded sequence of random nums
    
    def test_n_days_return(self):
        '''
        Test that n_days_returns() generates the correct list of values
        '''
        position_1000 = InvestmentPositions(1, 1000)
        self.assertEqual(position_1000.n_days_return(10), [2000, 0, 0, 2000, 2000, 0, 2000, 2000, 0, 0])
        # the second value must be hard coded based on the seeded sequence of random nums
        

class parsePositionsTests(unittest.TestCase):  
    '''
    Tests for the parse_positions @classmethod
    '''      
    
    def test_parse_invalid_positions(self):
        '''
        Invalid position value (5) raises InvalidPositionError
        '''
        with self.assertRaises(InvalidPositionError):
            InvestmentPositions.parse_positions("[1, 5, 100, 1000]")
    
    def test_parse_valid_positions(self):
        '''
        Test that parse_positions on a list_as_string returns a list of InvestmentPosition objects.
        '''
        self.assertEqual(InvestmentPositions.parse_positions("[1, 10, 100, 1000]"),
            [InvestmentPositions(position, int(1000 / position)) for position in [1, 10, 100, 1000]]
            )
        
    def test_parse_positions_valid_repeated_vals(self):
        '''
        Test that parse_positions accepts repeated valid positions and returns list of InvestmentPosition objects.
        '''
        self.assertEqual(InvestmentPositions.parse_positions("[1, 10, 10, 100, 1000, 1]"),
            [InvestmentPositions(position, int(1000 / position)) for position in [1, 10, 10, 100, 1000, 1]]
            )
    
    def test_parse_positions_invalid_format(self):
        '''
        Test parse_positions raises InvalidListError if list_as_string is not in "list" format.
        '''
        with self.assertRaises(InvalidListError):
            InvestmentPositions.parse_positions("1, 10, 100, 1000")
            
if __name__ == '__main__':
    unittest.main()
    
