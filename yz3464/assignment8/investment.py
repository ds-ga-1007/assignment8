'''
Created on Nov 26, 2016

@author: twff
'''
import numpy as np
import matplotlib.pyplot as plt

class investment:
    def _init_(self, num_trials, positions):
        self.positions = positions#a list of the number of shares to buy in parallel:
        self.num_trials = num_trials#how many times to randomly repeat the test
        
    @staticmethod
    def simulateInvestment(investment):
        '''
        simulate the investment and return the outcome of one day
        '''
        trial_num = investment.num_trials
        positions_num = investment.positions
        value = 1000 / positions_num #even value
        cumu_ret = np.zeros(trial_num) #total income of one day
        daily_ret = np.zeros(trial_num)#the result of each day
        
        for trial in range(trial_num):
            temp = 0
            for pos in range(positions_num):
                rand = np.random.uniform(0,1)
                if rand <= 0.51:
                    temp = temp + value*2
                else:
                    temp = temp + 0
                cumu_ret[trial] = temp
            daily_ret[trial] = (cumu_ret[trial]/1000) - 1
        return daily_ret
    
    
    @staticmethod
    def plotFigures(position, num_trials,filename):
        '''
        plot the histgram of daily outcome of each trial and save it to the filename inputed
        '''
        daily_ret = investment.simulateInvestment(investment(position,num_trials))
        fig, ax = plt.subplots(nrows=1, ncols=1)
        fig.set_size_inches(12, 12)
        ax.hist(daily_ret, 100, range=[-1, 1])
        plt.title('histogram ' + str(position))
        fig.savefig(filename)
        plt.close(fig)
        
    @staticmethod    
    def showResult(positions, num_trials):
        '''
        return result.txt, which includes the numerical results.
        '''
        f = open('result.txt', 'w')
        for p in positions:
            daily_ret = investment.simulateInvestment(investment(p,num_trials))
            mean = str(np.mean(daily_ret))
            std = str(np.std(daily_ret))
            file.write("position " + str(p) + ", mean: " + mean + ", std:  " + str + "\r\n")
            f.flush()
        f.close()
        
            
            
            
            
        
        