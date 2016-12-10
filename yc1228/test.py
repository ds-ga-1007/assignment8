import unittest
from investment import investment

'''Unittest that tests the functions from class investment'''
class Test(unittest.TestCase):
    def test_init(self):
        self.assertEqual(investment(10,10000).position, 10)
        self.assertEqual(investment(10,10000).num_trials, 10000)
        self.assertEqual(investment(10,10000).position_value, 100)
    def test_simulation(self):
        invest = investment(10,10000)
        daily_ret = invest.simulation()
        self.assertEqual(len(daily_ret), 10000)
        self.assertTrue(daily_ret.all() <= 1)
        self.assertTrue(daily_ret.all() >= -1)

if __name__ == "__main__":
    unittest.main()