import matplotlib.pyplot as plt
import sys
from investment import *
"""
Author : Wenjie Sun

Input a list and how many times you want the program to run.
If the any numbers in the list can not be divided by 1000, for example, 33, it will return an error.
If the input is not a list or integer, it will return an error

My code is designed as: 1) loop through every position 2) loop through every trail 3) within each trail, create a list
of all the results (eg. if we buy 100 share in parallel, then the list will record the result of buying 10 times.)
4) sum the value of the list in step 3 for calculations and append the calculations to a dict

For plotting the chart and writing the txt, just looping through the dict in each position.

This program roughly takes 5 minutes to run.
"""

# quit, input a list of positions, input num of trails:
while True:
    try:
        quit_input = input("Quit? If yes, type QUIT: ")
        if quit_input.upper() == str("QUIT"):
            break

        inv_list = eval(input("Please input a list: "))
        inv_trail = eval(input("How many times to try: "))
        try:
            type(inv_list) is list
        except:
            raise ValueError("The input is not a list")

        try:
            type(inv_trail) is int
        except:
            raise ValueError("The input is not an integer")

        # call the investment function
        inv = investment(inv_list, inv_trail)
        # return the dict from the function
        inv = inv.result()
        txt = open('results.txt', 'w')

        for inv_pos in inv:
            fig = plt.figure()
            plt.hist((list(inv[inv_pos].values())), 100, range=[-1, 1])
            mean = np.mean(list(inv[inv_pos].values()))
            std = np.sqrt(np.var(list(inv[inv_pos].values())))
            title = "The histogram of the result for buying " + str(inv_pos) + " share(s) in parallel"
            plt.title(title)
            plt.savefig('histogram_%04d_pos.pdf' % int(inv_pos))
            plt.show()
            txt.write("At the position of: " + str(inv_pos) + "\n")
            txt.write("The mean of daily return: " + str(mean) + "\n")
            txt.write("The standard deviation: " + str(std) + "\n")
            txt.write("\n")

        txt.close()
    except KeyboardInterrupt:
        sys.exit(0)
    except EOFError:
        sys.exit(0)
    except ValueError:
        print ("Unexpected errors")

