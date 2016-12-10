import sys
from investment import *

'''
Created on Nov 28, 2016

@author: sunyifu
'''



def main():
    while True:
        try:
            positions_input = input("Please enter a list of number of shares to buy in parallel:")
            
            if positions_input == 'quit':
                sys.exit()
## check input                
            if positions_input == '':
                raise ValueError("invalid input")
            
            if positions_input[0] != '[' or positions_input[-1] != ']':   
                raise ValueError('input need be a list')  
             
            else:
                positions = positions_input[1:-1].split(',')
                for i, item in enumerate(positions):
                    positions[i] = int(item)
                break    
            
            
        except KeyboardInterrupt:
                sys.exit()
        except EOFError:
                sys.exit()
    
    while True:
        try:
            num_trials_input = input('Please input a number of trials you want or enter quit to end:\n')
            
            if  num_trials_input == 'quit':
                sys.exit()
##check input                
            if num_trials_input == "" :
                raise ValueError('invalid input')  
            
            num_trials = int(num_trials_input)  
            if num_trials <= 0:
                raise ValueError('Please enter a positive integer')
            
            break
        
        except KeyboardInterrupt:
                sys.exit()
        except EOFError:
                sys.exit()
    
    
    for pos in positions: 
        inves = investment(pos,num_trials)
        inves.output_histogram()
        inves.print_result()  
        
                  
if __name__ == '__main__':
    main()