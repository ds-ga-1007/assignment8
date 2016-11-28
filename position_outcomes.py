'''
Created on Nov 27, 2016
These functions assist the investment_portfolio class with generation of the daily investment outcome.
@author: danielamaranto
'''
import numpy as np
import random

#Determines the outcome of a single share
def share_result():
    result = random.uniform(0,1)
    if result <= 0.49:
        win = False
    else:
        win = True
    return win

#Determines the outcome of one day of trading
def cumu_ret(shares):
    wins = np.array([share_result() for i in range(shares)])
    return 2 * (1000/shares) * np.sum(wins)