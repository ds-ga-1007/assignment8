'''
Created on Nov 26, 2016

@author: Yovela
'''
import numpy as np
import matplotlib.pyplot as plt


class trial:
    
    def __init__(self, positions, num_trials):
        
        '''
        constructor
        '''
        
        self.positions = positions
        self.num_trials = num_trials
        

def simulation(position, num_trials):
        
    '''
    This function is to process the simulation
    Suppose further that we have $1000 to invest on the first day
    51% of the time the return is exactly 1.0 (the value doubles)
    49% of the time the return is exactly -1.0 (all value is loss)
    '''
    position_value = int(1000/position)
    
    cumu_ret = np.zeros(num_trials)
    daily_ret = np.zeros(num_trials)
               
    for trial in range(num_trials):
        cumu = 0
        for i in range(position):
            prob = np.random.uniform(0,1)
            if prob <= 0.51:
                cumu = cumu + 2 * position_value
            else:
                cumu = cumu
        cumu_ret[trial] = cumu
        daily_ret[trial] = (cumu_ret[trial]/1000)-1
    return daily_ret
    
def text_results(trial):
        
    '''
    This function is to print out results of simulation
    '''
        
    f = open('results.txt','w')
    
    for position in trial.positions:
        print (position)
        results = simulation(position, trial.num_trials)
        mean = results.mean()
        std = results.std()
        f.write("for position " + str(position) + ", mean = " + str(mean) + ", std =  " + str(std) + "\r\n")
            
        plt.hist(results,100,range=[-1.0,1.0])
        plt.ylabel("number of trials with that result")
        plt.xlabel('daily_ret for position' + str(position))  
        plt.savefig('histogram_' + str('0'*(4-len(str(position))) + str(position)) + '_pos.pdf')
        #plt.show()
   
    f.close()
    print("simulation finished, please check results in your current dictionary")
    return


