'''
Created on Nov 26, 2016

@author: Akash
'''
import random
import os.path
import re
import numpy as np
import matplotlib.pyplot as plt

class investmnt:
    valid_input = 1   # flag value to check whether input is valid or not
    def check_valid_position_list(self, list_of_positions, to_print_or_not): # the second argument (to_print_or_not) is to print the error message only when the function is called. It is not printed when it is run for test cases
        self.valid_input = 1
        positions_list = list(map(int, re.findall("[-\d]+", list_of_positions)))
        try:
            if positions_list.count(1)==0 or positions_list.count(10)==0 or positions_list.count(100)==0 or positions_list.count(1000)==0: # to check that positions list contains all the denominations
                self.valid_input = 0          
                raise ValueError  
            elif (re.search('[a-zA-Z_*#%&^@:></\{}?~!-]+', list_of_positions)== None) == False: # to check whether the input doesnt have special characters
                self.valid_input = 0          
                raise ValueError
            elif (list_of_positions.count('[') != 1) or (list_of_positions.count(']') != 1): # to check that the input has opening list sign and closing list sign.
                self.valid_input = 0          
                raise ValueError
        except ValueError:
            if to_print_or_not == 1:
                print("Invalid position list values! Read the instructions carefully!")
                
    def check_valid_num_trials(self, num_trials, to_print_or_not): # the second argument (to_print_or_not) is to print the error message only when the function is called. It is not printed when it is run for test cases
        self.valid_input = 1
        try:
            num_trials = int(num_trials)
            try:
                if num_trials <= 0:  # to check that the number of trials is not 0 or negative
                    self.valid_input = 0          
                    raise ValueError
            except ValueError:
                if to_print_or_not == 1:
                    print("Invalid number of trials! It should be an integer > 0")   
        except ValueError:
            self.valid_input = 0
            if to_print_or_not == 1:
                print("That's not an integer!")
        
    def simulate(self, list_of_positions, num_trials):
        file = open('results.txt', 'w')
        num_trials = int(num_trials)
        list_of_positions = list(map(int, re.findall("[-\d]+", list_of_positions)))
        try:  # the try-catch is because we don't want continue the simulation for incorrect input values. 
            if self.valid_input == 0:
                raise ValueError
            else:
                for i in range(len(list_of_positions)):
                    position_value = 1000/list_of_positions[i]
                    list_of_day_values = []
                    for j in range(num_trials):
                        list_of_day_values.append((self.cumu_res(position_value)/1000) - 1)
                    s1 = '{0}{1}{2}{3}{4}{5}{6}'.format('The mean of the daily return of trail ',i+1 ,' with position value ',str(position_value),' is ', str(self.average(list_of_day_values)), '\n')
                    s2 = '{0}{1}{2}{3}{4}{5}{6}'.format('The standard deviation of the daily return of trail ',i+1, ' with position value ',str(position_value),' is ', str(self.standard_deviation(list_of_day_values)), '\n')
                    file.write(s1)
                    file.write(s2+'\n')  # write function writes the values in results.txt
                    f = plt.figure()
                    plt.hist(list_of_day_values,100,range=[-1,1])
                    if position_value == 1000:  #this if-else block is to assign appropriate name to position value simulation graph
                        n = '1000'
                    elif position_value == 100:
                        n = '0100'
                    elif position_value == 10:
                        n = '0010'
                    else:
                        n = '0001'
                    name = '{0}{1}{2}'.format('histogram_',n,'_pos.pdf')
                    if os.path.exists(name):
                        print("Note: The file ",name,"already exists and it is being overwritten by another simulation graph with the same position value :", position_value)
                        # the above print statement is useful when we have two simulations of same position value. Ex: [1,10,10,100,1000] <--here 10 position of $100 occurs twice.
                    f.savefig(name)
                file.close()
        except ValueError:
            print("Inputs are incorrectly defined!")
        
    def standard_deviation(self, x):
        return np.std(x)
        
    def average(self, x):
        return np.mean(x)
            
    def cumu_res(self, position_value):  # this function generates the total value retained after a particular trial
        no_of_shares = 1000/position_value
        list_of_outcomes = []
        for i in range(int(no_of_shares)):
            rand = random.randint(1, 100) # generates a uniform random number between 1 and 100 
            if rand <= 51:   # this makes sure that probability of winning is 51%
                list_of_outcomes.append(position_value*2)
            else:
                list_of_outcomes.append(0)
                
        return sum(list_of_outcomes)
            
            

     
