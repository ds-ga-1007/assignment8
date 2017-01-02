import unittest
from assignment8 import *


class UnitTest_test(unittest.TestCase):
    N = 1000
    position = np.array([1, 10, 100, 1000], dtype=np.int)
    num_trials = 10000
    # AssertTrue
    def test_functions(self):
        self.assertTrue(cumu_ret(position, N, num_trials), "AssertTrue with cumu_ret funtion.")
        self.assertTrue(daily_ret(a), "AssertTrue with daily_ret funtion.")
        self.assertTrue(make_hist_list(position, b, num_trials), "AssertTrue with make_hist_list funtion.")

    # test the input array is the number we interested
    def test_input(self):
        self.assertIs(position, [1, 10, 100, 1000])


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)