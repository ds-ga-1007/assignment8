import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
"""Functions for use of processing of the position class"""


def get_daily_ret(positions, num_trials):
    """collect daily_ret from num_trials iterations of share behavior"""
    pos_ret = np.empty((num_trials, len(positions)))
    cumu_ret = np.empty((num_trials, len(positions)))
    daily_ret = np.empty((num_trials, len(positions)))
    
    for trial in range(num_trials):
        for pos_idx, pos in enumerate(positions):
            pos.total_value = 0             
            pos.bet_shares_independently()
            pos_ret[trial, pos_idx] = pos.total_value
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
    
    num_shares = [pos.num_shares for pos in positions]
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