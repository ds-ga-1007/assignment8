'''
Created on Nov 23, 2016

@author: felix
'''
from simu_funcs import *
from simulation import *
import matplotlib.pyplot as plt
    
def main():
    while True:
        try:
            shares_input_str = ''
            trials_input_str = ''
            
            while not valid_share_str(shares_input_str):
                shares_input_str = input("Please enter a list of 4 integers separated by commas, as number of shares to buy in parallel\n")
                shares_input_str = rm_ws(shares_input_str)

            while not valid_trial_str(trials_input_str):
                trials_input_str = input("Please enter the number of simulation trials\n")
                trials_input_str = rm_ws(trials_input_str)

            positions = [int(string) for string in shares_input_str.split(",")]
            num_trials = int(trials_input_str)
            this_simu = simulation(positions,num_trials)
            
            this_simu.simulate() # Run the simulation
            
            cumu_ret = this_simu.simulate_results # Collect the simulated results
            #print(cumu_ret)#######################################
            
            daily_ret = (cumu_ret/1000) - 1
            #print(daily_ret)#################################
            
            for ii in np.arange(4):
                this_plot_data = daily_ret[:,ii]
                plt.hist(this_plot_data,100,range=[-1,1])
                plt.show()
            
            

            
            
            break
        except:
            pass

if __name__ == '__main__':
    try:
        main()
    except EOFError:
        pass