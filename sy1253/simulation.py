'''
Created on Nov 27, 2016

@author: kevinyan


this module creates the class for simulation. Each object of simulation will have the following method.
'''
import numpy as np
import matplotlib.pyplot as plt


class simulation(object):


    def __init__(self, positions, num_trials):
    
        '''
        Constructor
        '''   
        self.positions = positions
        self.num_trials = num_trials  
    # set a value to represents the size of each investment
        self.position_value = 1000 / self.positions
    
    
    def cumu_return(self):
        '''
        this function simulates the investment and generates the daily return
        '''   
        cumu_ret = np.zeros(self.num_trials)
        daily_ret = np.zeros(self.num_trials)
        
        for trial in range(self.num_trials):
            ret = 0
            for j in range(self.positions):
                prob = np.random.rand(1) 
                if prob >= 0.49:
                    ret = ret + self.position_value * 2
             
            cumu_ret[trial] = ret
            daily_ret[trial] = (cumu_ret[trial] / 1000) - 1         
        return daily_ret
    


    def get_mean(self):
        '''
        this function returns the mean of the return of all the trails
        '''   
        return np.mean(self.cumu_return())
    
    def get_std(self):
        '''
        this function returns the standard deviation of the return of all the trails
        '''   
        return np.std(self.cumu_return())
        
    def present_result(self):
        '''
        this function plot the histogram of the return of all the trials
        '''         
        fig = plt.figure()          
        plt.title('histogram of position  ' + str(self.positions))
        plt.hist(self.cumu_return(), 100, range=[-1, 1])
        plt.ylabel('number of trials')
        plt.xlabel('daily return') 
        fig.savefig('histogram_' + str('0' * (4 - len(str(self.positions))) + str(self.positions)) + '_pos.pdf')
         

        
                 
                 
             
            
