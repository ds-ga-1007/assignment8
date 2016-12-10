import matplotlib.pyplot as plt
import numpy as np
from investment import investment

def figure_saver(position, daily_ret):
    """This function takes the position and the daily return list of a particular investment and builds          and saves the histogram of that particular investment"""
    file_marker = str(position)
    while len(file_marker) < 4:
         file_marker = "0" + file_marker
    fig = plt.figure(figsize=(14, 7))
    plt.hist(daily_ret,100,range=[-1,1])
    file_name = "histogram_" + file_marker + "_pos.pdf"
    plt.savefig(file_name)

    
def results_builder(daily_ret, curr_inv) :
    """This function takes in daily return list of a single position and extracts the mean and standard          deviation from it makes a result list to be appended to the to the overall results"""
    pos_ret = np.array(daily_ret)
    mean = pos_ret.mean()
    std = pos_ret.std()
    pos_res = "For {: d} positions of ${: f} the mean is {: f} and the standard deviation is {: f} at {: d} trials".format(curr_inv.position, curr_inv.position_value, mean, std, num_trials)
    results = []
    results.append(pos_res)
    results.append("\n")
    return results
    
    
    
def results_writer(results):
    """This function takes in a list with results and writes them into a file"""
    f = open("results.txt", 'w')
    f.writelines(results)
    
    
def trial_investments(positions, num_trials) :
    """This function takes in a list of positions and a number of trials to run and creates a pdf with a        histogram for each position and a results text file with the mean and standard deviation of each          position"""
    results = []
    
    #Here the program runs the trials for each positions
    for position in positions :
        curr_inv = investment(position)
        cumu_ret = [0] * num_trials
        daily_ret = [0] * num_trials
        for trial in range(num_trials) :
            cumu_ret[trial] = curr_inv.day_instance()
            daily_ret[trial] = (cumu_ret[trial]/1000) - 1
        
        # Here the program builds the histogram and the results
        figure_saver(position, daily_ret)
        result = results_builder(daily_ret, curr_inv)
        results.extend(result)
        
    results_writer(results)    
    
def position_list_builder():
    """This function asks the user for to build a list of positions piece by piece by asking for each            position one at a time and then asking them to type 'end' when they are finished. The user can            type 'quit' at any time to exit the program. Also the program will automatically exit if the user        ends without enter in a position"""
    not_end = True
    positions = []
    while not_end:
        input_string = input("Please enter an integer to add to the list of positions or type 'end' to end the list \n")
        if input_string == "end" :
            not_end = False
        elif input_string == "quit" :
            return input_string
        else:
            # Here the program check to see if the string the user entered can be turned into an integer
            try:
                position = int(input_string)
            except ValueError:
                print("You have entered a wrong value for a position")
                pass
            else:
                positions.append(position)
    else:
        if len(positions) > 0:
            return positions
        else :
            return "quit"
    
def get_num_trials():
    """this function asks the user for the number of trials they would like to run for each of the positions they have entered. The user can type 'quit' at any time to exit the program"""
    is_valid = False
    while not is_valid :
        input_string = input("Please enter the number of trials \n")
        
        if input_string == "quit":
            return input_string
        else :
            # Here the program check to see if the string the user entered can be turned into an integer
            try :
                num_trials = int(input_string)
            except ValueError:
                print("You have entered an improper value for the number of trials")
                pass
            else:
                is_valid = True
    else :
        return num_trials

# Here the program actually runs the above functions making sure to quit either when a keyboard interrupt 
# happens or when the user types quit
not_quit = True
while not_quit :
    try:
        num_trials = get_num_trials()
    except KeyboardInterrupt:
        num_trials = "quit"
        print("Exiting program")
        
    if num_trials == "quit" :
        break
    
    try:
        positions = position_list_builder()
    except KeyboardInterrupt:
        positions = "quit"
        print("Exiting program")
        
    if positions == "quit" :
        break
    
    try:
        trial_investments(positions, num_trials)
    except ValueError :
        print("One of the positions you have entered is invalid")
        pass
    except KeyboardInterrupt:
        print("Exiting program")
        not_quit = False
        pass
    else :
        not_quit = False
    
