import unittest
from UserDefinedError import *
from assignment8 import *
from investment import *
from functions import *
"""
Unittest for investment_input_pos and investment_input_trials
@author: Qianyu Cheng
"""


class MyTestCase(unittest.TestCase):
    def test_investment_input_pos(self):

        self.assertEqual(['1', '10', '100'], investment_input_pos('[1,10,100]'))
        self.assertEqual(['1', '10', '100','1000'], investment_input_pos('[1,10,100,1000]'))

        with self.assertRaises(InputErrorPositions):
            investment_input_pos('foo')
        with self.assertRaises(InputErrorPositions):
            investment_input_pos('[1,222,3333]')

    def test_investment_input_trials(self):

        self.assertEqual(1000, investment_input_trials('1000'))
        self.assertEqual(10000, investment_input_trials('10000'))

        with self.assertRaises(InputErrorTrials):
            investment_input_trials('-1000')

if __name__ == '__main__':
    unittest.main()
