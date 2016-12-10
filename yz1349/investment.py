import unittest
import numpy as np    

class investment():
    '''Takes an position from [1,10,100,1000] and creates an investment object with attributes: position and position_value.
    This class also has a method that returns an array of daily outcome of an investment and returns the total return in one day.'''
    
    def __init__(self, position):
              
        if position in [1,10,100,1000]:
            self.position = position  
            self.position_value = 1000/position  
        else:
            raise ValueError('Invalid position value, must be either of 1, 10, 100, 1000.') 
        
        self.cumu_ret, self.gain_day = self.outcome_day() 
    
    def outcome_day(self):
        '''Returns an array that contains all the investment outcomes in one day'''

        cumu_ret = np.zeros((self.position,1))
        
        for thistrial in range(self.position):
            if np.random.uniform(low=0.0, high=1.0, size=1) < .49:  
                cumu_ret[thistrial] = 0 
            else: 
                cumu_ret[thistrial] = self.position_value*2
           
        gain_day =  (np.sum(cumu_ret)/1000) -1   
            
        return cumu_ret, gain_day


def total_gain(numberofshares, num_trials):
    '''This function takes a number of shares in one day and total number of trials and 
    returns the total gain over all the trials.'''
    daily_ret = np.zeros((num_trials,1))
    for thistrial in range(num_trials):
        thisinvestment = investment(numberofshares) 
        daily_ret[thistrial] = thisinvestment.gain_day
    return daily_ret

if __name__ == '__main__':
    unittest.main()