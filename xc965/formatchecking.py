'''
This module allows users to validate the formats
of their customized postions set and number of trials.

Author: Xianzhi Cao (xc965)
'''

import re
from errors import *


def get_positions_set(pos):
    '''
    This function checks:
    whether the users' customized input positions set fits the format
    '''
    # remove whitespace from input position set
    pos = pos.replace(' ', '')

    # input format should conform to the format
    if pos == '':
        raise EmptyInputError
    elif not re.match(r'[\[]\d+(\,\d+)*[\]]$', pos):
        raise InputFormatError
    else:
        # convert input strings to a list
        positions_set = re.findall(r'\d+', pos)
        if '0' in positions_set:
            raise ZeroPositionError
        else:
            return positions_set


def get_num_trials(num):
    '''
    This function checks:
    whether the new number of trials is a positive integer.
    '''
    try:
        num = int(num)
        if int(num) <= 0:
            raise NonPositiveIntegerError
        else:
            return num
    except ValueError:
        raise NonNumericError
    except TypeError:
        raise NonNumericError
