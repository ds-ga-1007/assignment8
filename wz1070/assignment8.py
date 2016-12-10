import numpy as np
import MyException
import matplotlib.pyplot as plt

#check for the validness of the list of positions
def check_pos_list(position_list):
    potential_pos = [1, 10, 100, 1000]
    for item in position_list:
        if not item in potential_pos:
            raise MyException()
            break

#getting input positions from user and handle exceptions
def get_positions(positions_string):
    try:
        positions = [int(x, 10) for x in positions_string[1: len(positions_string) - 1].split(', ')]
    except ValueError:
        print('Input list of the number of shares to buy should be the form: [1, 10, 100, 1000]')
    check_pos_list(positions)
    return positions

#getting input num_trials from user and handle exceptions
def get_num_trials(num_trials_string):
    try:
        num_trials = int(num_trials_string)
    except ValueError:
        print('number of times to randomly repeat the test should be a integer')
    return num_trials

#do the simulation num_trials times and generate 5 requested files
positions = get_positions(input('list of the number of shares to buy'))
num_trials = get_num_trials(input('number of times to randomly repeat the test'))
means = np.zeros(len(positions))
sd = np.zeros(len(positions))
for i in range(len(positions)):
    position_value = 1000 / positions[i]
    cumu_ret = np.zeros(num_trials)
    for j in range(num_trials):
        draw = np.random.randint(1, 101)
        if draw <= 49:
            cumu_ret[j] = 0
        else:
            cumu_ret[j] = 2 * position_value
    daily_ret = cumu_ret / 1000 - 1
    means[i] = np.mean(daily_ret)
    sd[i] = np.std(daily_ret)
    np.savetxt('results.txt', (means, sd), header = 'Means and Standard Devaition of daily_ret of position' + str(positions))
    plt.hist(daily_ret, 100, range=[-1, 1])
    plt.savefig('histogram_%04d_pos.pdf' % positions[i])