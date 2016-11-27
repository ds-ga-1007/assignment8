import pandas as pd
import numpy as np
import matplotlib
import sys
import matplotlib.pyplot as plt


def get_daily_ret(positions, num_trials):
    """collect daily_ret from num_trials iterations of share behavior"""
    pos_ret = np.empty((num_trials, len(positions)))
    cumu_ret = np.empty((num_trials, len(positions)))
    daily_ret = np.empty((num_trials, len(positions)))
    
    for trial in range(num_trials):
        for pos_idx, position in enumerate(positions):
            position.total_value = 0             
            position.bet_shares_independently()
            pos_ret[trial, pos_idx] = position.total_value
        cumu_ret[trial] = pos_ret[trial,:]
        daily_ret[trial] = (cumu_ret[trial]/1000) - 1
    return daily_ret

def graph_daily_ret(positions, num_trials, daily_ret):
    """graph daily return values to histographs and save the hists to file"""
    for pos_idx in range(len(positions)):
        ret_vals = daily_ret[:,pos_idx]
        plt.hist(ret_vals,100,range=[-1,1])
        plt.title('number of shares at ' + str(positions[pos_idx].num_shares) + \
                 ' share value at ' + str(positions[pos_idx].share_value) + \
                 '\nnumtrials: ' + str(num_trials))
        numsharesdisplay = str(positions[pos_idx].num_shares)
        while len(numsharesdisplay) < 4:
            numsharesdisplay = '0' + numsharesdisplay
        plt.savefig('histogram_' + numsharesdisplay + '_pos.pdf', format='pdf')

def get_aggregated_results(daily_ret, positions):
    """get aggregated results from daily_ret about positions returns"""
    means = np.mean(daily_ret, 0)
    stds = np.std(daily_ret, 0)
    
    num_shares = [position.num_shares for position in positions]
    res = np.array((num_shares, means, stds))
    df = pd.DataFrame(np.round(res, 3), index = ['num shares', 'means', 'stds'])
    return df
        
def process_one_day(positions, num_trials):
    """ Process one day of stock behavior, for each of the positions,
    iterate num_trials times to aggregate output distributions"""
    daily_ret = get_daily_ret(positions, num_trials)
    
    graph_daily_ret(positions, num_trials, daily_ret)

    df = get_aggregated_results(daily_ret, positions)

    df.to_csv(r'results.txt', header = False)
    return df


def get_integer_if_possible(s):
    """get an integer from the input, or raise a value error 
    if s does not represent an integer"""
    try: 
        return int(s)
    except ValueError:
        raise ValueError('%s is not an integer' % (s))

def weightedcoinflip(probabilty):
    """A weighted coin flip has chance probability of coming up heads"""
    return np.random.rand() > probabilty

def get_position_list(share_list):
    """get list of positions from string of positons, or raise a ValueError"""
    if not isinstance(share_list, str):
        raise ValueError("get_interval_list only takes in strings. \
                         Received %s" % (type(share_list)))
    cleaned_input = share_list.strip()
    no_brackets = cleaned_input.replace('[','').replace(']','')
    split_positions = str.split(no_brackets, ',')
    positions = []
    for num_shares_input in split_positions:
        num_shares_processed = get_integer_if_possible(num_shares_input)
        positions.append(position(num_shares_processed))
    return positions

class position(object):
    """This class represents a position, which is a distribution
    of an initial investment, evenly distributed among num_shares
    separate shares that are invested independently"""
    def __init__(self, num_shares):
        """All positions contain 1000 montetary units, among num_shares
        shares each worth share_value"""
        if not isinstance(num_shares, int):
            raise ValueError("num_shares must be an integer")
        INITIAL_INVESTMENT = 1000
        self.num_shares = num_shares
        self.share_value = INITIAL_INVESTMENT / num_shares
        self.total_value = 0
        
    def bet_shares_independently(self, probabilty = 0.51):
        """bet all shares with probability = probability.
        Tally the total outcome value of the investment in 
        self.total_value"""
        for share in range(self.num_shares):
            if weightedcoinflip(probabilty = probabilty):
                self.total_value += self.share_value * 2
            
    @property
    def num_shares(self):
        return self._num_shares

    @num_shares.setter
    def num_shares(self, num_shares):
        if not num_shares in [1, 10, 100, 1000]:
            raise ValueError('%s needs to be an exponent \
                             of 10 between 1 and 1000' % (num_shares))
        self._num_shares = num_shares