import matplotlib.pyplot as plt
import numpy as np
from investment import investment

def figure_saver(position, daily_ret):
    
    file_marker = str(position)
    while len(file_marker) < 4:
         file_marker = "0" + file_marker
    fig = plt.figure(figsize=(14, 7))
    plt.hist(daily_ret,100,range=[-1,1])
    file_name = "histogram_" + file_marker + "_pos.pdf"
    plt.savefig(file_name)

def results_writer(results):
    f = open("results.txt", 'w')
    f.writelines(results)
    
    
def trial_investments(positions, num_trials) :
    results = []
    for position in positions :
        curr_inv = investment(position)
        cumu_ret = [0] * num_trials
        daily_ret = [0] * num_trials
        for trial in range(num_trials) :
            cumu_ret[trial] = curr_inv.day_instance()
            daily_ret[trial] = (cumu_ret[trial]/1000) - 1
        
        figure_saver(position, daily_ret)
        pos_ret = np.array(daily_ret)
        mean = pos_ret.mean()
        std = pos_ret.std()
        pos_res = "For {: d} positions of ${: f} the mean is {: f} and the standard deviation is {: f} at {: d} trials".format(curr_inv.position, curr_inv.position_value, mean, std, num_trials)
        results.append(pos_res)
        results.append("\n")
    results_writer(results)    
    
def position_list_builder():
    not_end = True
    positions = []
    while not_end:
        input_string = input("Please enter an integer to add to the list of positions or type 'end' to end the list \n")
        if input_string == "end" :
            not_end = False
        elif input_string == "quit" :
            return input_string
        else:
            try:
                position = int(input_string)
            except ValueError:
                print("You have entered a wrong value for a position")
                pass
            else:
                positions.append(position)
    else:
        return positions
    
def get_num_trials():
    is_valid = False
    while not is_valid :
        input_string = input("Please enter the number of trials \n")
        
        if input_string == "quit":
            return input_string
        else :
            try :
                num_trials = int(input_string)
            except ValueError:
                print("You have entered an improper value for the number of trials")
                pass
            else:
                is_valid = True
    else :
        return num_trials
    
not_quit = True
while not_quit :
    num_trials = get_num_trials()
    if num_trials == "quit" :
        break
    
    positions = position_list_builder()
    if positions == "quit" :
        break
    
    try:
        trial_investments(positions, num_trials)
    except ValueError :
        pass
    else :
        not_quit = False
    
