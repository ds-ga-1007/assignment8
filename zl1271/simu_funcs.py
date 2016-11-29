'''
Created on Nov 27, 2016

@author: felix
'''

import re
import numpy as np

def valid_share_str(string):
    if not re.match(r"^((\d+,)*(\d+))$", string):
        # must be four ints separated by commas
        return False
    else:
        return True

def rm_ws(string):
    # remove white spaces
    new_str = re.sub(r'\s+', '', string)
    return new_str

def valid_trial_str(string):
    if not re.match(r"(\d+)$", string):
        # must be an int
        return False
    else:
        return True
    
def invest_return(bias_level = 0.51):
    return_rate = 0.0
    if np.random.rand(1)[0] >= bias_level:
        return_rate = -1.0
    else: 
        return_rate = 1.0
    return return_rate 

def get_invest_return_vec(position_value,position):
    # need both position_value and position so that if total money for investment changes this still work
    all_returns = np.zeros([position])
    for ii in np.arange(position):
        this_return = invest_return() * position_value
        all_returns[ii] = this_return
    return all_returns
        
    
    
    
    
    
    
    