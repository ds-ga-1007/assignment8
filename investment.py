'''
Created on Nov 24, 2016
I created a class that would perform all of the required calculation for each
position determined by the user.  Functions referenced by the class's attributes
are located in the position_outcomes module.
@author: danielamaranto
'''

import numpy as np
from position_outcomes import cumu_ret

class investment_position:
    def __init__(self, shares, trials):
        self.position = shares
        self.position_value = 1000/shares
        self.num_trials = trials
    
    def all_trials_result(self):
        trial_array = np.array([cumu_ret(self.position) for i in range(self.num_trials)])
        return trial_array
    
    def daily_ret(self):
        normalized_result = np.array([i/1000-1 for i in self.all_trials_result()])
        return normalized_result
    
    def mean(self):
        return self.daily_ret().mean()
    
    def stdev(self):
        return self.daily_ret().std()
    