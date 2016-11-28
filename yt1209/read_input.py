'''
Created on Nov 27, 2016

@author: Yovela
'''
import sys


def read_position(user_input):
    position_list = []
    if isinstance(user_input, str) == True:    
        positions_str = user_input[2:-2].split(",")
        position_list = [int(p) for p in positions_str]
            
    for position in position_list:
        if position <= 0:
            raise ValueError("Invalid Input, please note that all elements must be non-negative integers")
 
    return position_list

def read_num_trials(user_input): 
    num_trials = int(user_input)  
    
    if num_trials <= 0:
        raise ValueError("Invalid Input, please note that num_trials must be a non-negative integer") 
     
    if isinstance(num_trials, int) == True:
        raise ValueError("Invalid Input, please note that num_trials must be a non-negative integer")      
    return num_trials
        