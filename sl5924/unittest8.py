
'''
This is the test module of the program
Created on 2016/11/22
Version: 1.0
@author: liusheng
ShengLiu Copyright 2016-2017
'''
from investiment_simulation import *
import sys
import unittest

class  utest(unittest.TestCase):
	def setUp(self):
		#print ('Setting up ....')
		pass

	def test_invest_simulation(self):
		self.assertEqual(invest_simulation([1, 10, 50, 1000],10000).positions,[1, 10, 50, 1000])
		self.assertEqual(invest_simulation([1, 10, 50, 1000],10000).num_trials,10000)

	def test_calc_mean(self):
		test = invest_simulation([1,2],10000)
		self.assertEqual(test.calc_mean_return([1,3,5]),3)

	def test_calc_std(self):
		test = invest_simulation([1,2],10000)
		self.assertEqual(test.calc_std_return([1]),0)

	def test_investment_outcome(self):
		test = invest_simulation(1000,1)
		self.assertIn(test.investment_outcome(1),[0,2000])
		self.assertIn(test.investment_outcome(10),[0,200,400,600,800,1000,1200,1400,1600,1800,2000])
		self.assertIn(test.investment_outcome(100),range(0,2020,20))
		self.assertIn(test.investment_outcome(1000),range(0,2002,2))

if __name__ == '__main__':
	unittest.main()

