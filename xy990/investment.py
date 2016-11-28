import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Author:xy990

#Define a class investment which includes initilization, how to simulate and the output of figures and txt.
class investment:
    #Initialization
    def __init__(self, positions, num_trials):
        self.positions = positions
        self.num_trials = num_trials
        
        
    #How to simulate    
    def simulate(self):
        position_values=[]
        for pos in self.positions:
            position_value =1000/pos
            position_values.append(position_value)
        
        daily_returns = []
        for p in position_values:
            cumu_ret = np.zeros(self.num_trials)
            
            for trial in range(self.num_trials):
                cumu_return =0
                for i in range(int(1000/p)):
                    
                    rand_num = np.random.rand()
                    if rand_num<=0.51:
                        cumu_return += p*2
                    else:
                        cumu_return = cumu_return
                cumu_ret[trial] = cumu_return
            daily_ret = (cumu_ret/1000) -1
            daily_returns.append(daily_ret)
        return daily_returns

    #Call the function simulate and get the results as figures and txt.
    def results(positions, num_trials):
        daily_return = investment.simulate(investment(positions, num_trials))
        file = open("output.txt", "w")
        for p in range(len(positions)):
            daily_ret = daily_return[p]
            plt.figure()
            plt.hist(daily_ret, 100, range =[-1,1])
            plt.xlabel("daily_return")
            plt.ylabel("number of trials")
            plt.savefig("histogram_%04d_pos.pdf" % positions[p])
            plt.close()
            
            
            
            file.write("At position" + str(positions[p])+ ", the mean of the daily return is"+ str(np.mean(daily_return[p]))+'\n')
            file.write("At position"+ str(positions[p]) + ", the standard deviation of the daily return is"+ str(np.std(daily_return[p]))+'\n' )
        file.close()
        print("Finished the task!")
            
            
            

            
