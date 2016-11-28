'''
Created on Nov 27, 2016

@author: muriel820
'''
import numpy as np
import exceptions
from exceptions import input_bound_exception,input_value_exception,input_trial_number_exception

class investments(object):
    '''
    convert input strings into a list and an integer
    '''


    def __init__(self, positions_input, num_trials_input):
        '''
        Constructor
        '''
        if positions_input[0]!='[' or positions_input[-1]!=']':
            raise input_bound_exception()
        else:
            positions = positions_input[1:-1].split(',')
            for i in range(len(positions)):
                try:
                    positions[i] = int(positions[i])
                except:
                    raise input_value_exception()
        self.positions = np.array(positions)
        self.position_values = np.floor(1000/self.positions)
        try:
            self.num_trials = int(num_trials_input)
        except:
            raise input_trial_number_exception()
        