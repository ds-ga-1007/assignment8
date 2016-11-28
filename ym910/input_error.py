'''
This Module read-in inputs as readable format and deals with possible errors.
'''
import sys

def input_positions(inpt):
    position_list=[]
    p=inpt[1:-1].split(",") #a position string
    position_list=[int(p[0]),int(p[1]),int(p[2]),int(p[3])]
    for position in position_list:
        if position <=0:
            raise ValueError("Please input positive integers.")
    return position_list
            

def input_trials(inpt):
    num_trials=int(inpt)
    if num_trials <=0:
        raise ValueError("Invalid input. Please input an positive integer.")
    else:
        return num_trials
