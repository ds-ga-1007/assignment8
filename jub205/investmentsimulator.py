"""
Created on Fri Nov 25 2016

@author: jinubak/jub205
@desc: This file contains classes and functions needed for
	   investment simulation.
"""

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class InvestmentPortfolio():
    '''
    InvestmentPortfolio class for daily investment simulation
    '''
    
    def __init__(self, position, num_trials):
                
        self.position = position
        self.num_trials = num_trials
        self.position_value = 1000/position
        self.cumu_ret = []
        self.daily_ret = []
        self.mean = 0.0
        self.std_dev = 0.0
        
    def DailySimulation(self):
        '''
        This function runs daily simulation for each position 
        in the investment portfolio with 51% chance of winning
        '''
        
        betresult = np.random.uniform(size=self.position) #Generate random bet results
        betsWon = betresult  > 0.49 #Filter out winning bets
        
        position_ret = sum(betsWon*(self.position_value)*2) #Compute cumulative return for portfolio
        self.cumu_ret.append(position_ret)
        
        daily_ret = (position_ret/1000) - 1 #Compute daily return
        self.daily_ret.append(daily_ret)
    
    def InvestmentSimulation(self):
        '''
        This function runs simulation for given number of trials.
        '''        
        for i in range(self.num_trials):
            self.DailySimulation()
            
    def compute_mean(self):
        '''Function used to compute mean of daily return'''
        
        self.mean = np.array(self.daily_ret).mean()
                
    def compute_std_dev(self):
        '''Function used to compute standard deviation of daily return'''
        
        self.std_dev = np.array(self.daily_ret).std()
        
def plot_hist(daily_ret, position_size):
    '''
    This function plots histogram of given daily return and position value.
    It also saves plot to PDF file.
    '''    
    
    plt.xlabel('Daily return')
    plt.ylabel('Count')
    plt.title('Daily returns Histogram for %d position(s)'%position_size)
    plt.hist(daily_ret, 100, range=[-1,1])
    plt.savefig('histogram_%s_pos.pdf'%(str(int(position_size)).zfill(4)))
    plt.close("all")

def format_position_input(positions):
    '''Function to handle user input for positions list'''

    raw_positions = positions.replace("[","").replace("]","")
    position_list = raw_positions.split(",")
    formatted_pos = []

    try:
        for i in position_list:
            position = int(i.strip())
            if position <= 0 or position>1000:
                raise ValueError #Zero/Negative/value over 1000 not allowed
            else:
                formatted_pos.append(position)

    except ValueError:
        print("Invalid input for positions list!")
        sys.exit("Exit the program")

    else:
        return formatted_pos
        
def format_num_trials(num_trials):
    '''Function to handle user input for number of simulations'''

    try:
        formatted_num_trials = int(num_trials)
        if formatted_num_trials <= 0:
            raise ValueError #Zero/Negative value not allowed

    except ValueError:
        print("Invalid input for number of trials!")
        sys.exit("Exit the program")

    else:
        return formatted_num_trials
