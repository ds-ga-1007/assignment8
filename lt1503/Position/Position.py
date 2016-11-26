import pandas as pd
import numpy as np
import matplotlib
import sys

def get_integer_if_possible(s):
    """get an integer from the input, or raise a value error if s does not represent an integer"""
    try: 
        return int(s)
    except ValueError:
        raise ValueError('%s is not an integer' % (s))

def weightedcoinflip(probabilty):
    return np.random.rand() > probabilty

def get_position_list(share_list):
    
    """get list of positions from string of positons, or raise a ValueError"""
    if not isinstance(share_list, str):
        raise ValueError("get_interval_list only takes in strings. Received %s" % (type(share_list)))
    cleaned_input = share_list.strip()
    split_positions = str.split(cleaned_input, ',')
    
    positions = []
    for num_shares_input in split_positions:
        num_shares_processed = get_integer_if_possible(num_shares_input)
        positions.append(position(num_shares_processed))
    return positions

class position(object):
    def __init__(self, num_shares):
        INITIAL_INVESTMENT = 1000
        self.num_shares = num_shares
        self.share_value = INITIAL_INVESTMENT / num_shares
        self.total_value = 0
        
    def bet_shares_independently(self, probabilty = 0.51):
        for share in range(self.num_shares):
            if weightedcoinflip(probabilty = probabilty):
                self.total_value += self.share_value * 2
            
    @property
    def num_shares(self):
        return self._num_shares

    @num_shares.setter
    def num_shares(self, num_shares):
        if not num_shares in [1, 10, 100, 1000]:
            raise ValueError('%s needs to be an exponent of 10 between 1 and 1000' % (num_shares))
        self._num_shares = num_shares