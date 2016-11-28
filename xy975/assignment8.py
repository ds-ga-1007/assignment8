'''
The main program of simulation.

To run this program, two arguments should be input: positions and num_trials.
positions is a list of some combination of 1, 10, 100, and 1000 which represents the 
position of an investment.
num_trials is an integer which represents how many times to randomly repeat the test.
This program will check if these inputs are valid.

When inputs are valid, for each position, the program will use class investment to 
simulate its return on investment (i.e. daily_ret) num_trials times.
It will also plot the histogram of simulation and calculate its mean and sd.

@author: Xinyan Yang
NetID: xy975
'''
import sys
import matplotlib.pyplot as plt
from tools.investment import *
from tools.exceptions import *

def simulation(positions, num_trials):
    """
    Simulate a list of positions in num_trials times.
    Then plot and write down the numerical results.
    """
    num_result = open('result.txt', 'w')
    for i in positions:
        sim = investment(i, num_trials).simulation()
        #  Plot and print the mean and sd of its daily
        plt.hist(sim,100,range=[-1,1])
        plt.title("position = " + str(i))
        plt.savefig("histogram_" + "{:04d}".format(i) + "_pos.pdf")
        plt.clf()
        num_result.write ("Numerical results when position = " + str(i) +"\n")
        num_result.write ("Mean value: " + str(np.mean(sim)) + "\n" )
        num_result.write ("standard deviation: " + str(np.std(sim)) + "\n" +"\n")
        print("Position = " + str(i) + " finished.")

def main():
    while True:
        input_p = input("positions (list) = ")
        if input_p  == 'quit':
            sys.exit(0)
        else:
            try:
                # If input positions valid
                input_p = input_p[1:-1].split(',')
                positions = [int(x) for x in input_p]
                positioins_valid(positions)
                
                input_nt = input("num_trials (integer) = ")
                if input_nt == 'quit':
                    sys.exit(0)
                else:
                    try:
                        # If input num_reials valid
                        num_trials = int(input_nt)
                        num_trials_valid(num_trials)
                        
                        # When all of the inputs are valid, simulate.
                        simulation(positions, num_trials) 
                        
                    # If the input is invalid, try another
                    except ValueError:
                        print('Invalid num_trials.')
                            
            
            # If the input is invalid, try another
            except ValueError:
                print('Invalid positions.')
                
    
if __name__ == "__main__":
    main()