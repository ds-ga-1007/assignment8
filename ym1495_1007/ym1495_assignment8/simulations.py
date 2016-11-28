'''
Created on Nov 28, 2016

@author: muriel820
'''

import numpy as np
import matplotlib as plt
from investments import investments

def cumu_ret(position_value):
    '''a single time operation'''
    prob = np.random.randint(100)
    if prob < 49:
        ret = 0
    else:
        ret = 2*position_value
    return ret

def daily_ret(position_value, position):
    '''complete a whole day's investment'''

    ret = 0
    for i in range(position):
        ret += cumu_ret(position_value)
    return_rate = float(ret)/1000 - 1   #return the daily return 
    return return_rate    

def multiple_trials(position_value, position, num_trials):
    '''keep testing and saving the results for a certain position'''
    ret = []
    for i in range(num_trials):
        ret.append(daily_ret(position_value, position))
    return ret

def plot_investment(position_value, position, num_trials):
    '''save histogram plot in a pdf file'''

    daily_ret_list = multiple_trials(position_value, position, num_trials)
    plt.figure()
    plt.hist(daily_ret_list, 100, range = [-1,1])
    plt.xlabel('Return Rate')
    plt.ylable('Number of Trials')
    plt.title('Return Rate Histogram with Positions: {}'.format(str(position)))
    plt.savefig('histogram_{}_pos.pdf'.format(str(position).zfill(4)))   #name the new file as required

