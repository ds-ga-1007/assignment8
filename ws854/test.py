import unittest

from collections import Counter

from investment import *

"""
The only thing needs to be tested is the random process to make sure the result is genereated
randomly as 51% and 49% percent. The test below was developed to run for buying 1 share parallel a time
and make sure the chances are roughly 51% to win.
"""
class MyTest(unittest.TestCase):
    def test_investment(self):
        inv = list(investment([1], 100000).result()[1].values())
        c = Counter(inv)
        # how many times to get the 2000 (which is 1 as daily_ret)
        pos = c[1]
        # how many times to get the 0 (which is -1 as daily_ret)
        neg = c[-1]
        self.assertAlmostEqual(round(pos/(neg+pos),3), 0.51,places=2)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()