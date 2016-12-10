
import numpy as NP
import numpy.random as RNG
import matplotlib.pyplot as PL

class Trial:
    '''
    Class representing a series of random trials for a given position.

    The trials are simulated upon instantiation.

    Parameters
    ----------
    position : int
    num_trial : int
    '''
    def __init__(self, position, num_trial):
        position_value = 1000 / position
        self._cumu_ret = NP.zeros(num_trial)
        for i in range(num_trial):
            outcomes = RNG.choice(
                    [0, 2 * position_value],
                    size=[position],
                    p=[0.49, 0.51]
                    )
            self._cumu_ret[i] = outcomes.sum()
        self._daily_ret = (self._cumu_ret / 1000) - 1

    @property
    def mean(self):
        '''
        The mean outcome of this set of trials
        '''
        return self._daily_ret.mean()

    @property
    def std(self):
        '''
        The standard deviation of this set of trials
        '''
        return self._daily_ret.std()

    def plot(self, filename):
        '''
        Plot the histogram of simulated daily outcomes in this trial and
        save the figure into a file.

        Parameters
        ----------
        filename : str
        '''
        fig, ax = PL.subplots(nrows=1, ncols=1)
        fig.set_size_inches(12, 12)
        ax.hist(self._daily_ret, 100, range=[-1, 1])
        fig.savefig(filename)
        PL.close(fig)
