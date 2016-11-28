# Author: Leslie Huang (lh1036)
# Description: InvestmentPositions class and methods.

import numpy as np
import re
from .exceptions import *

class InvestmentPositions(object):
    
    def __init__(self, count, value):
        '''
        Initializes an InvestmentPosition object with 
        count (number of shares) and value (denomination of investment position)
        '''
        
        self.count = count
        self.value = value
        
    def simulate_one_share(self):
        '''
        Simulates 1-day return for 1 investment position
        Per the instructions, returns 2 * starting value with Probability = 0.51 (if randnum > 0.49) 
        and 0 with Pr = 0.49 (if randnum <= 0.49)
        '''
        
        success = np.random.random() > 0.49
        return self.value * (2 if success else 0)
        
    def one_day_return(self):
        '''
        Runs independent simulation of 1-day return for each share in count (num shares purchased). 
        Returns the cumulative return (sum of 1-day return of each share)
        '''
        
        return sum(self.simulate_one_share() for i in range(self.count))
        
    def n_days_return(self, num_trials):
        '''
        Runs num_trials simulations of the 1-day return for user's number of shares. 
        Returns a list with num_trials elements. 
        Each list element is a separate simulation that calculates the 1-day cumulative 
        return for the number of shares and denomination
        '''
        
        return [self.one_day_return() for i in range(num_trials)]
        
    def __repr__(self):
        # Used in printing the results.txt file
        return "{} shares of ${}".format(self.count, self.value)
    
    def __eq__(self, other):
        return self.count == other.count and self.value == other.value
    
    @classmethod
    def parse_positions(cls, list_as_string, dollars = 1000, valid_share_counts = set([1, 10, 100, 1000])):
        ''' 
        Parse a list of positions (in String format).
        Returns list of InvestmentPositions objects.
        Raises InvalidListError if string is not correctly formatted as a "list"
        Raises InvalidPositionError if an invalid position value is entered
        '''
        
        if re.match(r"\[(\d+, )+\d+\]", list_as_string) is None:
            raise InvalidListError(list_as_string)
        
        # the user's input is "counts" instead of "positions" because they may not be valid positions
        counts = [int(num.strip().strip("[]")) for num in list_as_string.split(",")]
        
        # confirms that the user's inputs are valid positions
        for share_count in counts:
            if share_count not in valid_share_counts:
                raise InvalidPositionError(share_count)

        position_vals = [int(dollars / count) for count in counts]
        
        return [cls(count, val) for (count, val) in zip(counts, position_vals)]

