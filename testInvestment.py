import unittest
from Investment import InvSimulation
import numpy as np

class TestInvestment(unittest.TestCase):
	 
	def test_singleReturn(self):
		testObj_1 = InvSimulation(250, 1000)
		one_day_test = testObj_1.singleReturn()
		self.assertTrue(one_day_test<=2000 and one_day_test>= 0)
	 
	def test_cumuReturn(self):
		testObj_2 = InvSimulation(200, 500)
		cumu_test = testObj_2.cumuReturn()
		self.assertTrue(np.mean(cumu_test)<=2000 and np.mean(cumu_test)>= 0)
		self.assertEqual(len(cumu_test), 500)

	def test_dailyReturn(self):
		testObj_3 = InvSimulation(50, 2000)
		daily_test = testObj_3.dailyReturn()
		self.assertTrue(np.mean(daily_test)<=2 and np.mean(daily_test)>= 0)
		self.assertEqual(len(daily_test), 2000)




if __name__ == '__main__':
    unittest.main(exit=False)