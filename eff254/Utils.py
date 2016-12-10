# -*- coding: utf-8 -*-

import numpy as np

class negativeNumber(Exception):
    def __str__(self):
        return "Negative number"

class textInputedException(Exception):
    def __str__(self):
        return "Invalid interval exception"
    
class positionOver1000(Exception):
    def __str__(self):
        return "Position over 1000"

class singlePosition():
    
    ''' Class to define a single position'''
    
    def __init__(self, position):
        
        self.position = position
        
        try: 
            self.numShares = int(position)
        except:
            raise textInputedException(Exception) 
            
        self.position_value = 1000 /self.numShares       
        if self.numShares<0: 
            raise negativeNumber() 
        
        if self.numShares>1000:
            raise positionOver1000()  

class textTrialInputedException(Exception):
    def __str__(self):
        return "Invalid trial exception"

class number_trials: 
    
    ''' Class to define the number of trials'''
    
    def __init__(self, trials):
        try: 
            self.number = int(trials)
        except:
            raise textTrialInputedException(Exception) 
        
        
def uniform01ToBinary(rand):
    
    ''' A simple function to transform a number in the range 0-1 to 
    a binary variable according to probabilities in the assignment'''
    
    if rand<=0.49:
        binary = 0
    else:
        binary = 1
        
    return binary


def singleSimulation(rand, position):
    
    '''Function to take the value of 0 or position_value times 2 according to above probabilities'''
    
    if uniform01ToBinary(rand)==0:
        retunrOfInvestment = 0
    if uniform01ToBinary(rand)==1:
        retunrOfInvestment = position.position_value * 2
        
    return retunrOfInvestment


def positionGainSimulation(position):
    
    '''Function to do the simulations to all possible number of shares that you can buy with the $1000 dlls.'''
    
    result = 0 
    
    randomNumbers = np.random.rand(position.numShares)
    
    for x in range(0, position.numShares):
        result = result + singleSimulation(randomNumbers[x], position)
        
    return result

def positionGainMultipleSimulation(position, ntimes):
    
    '''Do the above function ntimes, and return a numpy array with the results'''
    
    cumu_ret = np.empty(ntimes) * np.nan
    
    for x in range(0,ntimes):
        cumu_ret[x] = positionGainSimulation(position)
        
    return cumu_ret 