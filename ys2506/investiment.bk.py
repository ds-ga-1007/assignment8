import matplotlib.pyplot as plt
from statistics import mean, stdev
import numpy as np


class Investiment:
    def __init__(self, positions, num_trials):
        self.positions = positions
        # For each position, set a value to represents the size of each investment
        self.position_value = 1000 / positions
        self.num_trials = num_trials
    
    def outcome(self):
        # Use NumPy's random number generating capability to simulate the outcome of one day of investment:
        cumu_ret = np.zeros(self.num_trials)
        # Repeat num_trials times
        for trial in range(self.num_trials):
            ret = 0
            for j in range(self.positions):
                if np.random.uniform(0, 1) <= 0.51:
                    ret += self.position_value * 2
                cumu_ret[trial] = ret
        return (cumu_ret / 1000.0) - 1.0
    
    def writeResults(self):
        file = open('results.txt', 'w')
        for position in positions:
            # For each position, plot of the result of the trials in a histogram with X axis from -1.0 to +1.0, and Y axis as the number of trials with that result.
            daily_ret = self.outcome()
            file.write("for position " + str(self.position) + " :" + "\r\n")
            file.write(" the mean or expected value of the daily return is: " + str(mean(daily_ret)) + "\r\n")
            file.write(" the standard deviation of the daily return is: " + str(stdev(daily_ret)) + "\r\n")
            file.flush()
        file.close()
    
    def writePDFs(self):
        for position in self.positions:
            # For each position, plot of the result of the trials in a histogram with X axis from -1.0 to +1.0, and Y axis as the number of trials with that result.
            daily_ret = self.outcome()
            fig = plt.figure()
            plt.hist(daily_ret, 100, range=[-1, 1])
            plt.title("histogram_" + str(position).rjust(4, '0') + "_pos")
            fig.savefig("histogram_" + str(position).rjust(4, '0') + '_pos.pdf')
        plt.show()
        plt.close('all')

    def invest(self):
                #compute the daily_ret and output results to result.txt and create pdfs
        self.writeResults()
        self.writePDFs()




if __name__ == "__main__":
    positions = [1, 10, 100, 1000]
    num_trials = 10000
    investiment = Investiment(positions, num_trials)
    investiment.invest()