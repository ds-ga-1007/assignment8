'''

@author: jonathanatoy
'''
import numpy as np
import matplotlib.pyplot as plt
import investment

def main():
    '''
    Main program designed to simulate $1000 spread amongst 1, 20, 100, or 1000 positions.
    For each position size the investment is simulated for 1 day of trading for 10000 trials.
    The histogram, mean and standard deviations for the percentage returns for the trials 
    associated with each position are output as files.
    '''
    
    positions = [1, 10, 100, 1000]
    num_trials = 10000
    
    my_investment = investment.investment(positions, num_trials)
    
    my_returns = my_investment.multi_day_gamble()
    file_labels = ['0001', '0010', '0100', '1000']
    
    for i in range(4):
        my_fig = plt.figure()
        plt.hist(my_returns[:,i], 100, range = [-1,1])
        plt.xlabel('Daily Return')
        plt.ylabel('Number of instances')
        plt.title('Daily returns for investsments of size ' + str(my_investment.position_value[i]))
        plt.savefig('histogram_' + file_labels[i] + '_pos.pdf')
    
    results = np.array([my_investment.positions, np.mean(my_returns, axis=0), np.std(my_returns, axis=0)])
    
    fout = open('results.txt', "w")

    fout.write('    Position Size     Mean Return      Std Return \n')
    fout.write(str(results.T))
    
if __name__ == '__main__':
    main()