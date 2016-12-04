'''
Created on 2016年12月4日

@author: bz866
'''

import numpy as np
import matplotlib.pyplot as plt
from Investment.exp_handle import *

class trialInput(object):
    def __init__(self, positionList, num_trials):  
        if not isinstance(positionList, list):
            raise InvalidListError()
        else:
            denominations = [1000,100,10,1]
            for i in range(len(positionList)):
                if 1000/positionList[i] != denominations[i]:
                    raise PositionError()
        if not isinstance(num_trials, int):
            raise ValueError() 
        
        self.positionList = positionList
        self.num_trials = num_trials
    
    
    '''function that repeat num_trail times stimulation for each in 
    position_values and return their results as daily_ret.
    Meanwhile, it represent results. 
    '''    
    def stimulate(self):
        f = open('results.txt', 'w')
        for p in self.positionList:
            cumu_ret=np.zeros(self.num_trials)
            daily_ret=np.zeros(self.num_trials)
            for t in range(self.num_trials):
                cumu_num = 0
                for i in range(int(1000/p)):
                    random_num = np.random.rand()
                    if (0 <= random_num <= 0.51):
                        cumu_num = cumu_num + 2 * p
                    elif (1 > random_num > 0.51):
                        cumu_num = cumu_num 
                cumu_ret[t]=cumu_num
                daily_ret[t]=(cumu_ret[t]/1000)-1
            plt.clf()
            plt.hist(daily_ret,100,range=[-1,1])
            plt.xlabel('Daily Returns')
            plt.ylabel(str(p) + 'trails result')
            
            if p ==1:
                plt.savefig('histogram_0001_pos.pdf')
            elif p == 10:
                plt.savefig('histogram_0010_pos.pdf')
            elif p ==100:
                plt.savefig('histogram_0100_pos.pdf')
            elif p ==1000:
                plt.savefig('histogram_1000_pos.pdf')
                
            ret_mean = np.mean(daily_ret)
            ret_std = np.std(daily_ret)
            f.write('mean of return for position ' + str(p) + ' : ' + str(ret_mean) + '\n')
            f.write('std of return for position ' + str(p) + ' : ' + str(ret_std) + '\n')
            
        f.close() 