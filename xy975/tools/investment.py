"""
This class is used to describe the cumu_ret and daily_ret of a investment.
"""
import numpy as np

class investment:
    def __init__(self, position, num_trials):
        """
        The input should be an integer.
        """
        self.position = position
        self.num_trials = num_trials
    
    def position_value(self):
        return 1000/self.position
        
    def cumu_ret(self):
        """
        The earning of this portfolio.
        """
        success = np.random.binomial(self.position, 0.51)
        cumu_earn = 2* success * self.position_value()
        return cumu_earn
        
    def daily_ret(self):
        """
        The ROI of this portfolio.
        """
        roi = self.cumu_ret()/1000 - 1
        return roi
        
    def simulation(self):
        """
        Simulate a fixed position in num_trials times.
        """
        simulation = np.zeros(self.num_trials)
        for i in range(self.num_trials):
            simulation[i] = self.daily_ret()
        return simulation
        