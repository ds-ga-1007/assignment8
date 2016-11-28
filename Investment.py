import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

class InvSimulation():

	def __init__ (self, position, num_trials):

		self.position = position
		self.num_trials = num_trials

	def singleReturn(self):

		'''
		singleReturn simulates a one-day test, the result is the return of that particular day.
		'''
		
		chance_of_winning = 0.51
		self.value = 1000/self.position

		chance_array = np.random.binomial(1, chance_of_winning, self.position)

		single_trial = np.zeros(self.position)
		single_trial[:] = self.value

		for i in range(self.position):
			if chance_array[i] == 1:
				single_trial[i] *= 2
			else:
				single_trial[i] = 0

		single_ret = sum(single_trial)

		return single_ret

	def cumuReturn(self):

		'''
		singleReturn simulates a repeated test, 
		and the result is an array documenting everyday's return during the experiment.
		'''

		cumu_ret = np.zeros(self.num_trials)

		for test in range(self.num_trials):
			single_test = self.singleReturn()
			cumu_ret[test] = single_test

		return cumu_ret

	def dailyReturn(self):

		'''
		dailyReturn simulates a repeated test, 
		and the result is an array documenting everyday's ROI (return of investment) during the experiment.
		'''

		daily_ret = self.cumuReturn()/1000 - 1

		return daily_ret

	def EV(self):

		'''
		The mean of the daily ROI
		'''
		
		ev = np.mean(self.dailyReturn())
        
		return ev

	def SD(self):

		'''
		The standard deviation of the daily ROI
		'''

		std = np.std(self.dailyReturn())

		return std

	def result(self):

		'''
		The result will include two output formats:
		1. an text file containing the log of statistic summary of all historical experiment
		2. a histogram of the distribution of daily ROI.
		'''

	    pos_mean = self.EV()
	    pos_sd = self.SD()


	    text_file = open("results.txt", "a")
	    text_file.write("When position is %d:\n\
	    	The mean of daily return: %f,\n\
	    	The standard deviation of daily return: %f;\n"\
	    	 % (self.position, pos_mean, pos_sd))
	    text_file.close()

	    fig = plt.figure()
	    plt.hist(self.dailyReturn(),100,range=[-1,1])
	    plt.title('The Histogram of Daily Return When Position is %d' % self.position)
	    plt.xlabel('Daily Return')
	    plt.ylabel('Number of Trials')
	    plt.grid()
	    pdf_file = PdfPages('histogram_{:04d}_pos.pdf'.format(self.position))
	    plt.savefig(pdf_file, format='pdf')
	    pdf_file.close()


