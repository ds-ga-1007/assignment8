'''
Created on Nov 26, 2016
@author: Fanglin Chen
@Reference: assignment questions

Suppose that the user has $1000 to invest in an investment instrument with the following properties:  
a. The user can purchase it in $1, $10, $100, and $1000 denominations.
b. Holding time is one day.
c. 51% of the time the return is exactly 1.0 (the value doubles).
d. 49% of the time the return is exactly -1.0 (all value is lost).              

This program obtains the following inputs from the user:
a. positions: a list of the number of shares to buy in parallel, e.g. [1, 10, 100, 1000]
b. num_trials: an integer of the number of times to randomly repeat the test, e.g. 10000
And it presents the histograms, mean and standard deviation of the daily returns to the user.
'''

from daily_ret import *
from exception import *

def main():
    while True:
        try:
            # Obtain the inputs from the user
            positions = input('Please enter a list of the number of shares to buy in parallel:\n> ')
            if positions =='quit':
                break
            num_trials = input('Please enter an integer of the number of times to randomly repeat the test:\n> ')
            if num_trials =='quit':
                break
        
            # Check whether the inputs are valid
            positions = eval(positions)
            num_trials = eval(num_trials)
            if type(positions) != list or type(num_trials) != int or num_trials <= 0:
                raise InputError()
            if not all([position in [1, 10, 100, 1000] for position in positions]):
                raise InputError()
        
            # Summarize the statistics (mean and standard deviation) of the daily returns
            summary_stats = pd.DataFrame()
            for position in positions:
                ret_stats = pd.DataFrame([result(position, num_trials)], columns=['position', 'mean', 'standard deviation']) 
                summary_stats = summary_stats.append(ret_stats, ignore_index=True)
        
            # Write the statistics above into the file "results.txt"
            with open('results.txt', 'w') as f:
                f.write(str(summary_stats))
            break
    
        except (InputError, NameError, SyntaxError):
            print('Invalid input')
        except EOFError:
            print('This is the end of file')
        except KeyboardInterrupt:
            print('You have hit the interrupt key')
    

if __name__ == '__main__':
    main()