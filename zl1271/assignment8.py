'''
Created on Nov 23, 2016

@author: felix
'''
from simu_funcs import *
from simulation import *
from plot_funcs import *
    
def main():
    while True:
        try:
            shares_input_str = ''
            trials_input_str = ''
            
            while not valid_share_str(shares_input_str):
                shares_input_str = input("Please enter a list of 4 integers separated by commas as number of shares to buy in parallel\n")
                shares_input_str = rm_ws(shares_input_str)

            while not valid_trial_str(trials_input_str):
                trials_input_str = input("Please enter the number of simulation trials\n")
                trials_input_str = rm_ws(trials_input_str)

            positions = [int(string) for string in shares_input_str.split(",")]
            num_trials = int(trials_input_str)
            this_simu = simulation(positions,num_trials)
            
            this_simu.simulate() # Run the simulation
            
            cumu_ret = this_simu.simulate_results # Collect the simulated results

            
            daily_ret = (cumu_ret/1000) - 1

            result_file = open('results.txt', 'w')
            for ii in np.arange(len(positions)):
                this_plot_data = daily_ret[:,ii]
                this_position_int = positions[ii]
        
                plot_simulation(this_plot_data, this_position_int) 
                
                this_mean = np.mean(this_plot_data)
                this_std = np.std(this_plot_data)
                
                write_simulation(result_file, this_position_int, this_mean, this_std)

            result_file.close()
            print('results.txt saved.')

            break
            
        except:
            pass
    exit('Program finished.')
if __name__ == '__main__':
    try:
        main()
    except EOFError:
        pass