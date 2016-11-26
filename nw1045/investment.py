'''
Created on Nov 21, 2016
Last Modified        : 
Version        : 1.0
@author: Nan Wu
@email: nw1045@nyu.edu
'''
import numpy as np
class simulation:
    '''
    This is a class for simulation of every day 's result of the investment
    Methods:
      outcome: simulation of every day 's result of the investment
      outcome_total: a list of specific number of days' results.
    '''

    def __init__(self, position, position_value):
        '''
        init with input arguments: position and position_value
        '''

        self.position_value=position_value
        self.position=position
        
    def outcome(self):
        '''
        returns daily return of this position
        '''
        return sum(np.random.binomial(1, 0.51, self.position)*2*self.position_value)
    
    def outcome_total(self,trial):
        '''
        Args:
          trial: how many times need to be simulate
        return: a list of specific number of days' results.
        
        '''
        return [self.outcome() for day in range(0,trial)]
    
        
        
        