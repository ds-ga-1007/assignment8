
# coding: utf-8

# In[ ]:

from investment import *

def main():
    """Author: Li Lin Qin
    main program to run by user, input 'quit' to quit program
    
    When input an investment instrument, 
    this program will run a simulation to determine 
    how to make that investment on the first day.
    Program outputs a text file with mean and std of each input position
    as well as histograms in pdf format"""
    
    while True:
        try:
            lists = input("Enter a list of the number of shares to buy: ")
            if lists.lower() == 'quit':
                return
            if lists[-1] != "]" or lists[0] != "[":
                raise ValueError
            lists = lists.strip()
            sep = lists[1:-1].split(",")
            positions = [int(s) for s in sep]
            break
        except ValueError:
            print("Invalid list of positions. Please input a list of positive integers. ")
        except KeyboardInterrupt:
            return
            
    while True:
        try:
            num_trials = input("How many times to repeat the test? ")
            if num_trials.lower() == 'quit':
                return
            num_trials = int(num_trials)
            if num_trials <= 0:
                raise ValueError
            investment.output(positions, num_trials)
            breaks
        except ValueError:
            print("Invalid number of trials. Please input a positive integer. ")
        except KeyboardInterrupt:
            return
            
if __name__ == "__main__":
    main()

