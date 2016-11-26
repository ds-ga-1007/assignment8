import unittest
from positions import *

# I am not unit testing methods that are based on random number calculations because
# it is only possible to trivially test what they return

class parsePositionsTests(unittest.TestCase):  
    '''
    Tests for the parse_positions @classmethod
    '''      
    
    def test_parse_invalid_positions(self):
        '''
        Invalid position value (5) raises ValueError.
        '''
        with self.assertRaises(ValueError):
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
        Test parse_positions raises error if list_as_string is not in "list" format.
        '''
        with self.assertRaises(ValueError):
            InvestmentPositions.parse_positions("1, 10, 100, 1000")
            


if __name__ == '__main__':
    unittest.main()
    
