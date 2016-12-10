import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

'''read input and initialize input values.'''
class user_input:
    #Initializing postions, value of positions, and number of trivals to repeat the test
    def __init__(self, positions, num_trials):
        self.num_trials     = num_trials
        self.positions      = positions
        


    
#Use NumPy's random number generating capability to simulate the outcome of one day of investment

def outcome(position,num_trials):
    position_value = int(1000/position)
    
    cumu_ret  = np.zeros(num_trials)
    daily_ret = np.zeros(num_trials)
        
    #Repeat num_trials times
    for trial in range(num_trials):
        ret=0
        for posi in range(position):
            if np.random.uniform(0,1) <0.49:
                cumu_ret[trial]=ret
            else:
                ret+= position_value*2
            cumu_ret[trial]=ret                   
            daily_ret[trial] = (cumu_ret[trial]/1000)-1
            
    return daily_ret
    
def result(user_input):
    f = open('results.txt', 'w')
    for position in user_input.positions:
        results=outcome(position,user_input.num_trials)
        #plot
        fig= plt.figure()
        plt.hist(results, 100, range=[-1,1])
        plt.title("Histogram for position"+str(position))
        fig.savefig("Histogram_for_position"+str(position)+".pdf")
        #stats
        mean = np.mean(results)
        std = np.std(results)
        f.write("for position"+str(position)+":"+"\r\n")
        f.write("mean: "+str(mean)+"; standard deviation: "+str(std)+"\r\n")
    f.close()
    return
    
