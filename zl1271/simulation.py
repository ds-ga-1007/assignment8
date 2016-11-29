'''
Created on Nov 27, 2016

@author: felix
'''
import numpy as np
from simu_funcs import get_invest_return_vec

class simulation(object):
    '''
    classdocs
    '''

    def __init__(self, positions, num_trials, money_to_invest = 1000):
        '''
        Constructor
        A simulation is defined by positions and number of trials
        '''
        self.positions = positions
        self.num_trials = num_trials
        self.money_to_invest = money_to_invest
    
    def get_position_values(self):
        self.values = [(self.money_to_invest / position) for position in self.positions]
    
    def simulate(self):
        self.get_position_values()
        self.simulate_results = np.zeros([self.num_trials,len(self.values)])
        
        print(self.values,self.positions,self.num_trials) #################################
        
        for trial in np.arange(self.num_trials):
            ii = 0

            for position_value in self.values:
                
                this_return = get_invest_return_vec(position_value,self.positions[ii])
                this_result = self.money_to_invest + np.sum(this_return)
                
            
                self.simulate_results[trial,ii] = this_result
                ii = ii + 1
        

        #print(self.simulate_results)###########################
        

    
    
    
    
    
    
    
    
    
    