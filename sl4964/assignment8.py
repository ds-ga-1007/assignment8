'''
Created on Nov 27, 2016

This is a program that simulates the return on an investment.

@author: ShashaLin
'''
from Error import InputError 
from Functions import cumu_return, repeat, makefig, save_results
import numpy as np

input_counter = 1 
while input_counter != 0:
    inp = input('Type in some positions, each separated by a comma and space. Do not include brackets.')
    try:
        positions = inp.split(', ')
        for index, position in enumerate (positions):
            positions[index] = int(position)       #cast positions into integers
        input_counter -=1
    except InputError:
        raise InputError('Invalid input. Input for positions has to be numbers separated by a comma and a space.')

input_counter += 1
while input_counter != 0:
    inp2 = input('Type in number of trials to run.')  
    try:  
        num_trials = int(inp2) 
        input_counter -= 1    
    except:
        raise InputError('Invalid input. Input has to be a number.')

position_value = 1000/np.array(positions)

for index, value in enumerate(position_value):
    daily_ret = makefig(index, value, positions, num_trials)
    save_results(positions, index, daily_ret)
    

    
    
