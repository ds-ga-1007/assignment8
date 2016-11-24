#!/usr/bin/env python3

from investment.positions import InvestmentPositions
import matplotlib.pyplot as plt
import statistics as stats

'''
Sources consulted
http://matplotlib.org/1.2.1/examples/pylab_examples/histogram_demo.html

'''

def prompt_positions():
    while True:
        try:
            userinput = input("Enter the positions as a list. ")
            return InvestmentPositions.parse_positions(userinput)
        
        except ValueError as e:
            print("Invalid positions, try again.", e)

def prompt_trials():
    while True:
        try:
            num_trials = int(input("Enter the number of simulations. "))
            
            if num_trials > 0:
                return num_trials
            
            else:
                raise ValueError("No negative numbers pls")
    
        except ValueError:
            print("Invalid number, try again.")
        
def calculate_daily_ret(cumu_ret):
    return [ret / 1000 - 1 for ret in cumu_ret]

def calculate_daily_stats(daily_ret):
    return {
        "mean": stats.mean(daily_ret), 
        "standard deviation": stats.pstdev(daily_ret)
        }


# Runs the program in the terminal
if __name__ == "__main__":
    positions = prompt_positions()
    num_trials = prompt_trials()

    results = [investment.n_days_return(num_trials) for investment in positions]

    daily_ret = [calculate_daily_ret(result) for result in results]

    stats = [calculate_daily_stats(ret) for ret in daily_ret]

    # Write measures of central tendency to file
    with open("results.txt", "w") as file:
        for (position, stat) in zip(positions, stats):
            file.write("{}: {}\n".format(position, stat))

    # Plot and save histogram for each simulation
    for (position, ret) in zip(positions, daily_ret):
        n, _, _ = plt.hist(ret, 100, range = [-1, 1])
        graphnum = str(int(position.value)).zfill(4)
    
        plt.axis([-1, 1, 0, max(n) * 1.1]) # set graph axes to fit data
        plt.xlabel("Rate of Return")
        plt.ylabel("Frequency")
        plt.title("Simulation Results for ${} Instrument".format(position.value))

        plt.savefig("histogram_{}_pos.pdf".format(graphnum))
        plt.close()
        
        