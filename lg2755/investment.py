'''
Author: Lingshan Gao
Created on Nov. 27, 2016
'''

'''
References:
http://www.afterhoursprogramming.com/tutorial/Python/Writing-to-Files/
http://stackoverflow.com/questions/339007/nicest-way-to-pad-zeroes-to-string
'''

import numpy as np
import matplotlib.pyplot as plt

class Investment(object):
    '''
        This is a class that takes a list of shares as input, and simulates a one-day investment of $1000 given different strategies. It helps the investor to determine if the money should be invested as a lump sum or as separate shares.
    '''
    
    def __init__(self, positions, num_trails, rand_seed=None):
        '''
            Initiate the program. It take two required inputs: a list of shares to buy and number of trails for simulation, and one optional input: number of seed set.
        '''
        self.positions = positions
        self.num_trails = num_trails
        self.rand_seed = rand_seed
    
    def setSeed(self):
        if self.rand_seed is not None:
            np.random.seed(self.rand_seed)
    
    def calcPositionValue(self):
        self.position_value = 1000//np.array(self.positions)
    
    def calcCumulativeReturn(self):
        self.cumu_ret = np.zeros([len(self.positions), self.num_trails], dtype=int)
        for j in range(self.num_trails):
            for i in range(len(self.positions)):
                arr = np.random.random(self.positions[i])
                ret = sum((arr >= 0.49))*2*self.position_value[i]
                self.cumu_ret[i, j] = ret
    def calcDailyReturn(self):
        self.daily_ret = (self.cumu_ret/1000)-1
    
    def calcDailyReturnMean(self):
        self.daily_mean = np.zeros([len(self.positions)])
        for i in range(len(self.positions)):
            daily_mean_tmp = np.mean(self.daily_ret[i])
            self.daily_mean[i] = daily_mean_tmp

    def calcDailyReturnStd(self):
        self.daily_std = np.zeros([len(self.positions)])
        for i in range(len(self.positions)):
            daily_std_tmp = np.std(self.daily_ret[i])
            self.daily_std[i] = daily_std_tmp
                
    def saveResults(self):
        # Save the plots in pdf format
        for i in range(len(self.positions)):
            plt.figure()
            plt.hist(self.daily_ret[i],100,range=[-1,1])
            plt.savefig('histogram_%04d_pos.pdf'%self.positions[i])
        
        
        # Save mean and standard deviation to a text file
        mean = 'Mean of daily return for the positions of %s: %s'%(str(self.positions), str(self.daily_mean))
        std = 'Standard deviation of daily return for the positions of %s: %s'%(str(self.positions), str(self.daily_std))
        f = open('results.txt', 'w')
        f.write(mean+'\n'+std)
        f.close()


