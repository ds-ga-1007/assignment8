'''
This test module tests:
    - investment class with its methods
    - input_positions_set function
    - input_num_trials function
    - exceptions and errors

Author: Xianzhi Cao (xc965)
'''

import unittest
from investment import *
from formatchecking import *
from output import *


class UserTest(unittest.TestCase):
    """
    This class allows users to run tests with classes and functions.
    """

    def setUp(self):
        pass

    def test_investment(self):
        '''test the method of investment class'''
        self.assertEqual(100, len(investment(10, 100).daily_returns()))

    def test_get_positions_set(self):
        '''test the get_position_set function'''
        self.assertEqual(['1', '10', '100'],
                         get_positions_set('[1, 10 , 100]'))
        self.assertEqual(['10', '100', '1000'],
                         get_positions_set('[ 10, 1 0 0, 1000   ]'))

        # test when positions_set input is emtpy or space
        with self.assertRaises(EmptyInputError):
            get_positions_set('')
        with self.assertRaises(EmptyInputError):
            get_positions_set(' ')

        # test when position is zero
        with self.assertRaises(ZeroPositionError):
            get_positions_set('[0, 1, 10, 100]')

        # test disobeyed formatting input positions_set
        with self.assertRaises(InputFormatError):
            get_positions_set('foo')
        with self.assertRaises(InputFormatError):
            get_positions_set('(1, 10, 100)')
        with self.assertRaises(InputFormatError):
            get_positions_set('[1, 10, foo]')
        with self.assertRaises(InputFormatError):
            get_positions_set('[-1, -10]')
        with self.assertRaises(InputFormatError):
            get_positions_set(',')


    def test_get_num_trials(self):
        '''test the get_num_trials function'''

        # test non numeric input number of trials
        with self.assertRaises(NonNumericError):
            get_num_trials('=')
        with self.assertRaises(NonNumericError):
            get_num_trials('foo')
        with self.assertRaises(NonNumericError):
            get_num_trials([1, 10])

        # test when the numeric input is not a positive integer
        with self.assertRaises(NonPositiveIntegerError):
            get_num_trials(0)
        with self.assertRaises(NonPositiveIntegerError):
            get_num_trials(-100)


if __name__ == '__main__':
    unittest.main()
