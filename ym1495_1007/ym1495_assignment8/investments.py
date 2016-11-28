'''
Created on Nov 27, 2016

@author: muriel820
'''
import numpy as np
import exceptions
from exceptions import input_bound_exception

class investments(object):
    '''
    convert input strings into a list and an integer
    '''


    def __init__(self, positions_input, num_trials_input):
        '''
        Constructor
        '''
        if positions_input[0]!='[' or positions_input[-1]!=']':
            raise input_bound_exception
        