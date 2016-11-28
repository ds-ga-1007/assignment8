import numpy as np
import matplotlib.pyplot as plt

'''
Created on Nov 27, 2016

@author: sunyifu
'''

class investment(object):
    '''
    classdocs
    '''


    def __init__(self, position,num_trials):
        '''
        Constructor
        '''
        self.position = position
        self.num_trials = num_trials
        self.position_value = 1000 / position
        
    def simulate(self):
        '''
        simulate the investment
        '''
        cumu_ret = np.zeros(self.num_trials)
        daily_ret = np.zeros(self.num_trials)
        for trial in range(self.num_trials):
            invest_rate = np.random.uniform(0, 1, size = self.position)
            for p in range(self.position):
                if     0 < invest_rate[p] < 0.49:
                    cumu_ret[trial] = cumu_ret[trial]
                else :
                    cumu_ret[trial] += self.position_value * 2
                    
            daily_ret[trial] = (cumu_ret[trial]/1000) - 1       
        return daily_ret
    
    def output_histogram(self):
        '''
        draw histogram
        '''
        daily_ret = self.simulate() 
        fig = plt.figure()
        plt.hist(daily_ret,100,range=[-1,1])
        plt.xlabel('daily_ret')
        plt.ylabel('number of trials')
        fig.savefig("histogram_" + str(self.position) + "_pos.pdf")
        plt.close()
        
        
        
    def print_result(self):
        
        '''
        write the result into file
        '''
        f = open('results.txt','a')
        daily_ret = self.simulate()
        mean = np.mean(daily_ret)
        std = np.std(daily_ret)
        f.write("position " + str(self.position) +'\n' +"the mean of Daily Return is "   + str(mean) + "\nthe std of Daily Return is " + str(std) + "\r\n\n") 
        f.close()   
        