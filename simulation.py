import numpy as np
import matplotlib.pyplot as plt

'''This module "simulation" have two functions. The first function takes in two parameters, number of
positions bought and number of times to simulate. Daily return, the mean and standard deviation of daily
return are all calculated. The second function takes in one parameter and draws a histogram for each
 daily return'''

class simulation:
    def __init__(self, position, num_trials):
        position_value = 1000 / position
        self.cumu_ret = []
        ret_list = []
        for i in range(num_trials):
            cumu_ret = 0
            for j in range(position):
                chance = np.random.uniform(0, 1)
                if chance <= 0.51:
                    cumu_ret += position_value * 2
                else:
                    cumu_ret += 0
            ret_list.append(cumu_ret/1000.0 - 1)
        self.daily_ret = np.asarray(ret_list)
        self.mean = self.daily_ret.mean()
        self.std = self.daily_ret.std()

    def histogram(self,f_name):
        plt.hist(self.daily_ret, 100, range = [-1,1])
        plt.xlabel('Daily_ret')
        plt.ylabel('Number of trials')
        plt.savefig(f_name)
        plt.close()
