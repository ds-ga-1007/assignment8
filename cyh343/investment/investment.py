import numpy as np
import matplotlib.pyplot as plt

class investment:
    
    def __init__(self, positions, num_trials):
        
        """ class inputs constructor """
        
        self.positions = positions
        self.num_trials = num_trials
        
    def stimulate(self, position_values, num_trials):
        
        """
        Function stimulate repeat num_trials times simulation for each value
        in position_values and return and save the result as a list called 
        daily_ret
        
        parameters:
            position_values:    a list of value that represent the size of each
                                investment
            num_trials:    int
            
        return:
            result:    dictionary with a list of positions as keys and a list 
                       of daily_ret as values
        """
        
        result = {}
        for p in position_values:
            cumu_ret = np.zeros(num_trials)
            daily_ret = np.zeros(num_trials)
            
            for trial in range(self.num_trials):
                cumu_num = 0
                
                for i in range(int(1000/p)):
                    random_num = np.random.rand()
                    
                    if (0 <= random_num <= 0.51):
                        cumu_num = cumu_num + 2 * p
                    elif (1 > random_num > 0.51):
                        cumu_num = cumu_num
                        
                cumu_ret[trial] = cumu_num
                daily_ret[trial] = cumu_ret[trial]/1000 - 1
                
            result[int(1000/p)] = daily_ret
        
        return result
    
    def present_results(self, positions, num_trials):
        
        """
        Function present_results 
        1) call the function 'stimulate' to get a dictionary with list of daily_ret
           as values
        2) plot the histogram of the result and create file 'result.txt' with basic
           statistics info.
           
        parameters:
            positions:    list of int
            num_trials:    int
            
        returns:        
            create some histogram and a 'result.txt' file
           
        """ 
         
        position_values = [1000 / p for p in positions]
        result = self.stimulate(position_values, num_trials)
        
        d = open('results.txt', 'w')
        
        for p in positions:
            plt.hist(result[p], 100, range = [-1.0, 1.0])
            plt.ylabel('Number of trials with corresponding results')
            plt.xlabel('daily_ret')    
            
            if p == 1:
                plt.savefig('histogram_0001_pos.pdf')
            elif p == 10:
                plt.savefig('histogram_0010_pos.pdf')
            elif p == 100:
                plt.savefig('histogram_0100_pos.pdf')
            elif p == 1000:
                plt.savefig('histogram_1000_pos.pdf')
            plt.close()
            
            ret = np.asarray(result[p])
            ret_mean = np.mean(ret)
            ret_std = np.std(ret)
            d.write('The mean of daily return for position {0} is {1}\n'.format(p, ret_mean))
            d.write('The standard deviation of daily return for position {0} is {1}\n'.format(p, ret_std))                                                        
            
        d.close()    