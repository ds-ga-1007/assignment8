'''
Created on Nov 23, 2016
@author: peimengsui
@define a class representing investment
'''

import numpy as np
import matplotlib.pyplot as plt

class investment:
    def __init__(self, num_positions,num_trials):
        '''
        Constructor
        '''
        self.num_positions = num_positions
        self.num_trials = num_trials
        self.position_value = 1000 / num_positions
    @staticmethod
    def simulate(investment):
        'simulation of investment and return daily return'
        cumu_ret = np.zeros(investment.num_trials)
        for i in range(investment.num_trials):
            ret = 0
            for j in range(investment.num_positions):
                chance = np.random.uniform(0,1)
                if chance<=0.51:
                    ret += investment.position_value*2
                cumu_ret[i] = ret
        daily_ret = (cumu_ret/ 1000.0) - 1.0
        return daily_ret
    @staticmethod
    def invest_trial(positions, num_trials):
        'simulate @positions invest combination and @num_trials number of trials'
        f = open('results.txt','w')
        for pos in positions:
            daily_ret = investment.simulate(investment(pos,num_trials))
            f.write("position " + str(pos) + ", mean: " + str(np.mean(daily_ret)) + ", std:  " + str(np.std(daily_ret)) + "\r\n")
            f.flush()
            fig = plt.figure()
            plt.hist(daily_ret, 100, range=[-1,1])
            plt.title("histogram_'+str(pos/1000)+'_pos")
            fig.savefig('histogram_'+str(pos/1000)+'_pos.pdf')
        plt.show()
        plt.close('all')
        f.close()
        print ("Finish Simulation")
if __name__ == "__main__":
    positions = [1, 10, 100, 1000]
    num_trials = 10000
    investment.invest_trial(positions, num_trials)