'''

This module contains:
 
Class: 
invest_simulation: simulating the investiment with 51% chance winning 1 unit, 49$ chance losing 1 unit

Methods:
(1) invest_simu
(2) investment_outcome: return the outcome of investiment in each days each trial
(3) save_histogram: save histogram in required form
(4) calc_mean_return: Calculate the mean value of daily return
(5) calc_std_return: Calculate the standard deviation of the daily return

Created on 2016/11/22
Version: 1.0
@author: liusheng
ShengLiu Copyright 2016-2017
'''
import matplotlib.pyplot as plt
import numpy as np


class invest_simulation:

	def __init__(self, positions,num_trials):
		'''
		Constructor
		'''
		self.positions = positions
		self.num_trials = num_trials


	def invest_simu(self):
		'''
		simulating the investiment
		'''
		cumu_ret ={}
		wtofile = ''
		f = open('results.txt','w')
		print('Writting the results.txt ....')
		for position in self.positions:
			# initiate daily return
			daily_ret = np.zeros(self.num_trials)
			position_value = 1000/position
			cumu_ret = self.investment_outcome(position)
			for trial in range(self.num_trials):
				daily_ret[trial] = (cumu_ret[trial]/1000) - 1
			self.save_histogram(daily_ret, position)
			f.write("@ position " + str(position) +'\n' +"the mean of expReturn is "   + str(self.calc_mean_return(daily_ret)) + "\nthe std of expReturn is " + str(self.calc_std_return(daily_ret)) + "\r\n\n")
			f.flush()
		print('Clsoe the results.txt ....')
		f.close()


	def investment_outcome(self,position):
		'''
		Get the outcome of each investiment
		'''
		position_value = 1000/position
		outcome = np.zeros(self.num_trials)
		chance = np.random.uniform(0, 1, size = self.num_trials * position)
		for trial in range(self.num_trials):
			investiment_return = 0
			for i in range(position):
				if chance[trial*position+i] <= 0.51:
					investiment_return += position_value * 2
			outcome[trial] =  investiment_return
		return outcome


	def save_histogram(self,daily_ret, position):
		'''
		Save the histogram 
		'''
		print ("Loading Fig" + str(position) + '...')
		fig = plt.figure()
		plt.hist(daily_ret,100,range = [-1,1])
		plt.savefig('histogram_'+ str(position).zfill(4) + '_pos.pdf')
		print("Figure" + str(position) + 'saved.\n')

		
		

	def calc_mean_return(self,ret):
		return np.mean(ret)

	def calc_std_return(self,ret):
		return np.std(ret)

if __name__ == '__main__':
	positions = [1, 10, 100, 1000]
	num_trials = 10000
	invest_simulation(positions, num_trials).invest_simu()
