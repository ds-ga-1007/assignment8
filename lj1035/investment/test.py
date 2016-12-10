import unittest
from . import instrument, myexception
import numpy as np


# This class contains unittests for methods in the Instrument class and unittests for other functions.
class Test(unittest.TestCase):

    def test_init(self):
        """
        Unit test for the constructor of the Instrument class.
        """
        invest = instrument.Instrument(10, 1000)
        self.assertEqual(invest.position, 10)
        self.assertEqual(invest.position_value, 100)
        self.assertEqual(invest.num_trials, 1000)

    def test_simulate_invest(self):
        """
        Unit test for the simulate_invest method in the Instrument class.
        """
        np.random.seed(1)
        invest = instrument.Instrument(10, 1)
        self.assertTrue(np.isclose(invest.simulate_invest()[0], 0.6))

    def test_num_trials_to_int(self):
        """
        Unit test for the num_trials_to_int function.
        """
        with self.assertRaises(myexception.NotNumericError):
            instrument.num_trials_to_int('=')
        with self.assertRaises(myexception.NotIntegerError):
            instrument.num_trials_to_int('3.5')
        with self.assertRaises(myexception.NotPositiveIntegerError):
            instrument.num_trials_to_int('-3')

    def test_positions_to_list(self):
        """
        Unit test for the positions_to_list function.
        """
        with self.assertRaises(myexception.FormattingError):
            instrument.positions_to_list('1, 10, 100, 1000')
        with self.assertRaises(myexception.FormattingError):
            instrument.positions_to_list('1 10 100 1000')
        with self.assertRaises(myexception.NotNumericError):
            instrument.positions_to_list('[foo]')
        with self.assertRaises(myexception.NotIntegerError):
            instrument.positions_to_list('[1.5, 2.5]')
        with self.assertRaises(myexception.NotPositiveIntegerError):
            instrument.positions_to_list('[-3, -2, 7]')

if __name__ == '__main__':
    unittest.main()
