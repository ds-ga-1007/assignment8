'''
Created on Nov 28, 2016

@author: Jingyi Su js5991
This model simulates investment with 51% of the time the return is 1.0 and 49% of the time the return is exactly -1.0. 
The investment instrument is purchased in $1, $10,$100,$1000 denomination and will be hold one day each time. 
'''

import numpy as np
import matplotlib.pyplot as plt

class investment:
        def __init__(self, positions, num_trials):
            '''
            constructor
            '''
            self.positions=positions
            self.num_trials=num_trials
            
            
        def investment_return(self, position):
            '''
            computes/simulates the daily returns 
            '''
            position_value=1000/position
            cumu_ret=np.zeros(self.num_trials)
            for trial in range(self.num_trials):    
                for pos in range(position):
                    simulator=np.random.uniform(0,1)
                    if simulator<0.51:
                        cumu_ret[trial]=cumu_ret[trial]+position_value*2
            
            daily_ret=cumu_ret/1000-1
            return daily_ret
        
        def histogram(self, daily_ret, position):
            '''
            save histogram
            '''
            fig=plt.figure()
            plt.hist(daily_ret, 100, range=[-1,1])
            plt.savefig('histogram_'+str(position).zfill(4)+'_pos.pdf')
            
        def simulation(self):
            '''
            perform the simulation and print results
            '''
            f=open('results.txt','w')
            for pos in self.positions:
                daily_ret=self.investment_return(pos)
                self.histogram(daily_ret, pos)
                f.write("Position "+str(pos)+'\n'+"the mean of daily return is "+ str(np.mean(daily_ret))+", the std of daily return is "+str(np.std(daily_ret))+"\n\n")
                f.flush()
            f.close()
            print ('Results are written in the result.txt and histograms are written in pdfs for each position')    
            
if __name__ == '__main__':
    positions=[1,10,100,1000]
    num_trials=10000
    investment(positions, num_trials).simulation()