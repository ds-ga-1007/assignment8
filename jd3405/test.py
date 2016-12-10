# Solution for DS-GA 1007 Assignment#8
# Author: Jiaming Dong (jd3405@nyu.edu)
# NYU Center for Data Science

import unittest
from assignment8 import *


class SimpleTest(unittest.TestCase):

    def testInvest(self):
        """test one investment"""
        investment = Investment(100)
        self.assertGreaterEqual(investment.ret, 0)
        self.assertLessEqual(investment.ret, 1000)

if __name__ == "__main__":
    unittest.main()
