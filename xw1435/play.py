from investment import investment
import numpy as np
import matplotlib.pyplot as plt
import sys


def get_position():
    position_list =[]
    valid_input = False
    while valid_input == False:
        user_position_input = input("Please input a list of positions you want to use, separate by space\n")
        if user_position_input == "quit":
            return user_position_input
            sys.exit() 
        else:
            try: position_list = [int(s) for s in user_position_input.split(" ")]   
            except ValueError:
                print ("Invalid input! Please try again with a list of integer numbers!\n")
                pass
            else:
                valid_input = True
    return position_list

def get_trials():    
    valid_input = False
    trials = 0
    while valid_input == False:
        user_input = input("How many trials do you want to simulate?\n")
        if user_input == "quit":
            return user_input
            sys.exit()
        else:
            try: trials = int(user_input)
            except ValueError:
                print ("Invalid input! Please try again with an integer number!\n")
                pass
            else:
                valid_input = True    
    return trials

def save_plot(position,daily_ret):
    digit = len(str(position))
    if digit == 1:
        file_name = "000" + str(position)
    elif digit == 2:
        file_name = "00" + str(position) 
    elif digit == 3:
        file_name = "0" + str(position) 
    else:           
        file_name = str(position)
    fig = plt.figure(figsize=(14, 7))
    plt.hist(daily_ret,100,range=[-1,1])
    file_name = "histogram_" + file_name + "_pos.pdf"
    plt.savefig(file_name)



terminate = False

while terminate == False:
    num_trials = get_trials()
    position_list = get_position()
    
    if num_trials == "quit":
        terminate = True
        
    elif position_list =="quit":
        terminate = True
        
    else:    
        for position in position_list:
                daily_ret = [0]*num_trials
                cumu_ret = [0]*num_trials
            
                curr_investment = investment(position)
            
                for trial in range(num_trials):
                    cumu_ret[trial] = curr_investment.one_day_outcome()
                    daily_ret[trial] = (cumu_ret[trial]/1000) - 1
            
                mean = np.mean(daily_ret)
                std = np.std(daily_ret)
                result = "For Position " + str(position) + ", the mean is " + str(mean) + ", the standard deviation is " + str(std) + "\n"
            
                f = open('result.txt', 'a')
                f.writelines(result)
                save_plot(position,daily_ret)     
                
