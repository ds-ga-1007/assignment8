'''
Created on Nov 28, 2016

@author: sj238
'''
import numpy as np
import matplotlib.pyplot as plt

class Investment(object):
    '''
    classdocs
    '''
    def __init__(self, positions, num_trials):
        '''
        Constructor
        '''
        self.positions = positions
        self.num_trials = num_trials
        
        
    def simulation(self, positions, num_trials):
        '''
        This function repeat num_trials times simulation for each position in the list of positions.
        then generate and save the daily return performance as a list called daily_ret
   
        parameters:
            positions: a list of positions that invester would like to take
            num_trials: int, number of trials we want to simulate 
    
        returns: 
            position_ret: dictinary, keys are positions and values are a list of daily_ret
        '''
        position_ret = {}
        for pos in positions:
            position_value = 1000 / pos
            cumu_ret = np.zeros(self.num_trials)
            daily_ret = np.zeros(self.num_trials)
            for trial in range(self.num_trials):
                bet_outcome = np.random.binomial(1, 0.51, pos)*2
                #Because each bet is Bernoulli trial with p=0.51
                cumu_ret[trial] = sum(bet_outcome* position_value)
                daily_ret[trial] = cumu_ret[trial]/1000 - 1
            position_ret[pos] = daily_ret
        return position_ret
    
    def output_files(self,positions, num_trials):
        """
        This function fist call the method 'simulation' to get a daily_ret with respect to each position.
        Then, for each position, this function plot of the result of the trials in a histogram 
        with X axis from -1.0 to +1.0, and Y axis as the number of trials with that result and save it 
        as a pdf file.
        At last, for each position, this function generate the mean or 
        expected value of the daily return and the standard deviation of the daily return, and save them
        in a text file.

        parameters:
            positions: a list of positions that invester would like to take
            num_trials: int, number of trials we want to simulate 
    
        returns: NULL, generate and save some histogram graphs and a 'result.txt' file.
            
         """
        output_text = open('results.txt', 'w')
        result = self.simulation(positions, num_trials)
        for pos in positions:
            position_value = 1000 / pos
            mean = np.mean(result[pos])
            std = np.std(result[pos])
            plt.hist(result[pos],100,range=[-1,1])
            plt.savefig("histogram_"+str(pos).zfill(4)+"_pos.pdf")
            plt.close()
            output_text.write('For position :  {0}   with position Value:  {1} '.format(pos,position_value))
            output_text.write('  The mean is:  {0}  The standard deviation:  {1} \n'.format(mean,std))
        output_text.close()