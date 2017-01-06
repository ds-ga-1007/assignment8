"""
Date: Nov 28, 2016
Author: Chloe Meng(lm3226)
Description: This program simulates the expected daily return of investing
different denominations.
"""

import numpy as np
import matplotlib.pyplot as plt

class InvalidUserInputException(Exception):
    pass

class daily_investment_return:
    def __init__(self, denominations, num_trials):
        self.denominations = denominations
        self.num_trials = num_trials
        self.validate_denominations()
        self.validate_num_trials()

    def validate_denominations(self):
        for i in range (0, len(self.denominations)):
            if self.denominations[i] in [1,10,100,1000]:
                pass
            else:
                raise InvalidUserInputException("Invalid input.")

    def validate_num_trials(self):
        if self.num_trials > 0:
            pass
        else:
            raise InvalidUserInputException("Invalid input.")

    @staticmethod
    def number_denominations(denominations):
        return np.divide(1000, denominations)

    @staticmethod
    def single_purchase_return(denomination):
        #Daily return value for one single denomination purchase
        percentage = np.random.randint(1, 100)
        if percentage > 49:
            return denomination * 2
        else:
            return 0

    def portfolio_return(self):
        #Daily return value for given denominations purchase
        cumu_ret = np.zeros(len(self.denominations))
        num_denominations = self.number_denominations(self.denominations)
        for i in range(0, len(num_denominations)):
            for j in range(0, int(num_denominations[i])):
                cumu_ret[i] += self.single_purchase_return(self.denominations[i])
        return cumu_ret

    def run_trials(self):
        #Daily return value for given denominations purchase with multiple trials
        cumu_ret = [None] * self.num_trials
        daily_ret = [None] * self.num_trials
        for trial in range(0, self.num_trials):
            cumu_ret[trial] = self.portfolio_return()
            daily_ret[trial] = np.subtract(np.divide(cumu_ret[trial], 1000.0), 1)
        return np.transpose(daily_ret)

    def generate_results(self):
        #Generate histograms, and mean as well as standard deviation
        trials = self.run_trials()
        self.generate_histograms(trials)
        self.write_results_to_file(trials)

    def generate_histograms(self, trials):
        #Generate histograms for different positions with multiple trials
        for i in range(0, len(trials)):
            self.make_denomination_histogram(trials[i], self.denominations[i])

    def write_results_to_file(self, trials):
        #Write mean as well as standard deviation to a file and save it into txt
        f = open('results.txt', 'w')
        for i in range(0, len(self.denominations)):
            denomination = self.denominations[i]
            mean = self.mean_daily_ret(trials[i])
            std = self.std_daily_ret(trials[i])
            f.write(
"""Mean expected return for {0}: {1}
Standard deviation for {0}: {2}\n""".format(denomination, mean, std)
            )
        f.close()

    @staticmethod
    #Calculate mean
    def mean_daily_ret(daily_ret):
        daily_ret = np.array(daily_ret)
        return daily_ret.mean()

    @staticmethod
    #Calculate standard deviation
    def std_daily_ret(daily_ret):
        daily_ret = np.array(daily_ret)
        return daily_ret.std()

    @staticmethod
    def make_denomination_histogram(daily_ret, denomination):
        #Generate one histogram for each position and save it as pdf
        n,bins,patches = plt.hist(daily_ret, 100, range=[-1,1])
        plt.xlabel('$' + str(denomination) + ' denomination')
        plt.ylabel('Number of Trials')
        plt.title('Histogram of the result for ' + str(int(1000 / denomination)) + ' positions of $' + str(denomination))
        plt.grid(False)
        plt.savefig('histogram_' + '{0:04d}'.format(denomination) + '_pos.pdf')
        plt.show()
