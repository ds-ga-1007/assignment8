""" class invest is used to compute the investment returns and output results and histogram """

import numpy as np
import matplotlib.pyplot as plt

# Define a class called invest which can take two sets of inputs to do simulations such that
# positions: a list of the number of shares to buy in parallel, i.e., [1,10,100,100]
# num_trials: the number of times to randomly repeat the test

class invest:
    def __init__(self, positions, num_trials):
        self.posits = positions
        self.trials = num_trials

    def bet(self):
        
        # start to write results to results.txt, using open() based on online Python doc
        report = open('results.txt', 'w')
        
        for position in self.posits:
            position_value = 1000 / position    # size of each investment
            cumu_ret = np.zeros(self.trials)    # initialize the array of outcome of one day of investment
            daily_ret = np.zeros(self.trials)   # initialize the array of result of each day
            
            for trial in range(self.trials):
                # investment instrument based on the 49% for losing all and 51% for value doubles
                bet = np.random.choice([0,2],p=[0.49,0.51],size=position)  # learn from NumPy v1.11 Manual
                cumu_ret[trial] = sum(position_value * bet)    # get return of one day investment
                daily_ret[trial] = (cumu_ret[trial]/1000) - 1  # get the daily return
        
            daily_ret_mean = np.mean(daily_ret) # mean of the daily return
            daily_ret_sd = np.std(daily_ret)    # standard deviation of the daily return
            
            # create histograms
            # savefig learned from matplotlib.org
            plt.hist(daily_ret, 100, range=[-1,1])
            plt.savefig('histogram_' + str(position).zfill(4) + '_pos.pdf') # use .zfill(width=4) to fill zeros if the string less than 4 characters  
            plt.close()
            
            # set the content and format for the results.txt 
            report.write('Position: {0}, Position Value: ${1}, Mean: {2}, Standard Deviation: {3}\n'.format(position, position_value, daily_ret_mean, daily_ret_sd))
        report.close()
