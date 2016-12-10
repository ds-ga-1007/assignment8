"""
Created on Fri Nov 25 2016

@author: jinubak/jub205
@desc: Program takes positions list and number of simulations from the
	   user and simulates one day investment with 51% chance of winning.
	   It computes average daily return and cumulative return from the
	   simulation and plots histograms for each position in the position
	   list. It saves the result in a text file and plots in pdf files.
"""
import sys
import investmentsimulator as isim

def runSimulation():
    
    positions = input("Enter a list of number of shares to buy in parallel: e.g. [1,10,100,1000]: ")
    formatted_pos = isim.format_position_input(positions)
    
    num_trials = input("How many times do you want to randomly repeat the simulation? ")
    formatted_num_trials = isim.format_num_trials(num_trials)
        
    with open("results.txt", "w") as f:
        f.write("%-8s|%-10s|%-10s\n" %("POSITION","MEAN","STD DEV"))
        for position in formatted_pos:
            portfolio = isim.InvestmentPortfolio(position, formatted_num_trials)
            portfolio.InvestmentSimulation()
            portfolio.compute_mean()
            portfolio.compute_std_dev()
            isim.plot_hist(portfolio.daily_ret, portfolio.position)
            f.write("%-8s|%-10s|%-10s\n" %(str(portfolio.position), str(portfolio.mean), str(portfolio.std_dev)))
            
if __name__ == '__main__':

	try:
		runSimulation()

	except KeyboardInterrupt:

		print("Keyboard Interrupt from User!")
		sys.exit("Exit the program!")
