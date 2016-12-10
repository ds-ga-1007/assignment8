""" This module contains class investment_instrument that generates daily returns for each position, produces a histogram (in a pdf file), and saves the mean and std of daily returns for each position in results.txt file."""

import sys
import os
import numpy as np
import re
from random import randint
import matplotlib.pyplot as plt

class investment_instrument:
    
    def __init__(self, position, num_trials):
        self.position = position        
        self.num_trials = num_trials
        self.position_value = np.true_divide(1000, self.position) 
        if self.position == 1:
            self.position_word = " position "
        else:
            self.position_word = " positions "
    
    
    def generate_daily_returns(self): 
        investment_outcome = []
        for i in range(self.position*self.num_trials):
            outcome_of_draw = np.random.binomial(1, 0.51)
            investment_outcome.append(self.position_value*2*outcome_of_draw)
        matrix_of_results = np.array(investment_outcome).reshape(self.position, self.num_trials).T
        cumu_ret = matrix_of_results.sum(axis=1)
        daily_ret =  (cumu_ret/1000)-1
        return daily_ret
    
    
    def histogram(self, daily_ret):
        plt.hist(daily_ret,100,range=[-1,1])
        plt.xlabel("Daily Return") 
        plt.ylabel("Distribution")
        plt.title("The histogram of the result for " + str(self.position) + self.position_word + "of $"+ str(int(self.position_value)))
        plt.xticks(fontsize=8) 
        plt.yticks(fontsize=8)
        label = "000" + str(self.position)
        plt.savefig('histogram_' + label[-4:] +'_pos.pdf')
        plt.clf()
        
    
    def summary_stats(self, daily_ret):
        file = open("results.txt", "a")
        mean = float(("{0:.5f}".format(daily_ret.mean())))
        std = float(("{0:.5f}".format(daily_ret.std())))
        
        file.write("RESULT FOR " + str(self.position) + self.position_word + "of $"+ str(int(self.position_value)) + '\n')
        file.write('Mean of the daily return:               ' + str(mean) + '\n')
        file.write('Standard deviation of the daily return: '+str(std) + '\n') 
        file.write('\n')
        file.close()
