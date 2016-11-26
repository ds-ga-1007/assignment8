import matplotlib.pyplot as plt
from statistics import mean, stdev
import numpy as np


class Investiment:
    
    def __init__(self, positions, num_trials):
        self.positions = positions
        #For each position, set a value to represents the size of each investment
        self.position_value = 1000 / positions
        self.num_trials = num_trials
    
    
    def outcome(investment):
        #Use NumPy's random number generating capability to simulate the outcome of one day of investment:
        cumu_ret = np.zeros(investment.num_trials)
        #Repeat num_trials times
        for trial in range(investment.num_trials):
            ret = 0
            for j in range(investment.positions):
                if np.random.uniform(0,1) <= 0.51:
                    ret += investment.position_value*2
                cumu_ret[trial] = ret
        return (cumu_ret/ 1000.0) - 1.0
    
    def invest(positions, num_trials):
        file = open('results.txt', 'w')
        for position in positions:
            #For each position, plot of the result of the trials in a histogram with X axis from -1.0 to +1.0, and Y axis as the number of trials with that result.
            investiment = Investiment(position, num_trials)
            daily_ret = investiment.outcome()
            
            fig = plt.figure()
            plt.hist(daily_ret, 100, range=[-1, 1])
            plt.title("histogram_" + str(position).rjust(4,'0') + "_pos")
            fig.savefig("histogram_" + str(position).rjust(4,'0') + '_pos.pdf')
            file.write("for position " + str(position) + " :" + "\r\n")
            file.write(" the mean or expected value of the daily return is: " + str(mean(daily_ret)) + "\r\n")
            file.write(" the standard deviation of the daily return is: " + str(stdev(daily_ret)) + "\r\n")
            file.flush()
        plt.show()
        plt.close('all')
        file.close()


if __name__ == "__main__":
    
    positions = [1, 10, 100, 1000]
    num_trials = 10000
    Investiment.invest(positions, num_trials)