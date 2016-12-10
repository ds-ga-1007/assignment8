'''
This module simulates multiple daily returns with a given position value.
Each daily investment is independent.

Author: Xianzhi Cao (xc965)
'''

import numpy as np
import pandas as pd


class investment(object):
    '''
    This class contains attributes and methods of daily investment
    with total capital = $1,000.
    '''
    def __init__(self, position, num_trials):
        self.position = int(position)
        self.num_trials = int(num_trials)

    def daily_returns(self):
        '''
        This function simulates multiple trials of daily investments
        with a chosen number of denominations.
        ---
        Returns a numpy array.
        '''
        # the worth of each position with a total of 1,000 dollars
        position_value = 1000 / self.position

        cumu_ret = np.zeros(self.num_trials)
        daily_ret = np.zeros(self.num_trials)

        # Simulate the outcome of one day investment
        for trial in range(self.num_trials):
            # Step 1: generate a random list with size of chosen position
            gain_loss_list = np.random.uniform(size=self.position)

            # Step 2: get the daily weighted investment outcome
            cumu_ret[trial] = sum(gain_loss_list <= .51) * 2 * position_value

            # Step 3: regularize the outcome values
            daily_ret[trial] = (cumu_ret[trial]/1000 - 1)

        return daily_ret
