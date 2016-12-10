'''
Created on Nov 27, 2016
@author:Zhiqi Guo
@email: zg475@nyu.edu
'''
import numpy as np 
import matplotlib.pyplot as plt

class investment(object):
    '''
    The investment class inits number of shares to buy(num_positions) and number of times to repeated 
    the test(num_trials). It also contains two methods: get_cumu_ret and get_daily_ret.
    '''
    def __init__(self, num_positions,num_trials):
        '''
        Constructor
        '''
        self.num_positions  = num_positions                     #number of shares to buy in parallel
        self.num_trials = num_trials                            #how many times to randomly repeat the test
        self.position_value = 1000 / self.num_positions         #value to represents the size of each investment


    def get_cumu_ret(self):
        '''
        The method returns cumulative return, which is the outcome of 
        simulation of one day's investment for different choice of positions.
        '''
        uniform_list = np.random.uniform(0,1,self.num_positions)
        result = np.zeros(self.num_positions)
        for i in range(self.num_positions): 
            if uniform_list[i] <= 0.49:
                result[i] = self.position_value*(1-1)
            else:
                result[i] = self.position_value*(1+1)
    
        return sum(result)   

    def get_daily_ret(self):
        '''
        The method return a list contains daily return, every item in the list 
        is the result of simulation of every single day of trading.
        '''
        daily_ret = np.zeros(self.num_trials)
        cumu_ret  = np.zeros(self.num_trials)
        for trial in range(self.num_trials):
            cumu_ret[trial] = self.get_cumu_ret()
            daily_ret[trial] = (cumu_ret[trial]/1000) - 1
        
        return daily_ret
    
def simulate(position,num_trials):
    '''
    The method plot different histograms corresponding to different position choice,
    and also write and save the mean and std deviation of daily return to a txt file.
    '''
    f = open("results.txt", "w")
    for pos in position:
        fig = plt.figure()
        daily_ret = investment(pos,num_trials).get_daily_ret()
        plt.hist(daily_ret,100,range=[-1,1])
        fig.savefig('histogram_'+str(pos)+'_pos.pdf')
        mean = np.mean(daily_ret)
        std = np.std(daily_ret)
        f.write('For position '+str(pos)+' mean is: '+str(mean)+' and std is: '+str(std) + '\n')
    f.flush()
    f.close()

if __name__ == '__main__':
    position = [1, 10, 100, 1000]
    num_trials = 10000
    simulate(position,num_trials)
    