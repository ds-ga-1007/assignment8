'''
Created on Nov 22, 2016

@author: Caroline
'''
import numpy as np
import Investment as inv

def double_or_lose(amount):
    '''determines whether the amount will increase or decrease'''
    outcome = np.random.randint(1, 101, 1, int)
    if outcome < 50:
        new_amount = 0
    elif outcome >= 50:
        new_amount = amount*2
    return new_amount

def invest(Investment):
    '''invests however many small investments we have and returns the total'''
    investments = [double_or_lose(Investment.position_value) for p in range(Investment.position)]
    return sum(investments)

def simulate_trials(Investment, num_trials):
    cumu_ret = np.ones(num_trials)*-1
    for trial in range(0, num_trials):
        cumu_ret[trial] = invest(Investment)
    return cumu_ret