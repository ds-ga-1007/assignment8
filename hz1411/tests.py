import unittest
from trial import *

class SimpleTest(unittest.TestCase):
	def setUp(self):
		self.test_trial = trial

	def test_init(self):
		for pos in [1,10,100,1000]:
			for num_t in [1,100,10000]:
				self.assertEqual(self.test_trial(pos,num_t).position, pos)
				self.assertEqual(self.test_trial(pos,num_t).num_trials, num_t)
				self.assertEqual(self.test_trial(pos,num_t).position_value, int(1000/pos))

	def test_simulation(self):
		for pos in [1,10,100,1000]:
			for num_t in [1,100,10000]:
				ret = self.test_trial(pos,num_t).simulation()
				self.assertTrue(all(x<=1 for x in ret))
				self.assertTrue(all(x>=-1 for x in ret))
				self.assertEqual(len(ret), num_t)

if __name__=="__main__":
	unittest.main()

