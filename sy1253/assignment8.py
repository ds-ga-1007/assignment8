'''
Created on Nov 27, 2016

@author: kevinyan


credit the author of lj1035
take reference from lj1035 about how to how to handle the exceptions of the inputing positons list
Specifically, the "positions_to_list" function and user defined exceptions in 


This is the main program of the assignment, it asks the user for the positions they want to test 
in list and the number of trials they would like to perform. The program would generate text file and 
histograms for the return of each postion.
'''
import myexception
from simulation import simulation
import sys


def main():   
    while True:
        try:
            print('type "quit" to quit the program')
            shares = raw_input("a list of the number of shares to buy in parallel:e.g.[1, 10, 100, 1000]: ")           
            if shares == 'quit':
                sys.exit(0)
            
            positions = positions_to_list(shares)
            break
            
            
        except EOFError:
                sys.exit(0)

        except KeyboardInterrupt:
                sys.exit(0)     
                
    while True:            
        try:        
            trial = raw_input('number of trials? ')
            if trial == 'quit':
                sys.exit(0)
            
            num_trial = inputTrial_to_validTrial(trial)
            break
                
            
        except EOFError:
            sys.exit(0)
   
        except KeyboardInterrupt:
            sys.exit(0)
        
    f = open('results.txt', 'w')
    for i in positions:
        result = simulation(i, num_trial)
        result.present_result()
        f.write('position: ' + str(i) + ', mean = ' + str(result.get_mean()) + ', std = ' + str(result.get_std()) + "\r\n")    
    f.close()

def positions_to_list(position_input):
    """
    this function checks if the position list entered in valid
    credit lj1035 for reference
    """ 
    if position_input[1] != '[' and position_input[-1] != ']':
        raise myexception.FormatError()
    modifiedInput = position_input[1:-1].replace(" ", "")
    try:
        cleaned_input_list = modifiedInput.split(',')
    except:
        raise myexception.FormatError()
    positions = []
    for position in cleaned_input_list:
        if int(position) <= 0:
            raise myexception.invalidPositionError()
        positions.append(int(position))
    return positions
            
            
def inputTrial_to_validTrial(trial):
    """
    this function checks if the number of tries entered is valid
    """ 
    num_trials = int(trial)
    if num_trials > 0:       
        return num_trials
    else:
        raise ValueError("Invalid input. Please input a positive integer.")
   
             
if __name__ == '__main__':
    main()
