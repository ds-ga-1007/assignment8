import numpy as np
import matplotlib.pyplot as plt

class investment:

	def __init__(self, positions, num_trials):
		#class intercal constructor
		self.positions = positions
		self.num_trials = num_trials


	def stimulate(self, position_values, num_trials):
		"""
		function stimulate repeat num_trials times stimulation for each value in
		position_values and return save their result as a list called daily_ret
   
		parameters:
			position_values: a list of value that represent the size of each investment
			num_trials: int 
    
		returns: 
			result: dictinary with a list of positions as keys and a list of daily_ret as values
		"""
		result = {}
		for p in position_values:
			cumu_ret = np.zeros(num_trials)
			daily_ret = np.zeros(num_trials)
			for t in range(self.num_trials):
				cumu_num = 0
				for i in range(int(1000/p)):
					random_num = np.random.rand()
					if (0 <= random_num <= 0.51):
						cumu_num = cumu_num + 2 * p
					elif (1 > random_num > 0.51):
						cumu_num = cumu_num 
				cumu_ret[t] = cumu_num
				daily_ret[t] = cumu_ret[t]/1000 - 1
			result[int(1000/p)] = daily_ret
		return result

	def represent_results(self, positions, num_trials):

		"""
		Function represent_results fist call the method 'stimulate' to get a dictionary with lists of daily_ret
		as values, and then plot the result in a histogram as well as creat a file 'result.txt' with mean, standard
		devaition information. 
   
		parameters:
			positions: list of int
			num_trials: int 
    
		returns: NULL
			create some histogram graphs and a 'result.txt' file.
 		"""


		position_values = [1000 / p for p in positions]
		result = self.stimulate(position_values, num_trials)

		f = open('results.txt', 'w')

		for p in positions:
			plt.hist(result[p],100,range=[-1.0,1.0])
			plt.ylabel("number of trails with the corresponding x result")
			plt.xlabel('daily_ret')

			if p == 1:
				plt.savefig('histogram_0001_pos.pdf')
			elif p == 10:
				plt.savefig('histogram_0010_pos.pdf')
			elif p == 100:
				plt.savefig('histogram_0100_pos.pdf')
			elif p == 1000:
				plt.savefig('histogram_1000_pos.pdf')
			plt.close()

			
			ret = np.asarray(result[p])
			ret_mean = np.mean(ret)
			ret_std = np.std(ret)
			f.write('The mean of daily return for positon {0} is {1}\n'.format(p, ret_mean))
			f.write('The standard deviation of daily return for positon {0} is {1}\n'.format(p, ret_std))

		f.close()









