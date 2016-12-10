#!/usr/bin/env python3

# Author: Leslie Huang (LH1036)
# Description: This program prompts the user for a list of investment positions and 
# number of simulations to run. It calculates the mean and standard deviation of the results
# for each position and saves them in results.txt. It generates a histogram of returns
# for each investment position.

from investment.positions import InvestmentPositions
import matplotlib.pyplot as plt
import statistics as stats
from investment.exceptions import *


def prompt_positions():
    '''
    Prompt user and read in keyboard input of investment positions
    Raises InvalidListError, InvalidPositionError, ValueError for incorrect inputs
    '''
    
    while True:
        try:
            userinput = input("Enter the positions as a list with one space after each comma.")
            return InvestmentPositions.parse_positions(userinput)
        
        except (InvalidListError, InvalidPositionError, ValueError) as e:
            print(e)
        
def prompt_trials():
    '''
    Prompt user for number of simulations
    Raises ValueError for invalid (non positive integer) input
    '''
    
    while True:
        try:
            num_trials = int(input("Enter the number of simulations. "))
        
            if num_trials > 0:
                return num_trials
    
            print("Invalid: Number must be a positive nonzero integer. Try again.")
        
        except ValueError:
            print("Number must be an integer. Try again.")
        
        
def calculate_daily_ret(cumu_ret):
    '''
    Returns list of the returns from each 1-day simulation
    '''
    return [ret / 1000 - 1 for ret in cumu_ret]

def calculate_daily_stats(daily_ret):
    '''
    For a simulation of 1-day returns, calculate mean and std dev
    '''
    return {
        "mean": stats.mean(daily_ret), 
        "standard deviation": stats.pstdev(daily_ret)
        }


# Runs the program in the terminal
if __name__ == "__main__":
    try:
        positions = prompt_positions()
        num_trials = prompt_trials()
        
        # Returns a list whose elements are lists (1 list per denomination of investment position) 
        # with num_trials elements, each of which is one independent 1-day simulation
        # for each share purchased in the denomination specified
        cumu_ret = [investment.n_days_return(num_trials) for investment in positions]

        daily_ret = [calculate_daily_ret(ret) for ret in cumu_ret]

        stats = [calculate_daily_stats(ret) for ret in daily_ret] 

        # Write measures of central tendency and corresponding positions to file
        with open("results.txt", "w") as file:
            for (position, stat) in zip(positions, stats):
                file.write("{}: {}\n".format(position, stat))

        # For each position, plot and save histogram for its simulation
        for (position, ret) in zip(positions, daily_ret):
            n, _, _ = plt.hist(ret, 100, range = [-1, 1])
            graphnum = str(int(position.value)).zfill(4) # graphs named using 4 digit integer with leading zeros, per instructions
    
            plt.axis([-1, 1, 0, max(n) * 1.1]) # set y axis to fit data with a 10% margin
            plt.xlabel("Rate of Return")
            plt.ylabel("Frequency")
            plt.title("Simulation Results for ${} Instrument".format(position.value))

            plt.savefig("histogram_{}_pos.pdf".format(graphnum))
            plt.close()
       
    except KeyboardInterrupt:
        '''
        Terminate the program if user keyboard interrupt
        '''
        
        pass 


# Sources consulted
# http://matplotlib.org/1.2.1/examples/pylab_examples/histogram_demo.html