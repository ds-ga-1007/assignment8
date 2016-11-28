import numpy as np
import matplotlib.pyplot as plt


'''
all main function are in this class, including formating cleaning and calculation
'''
class investment:
    '''
    Constructor
    '''
    def __init__(self, positions, num_trails):
        self.positions = positions
        self.num_trails = num_trails
    
    '''
    convert the string that user input to a list of integer(for positions)
    and a single integer(for num_trails)
    '''
    def str2num(self, positions, num_trails):
        position_num=[]
        splited_positions = positions[1:-1].split(', ')
        for item in splited_positions:
            position_num.append(int(item))
        trails=int(num_trails)
        return position_num, trails
    
    '''
    Do calculation for one position, num_trails times, store the daily_return in a list
    '''
    def simulation_one(self, position, num_trails):
        cum_ret=[]
        daily_ret=[]
        for i in range(num_trails):
            position_value = 1000/position
            cum_ret_per = np.random.binomial(1, 0.51, position)*2*position_value                 
            cum_ret.append(sum(cum_ret_per))
            daily_ret.append(sum(cum_ret_per)/1000-1)
        return daily_ret
        
    '''
    Do calculation for all positions, store each daily_return in a dictionary
    '''
    def simulation(self, positions, num_trails):
        daily_ret_position={}
        for position in positions:
            daily_ret_position[position] = self.simulation_one(position, num_trails)
        return daily_ret_position
    
    '''
    plot the histogram and save them, write the statistics result to result.txt
    '''
    def plot_result(self,daily_ret_position):
        f = open('results.txt', 'w')
        for position in daily_ret_position.keys():
            plt.hist(daily_ret_position[position],100,range=[-1,1])
            plt.ylabel("frequency")
            plt.xlabel('daily_ret')
            plt.savefig("histogram_"+str(position).zfill(4)+"_pos.pdf")
            plt.close()
            all_simulation = np.asarray(daily_ret_position[position])
            ret_mean = np.mean(all_simulation)
            ret_std = np.std(all_simulation)
            f.write('Position: {0}\n'.format(position))
            f.write('mean: {0}'.format(ret_mean))
            f.write('   Std {0}\n\n'.format(ret_std))
        f.close()
