'''
Created on Nov 27, 2016

@author: muriel820
'''
import numpy as np
import exceptions
from ym1495_assignment8.exceptions import input_bound_exception,input_value_exception,input_trial_number_exception

def investments(positions_input):
        '''
        Constructor
        '''
        positions = []
        if positions_input[0]!='[' or positions_input[-1]!=']':
            raise input_bound_exception()
        else:
            positions = positions_input[1:-1].split(',')
            for i in range(len(positions)):
                try:
                    positions[i] = int(positions[i])
                except:
                    raise input_value_exception()
        return positions

def position_values(positions):
    array = np.array(positions)
    value_array = np.around(1000/array, decimals=2)
    return value_array

        
def trials(num_trials_input):          
    try:
        num_trials = int(num_trials_input)
    except:
        raise input_trial_number_exception()
    return num_trials