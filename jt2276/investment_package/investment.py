'''
Investment Class 
@author: jonathanatoy
'''

class investment(object):
    '''
    Class represents a string of $1000 investments and their daily returns
    '''


    def __init__(self, positions = [1], num_trials = 1):
        '''
        Constructor for interval class
        inputs:
                positions: A list of integers of number of shares to buy. Each entry must
                           be a factor of 1000.
                num_trials: An integer representing the number of days to simulate investment
                
        
        '''
        import numpy as np
        
        
        self.positions = np.array(positions)
        self.position_value = 1000 / self.positions
        self.num_trials = num_trials
        
        
    def gamble(self):
        '''
        Simulates 1 day of investments with a 51% chance of doubling each initial value
        and 49% chance of going bust.
        
        Output: numpy array corresponding to the cumulative return for each position in
        self.positions
        '''
        
        import numpy as np
        p = 0.51
        cumu_ret = []
        
        for i, position in enumerate(self.positions):
            position_return = 2 * self.position_value[i] * np.random.binomial(position, p)
            cumu_ret.append(position_return)
            
        return np.array(cumu_ret)
    
    def multi_day_gamble(self):
        '''
        Simulates 1 day of investments num_trials times repeatedly and returns the 
        percentage change of the original investment
        
        Output: n x m array corresponding to the cumulative return for each of 
        m positions in self.positions for each of n = num_trials trials
        '''
        
        import numpy as np
        daily_ret = []
        
        for trial in range(self.num_trials):
            cumu_ret = self.gamble()
            daily_ret.append((cumu_ret / 1000) - 1)
            
        return np.array(daily_ret)