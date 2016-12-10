'''
Created on Nov 26, 2016

@author: Yovela
'''
from read_input import *
from simulation import *
import sys


if __name__ == '__main__':
    while True:
        
        answer = input("do you want to start a new simulation? yes or no\n")
        
        if answer == "no":
            print("end")
            sys.exit()
        if answer == "yes":
            try:
                user_input1 = input("Please input a list of the number of shares to buy in parallel as a string: e.g. [1, 10, 100, 1000]\n")
                if user_input1 == "quit":
                    sys.exit()
                else:
                    positions = read_position(user_input1)
                
            except ValueError:
                print ("Invalid Input, please note that all elements must be non-negative integers")
                continue

            except KeyboardInterrupt:
                sys.exit()     

            try:
                user_input2 = input("please input how many times you want to randomly repeat the test: e.g. 10000\n")
                if user_input1 == "quit":
                    sys.exit()
                else:                
                    num_trials = read_num_trials(user_input2)
            except ValueError:
                print ("Invalid Input, please note that all elements must be non-negative integers")
                continue

            except KeyboardInterrupt:
                sys.exit()             
            
            
            print("starting simulation")
            investment = trial(positions, num_trials)
            text_results(investment)
                
            

    
