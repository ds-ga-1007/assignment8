"""
Created on Mon Nov 28 2016
@author: Yanan Shi/ys2506
@desc: define the class and related methods
"""

import matplotlib.pyplot as plt
import numpy as np

#Suppose we have an investment instrument with the following properties:
#You can purchase it in $1, $10, $100, and $1000 denominations.
#Holding time is one day.
#51% of the time the return is exactly 1.0 (the value doubles).
#49% of the time the return is exactly -1.0 (all value is lost).

class InvestmentInstrument(object):
    def __init__(self, positions, win_rate = 0.51, win_ravenue = 1., lose_ravenue = -1.):
        self.daily_ret = None
        self.positions = positions
        self.win_rate = win_rate
        self.win_ravenue = win_ravenue
        self.lose_ravenue = lose_ravenue

    #Accept the following inputs from the user:
    def investment_simulate(self, principal, num_trials):
        def revenue(position):
            def outcome(value):
                #Use NumPy's random number generating capability to simulate the outcome of one day of investment:
                ravenue = self.win_ravenue if np.random.uniform() <= self.win_rate else self.lose_ravenue
                return value * (1 + ravenue)
            #For each position, set a value to represents the size of each investment
            value = principal / position
            return sum(np.vectorize(outcome)(np.repeat(value, position))) / principal - 1
        #Repeat num_trials times
        return np.array([np.vectorize(revenue)(self.positions) for _ in range(num_trials)])


