import numpy as np
import matplotlib.pyplot as plt

class invest:
    # class investment used to check the earnings for different positions
    # the class will output the mean and std of daily return for different given position
    def __init__(self, positions, num_trials):
        # remember the positions and total trial numbers
        self.positions = positions
        self.num_trials = num_trials

    def invest_sub(self):
        result = open('results.txt', 'w')
        d=len(self.positions);
        for time in range(d):
            # try the time-th position
            position=self.positions[time];
            position_value = 1000 / position;
            cumu_ret = np.zeros(self.num_trials);
            daily_ret = np.zeros(self.num_trials);
            for trial_time in range(self.num_trials):
                # the process is repeated for num_trials times
                # earn (money double) with probability 0.51 and lose (money 0) with probability 0.49
                np.random.seed(trial_time)
                earn_lose = np.random.choice([2, 0], size=position, p=[0.51, 0.49]);
                # calculate the total and daily earnings for given trial
                cumu_ret[trial_time] = sum(earn_lose* position_value);
                daily_ret[trial_time] = cumu_ret[trial_time]/1000 - 1;
            # calculate the mean and std for given position
            mean_daily_ret = np.mean(daily_ret)
            std_daily_ret = np.std(daily_ret)
            # output the results and corresponding histogram
            result.write('Position:  {0}   Position Value:  {1}  Mean:  {2}  Standard Deviation:  {3} \n'.format(position,position_value,mean_daily_ret,std_daily_ret))
            plt.hist(daily_ret,100,range=[-1,1])
            plt.savefig("histogram_"+str(position).zfill(4)+"_pos.pdf")
            plt.close()
        result.close()