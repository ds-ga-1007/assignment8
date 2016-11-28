import numpy as np
import matplotlib.pyplot as plt

'''
class investment contains functions simulation, histogram, stats
'''
class investment:
    '''initialize position, num_trials, and position_value'''
    def __init__(self, position, num_trials):
        self.position = position
        self.num_trials = num_trials
        self.position_value = int(1000/position)
    
    '''Simulate investment depending on position in a single day'''      
    def simulation(self):
        cumu_ret = np.zeros(self.num_trials)
        daily_ret = np.zeros(self.num_trials)
        for trial in range(self.num_trials):
            rand_int = np.random.randint(100,size = self.position)
            for pos in range(self.position):
                if rand_int[pos] < 49:
                    cumu_ret[trial] = cumu_ret[trial]
                else:
                    cumu_ret[trial] += self.position_value * 2
            daily_ret[trial] = (cumu_ret[trial]/1000) - 1
        return(daily_ret)
    
    '''Plot histogram for the daily investment outcome for each position'''       
    def histogram(self):
        daily_ret = self.simulation()
        fig = plt.figure()
        plt.hist(daily_ret,100,range=[-1,1])
        plt.title("The result of trials for position" + str(self.position))
        plt.xlabel('Daily Outcome')
        plt.ylabel('Number of trials')
        fig.savefig("histogram_" + str(self.position) + "_pos.pdf")
    
    '''Calculate mean and standard deviation for each position'''   
    def stats(self):
        daily_ret = self.simulation()
        mean = np.mean(daily_ret)
        std = np.std(daily_ret)
        return [mean, std]