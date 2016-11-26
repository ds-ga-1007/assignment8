'''
Main Module for the simulation.
Functions:
is_int()
reading_in()
generate_report()
investment_simulation()

Created on Nov 21, 2016
Last Modified        : 
Version        : 1.0
@author: Nan Wu
@email: nw1045@nyu.edu
'''
from UserDefinedError import *
from investment import simulation
import numpy as np
import matplotlib.pyplot as plt

def is_int(s):
    ''' 
    little function to check the type of argument 
    Args:
        s: object
    Returns:
        bool: is or not the type of s is int 
    Raises:  
    '''
    try: 
        int(s)
        return True
    except ValueError:
        return False
def reading_in(positions,num_trials):
    '''
    This function handles with the interaction with user.  
    Args:
        positions
        num_trials
    Returns:
        num_shares: a list of shares for each simulation 
        num_trials: how many times to randomly repeat the test
    Raises:
        InputError
    '''
    
    positions = positions.split(',')
    num_shares=[]
    for num in positions:
        if is_int(num) and (num in ['1','10','100','1000']):
            num_shares.append(int(num))
        else:
            raise InputError
   
    if is_int(num_trials):
            num_trials=int(num_trials)
    else:
        raise InputError
    return num_shares, num_trials
def generate_report(daily_ret,pos):
    '''
    This function generates reports for each simulation.
    The numerical results with mean and variance of each simulation save in a file, results.txt.
    There will also be a histogram for each simulation. 
    Args:
       daily_ret: the daily return of the position
       pos: one position 
    Returns:
    Raises:

    '''
    hist_figure=plt.figure()
    plt.hist(daily_ret,100,range=[-1,1])
    hist_figure.savefig(''.join(['histogram_', str(pos).zfill(4),'_pos.pdf']))



def investment_simulation():
    '''
    This is the main function of the simulation
    Args:
    Returns:
    Raises:
        QuitSimulation
    '''
    print('This is a simulation of investments.')
    print('You can exit with "QUIT".')
    print("Please input a list of the number of shares to buy in parallel.")
    print('You can purchase it in $1, $10, $100, and $1000 denominations.')
    while True:
        try:
            positions = input("List of Numbers: ")
            if positions.upper() == 'QUIT':
                raise QuitSimulation
            num_trials = input('How many times to randomly repeat the test? ')
            if num_trials.upper() == 'QUIT':
                raise QuitSimulation
            num_shares, num_trials = reading_in(positions,num_trials)
            break
        except InputError:
            print('Invalid Input!\n Please according to the instruction!')
    file=open('results.txt','w')
    for pos in num_shares:
        cumu_ret=simulation(pos,1000/pos).outcome_total(num_trials)
        cumu_ret=np.array(cumu_ret)
        daily_ret=(cumu_ret/1000) - 1
        
        file.write(''.join(["Position:", str(pos)]))
        file.write('  '.join([" Mean:", str(daily_ret.mean())]))
        file.write('  '.join([" Standard Deviation:", str(daily_ret.std()), '\n']))
        
        generate_report(daily_ret,pos)
        
    file.close()
    print('Finish!')
    
    
        
        
            
    
        
        
                
               
            
        
    