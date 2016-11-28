'''
Created on Nov 28, 2016

@author: Zahra Kadkhodaie
'''
from investment import *


def total_gain(sharesNumber, num_trials):
    '''This function gets a position, number of shares in one day, and number of trials or days. 
    It returns the total gain over all the trials.'''
    from numpy import zeros
    daily_ret = zeros((num_trials,1))
    for trial in range(num_trials):
        position_object = investment(sharesNumber) #Create an investment object
        daily_ret[trial,0] = position_object.daily_gain() #find the gain in a single day
    return daily_ret