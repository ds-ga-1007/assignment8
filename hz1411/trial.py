
import numpy as np
import matplotlib.pyplot as plt

class trial:
'''
This class is defined to do simulations for a specific position,
calculate daily returns and its mean and std & plot histograms.
'''
    def __init__(self, position, num_trials):
    '''
    initialize with input variables
    '''
        self.position = position
        self.num_trials = num_trials
        self.position_value = int(1000 / position)
    
    def simulation(self):
    '''
    Simulate daily result of investment using numpy's 
    binimial(Bernoulli) distribution generator with p = 0.51.
    Then calculates and return daily return.
    '''
        cumu_ret = []
        daily_ret = []
        for trial in range(self.num_trials):
            result = np.random.binomial(1,0.51,size = self.position)
            win = sum(result)
            ret = self.position_value*2*win
            cumu_ret.append(ret)
            daily_ret.append(ret/1000-1) 
        return daily_ret
    
    def mean_std(self):
    '''
    Calculate and return the mean and standard deviation of daily return.
    '''
        ret = self.simulation()
        mean = np.mean(ret)
        std = np.std(ret)
        return mean,std
        
    def plot_hist(self):
    '''
    Plot the result of the trials in a histogram and generate a pdf file
    '''
        ret = self.simulation()
        f = plt.figure()
        plt.hist(ret, 100, range=[-1,1])
        plt.ylabel("Num of trials")
        plt.xlabel("Daily return")
        plt.title("Position = "+ str(self.position))
        f.savefig('histogram_'+str(self.position).zfill(4)+'_pos.pdf')   
        
        