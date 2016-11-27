
# coding: utf-8

# In[3]:

import numpy as np
import matplotlib.pyplot as plt

class investment:
    """Create class investment"""
    def __init__(self, positions, num_trials):
        """Constructing the class"""
        self.positions = positions
        self.num_trials = num_trials
        self.position_value = 1000 / positions
        
    def simulate(self):
        """Simulating outcome of investment"""
        cumu_ret = np.zeros(self.num_trials)
        for trial in range(self.num_trials):
            outcome = 0
            for p in range(self.positions):
                random = np.random.rand()
                if random <= 0.51:
                    outcome += self.position_value * 2
                cumu_ret[trial] = outcome
        daily_ret = (cumu_ret / 1000) - 1
        return daily_ret
    
    def output(positions, num_trials):
        """Creating graph and text file by running simulations"""
        file = open('results.txt', 'w')
        for p in positions:
            daily_ret = investment.simulate(investment(p, num_trials))
            hist = plt.figure()
            plt.hist(daily_ret, 100, range=[-1, 1])
            plt.xlabel('Trials')
            plt.ylabel("daily_ret")
            plt.title('Histogram of position ' + str(p))
            hist.savefig('histogram_%04d_pos.pdf' % p)
            plt.close('all')

            file.write("The mean of daily return for position " + str(p) + " is " + str(np.mean(daily_ret)) + "\n")
            file.write("The standard deviation of daily return for position " + str(p) + " is " + str(np.std(daily_ret)) + "\n")
        file.close()
        print("Done")

