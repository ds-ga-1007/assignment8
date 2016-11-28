import sys
import numpy 
from simulation import *
'''This is the main script
   Author:Liwei Song
   NetID:ls4408
   Creation date: 11/28/2016
   This script prompts user to enter a list of positions and number of simulations. Then it will plot histograms of different positions and generate a txt file for summaries.
'''

if __name__=='__main__':
    print('You only have $1000, and you could only purchase a list of \n position sizes of 1,10,100 and 1000 in form of []')
    #prompt user to enter a list of different positions
    position_list=[1,10,100,1000]
    while(True):
        try:
            input_str=input("Enter a list of position,and enter quit to exit: ")
            if input_str=='quit':
                sys.exit()
            positions=correct_input_position(input_str)
            break
        except inputError:
            print("Incorrect input! Please reenter a valid list of positions!")
        except KeyboardInterrupt:
            sys.exit()
        except EOFError:
            sys.exit()
        #handle exceptions for input of list of positions.

    while(True):    
        try:
            numb_str=input("Enter a valid number for simulation, and enter quit to exit: ")
            #prompt users to enter a valid number for simulations
            if numb_str=='quit':
                sys.exit()
            num_trials=correct_input_numb(numb_str)
            break
        except inputError:
            print("Incorrect input! Please reenter a valid number for simulation!")
        except KeyboardInterrupt:
            sys.exit()
        except EOFError:
            sys.exit()
        #handle exceptions for invalid input of number of simulations
    print('reults.txt and histograms for different positions are being generated')
    stimulation_initial=simulation(positions,num_trials)
    #generate simulations
    stimulation_initial.get_simulation()
    #generate histograms and txt
    stimulation_initial.get_txt_hist()