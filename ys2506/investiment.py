import matplotlib.pyplot as plt
import numpy as np

class InvestmentInstrument(object):
    def __init__(self, positions, win_rate = 0.51, win_ravenue = 1., lose_ravenue = -1.):
        self.daily_ret = None
        self.positions = positions
        self.win_rate = win_rate
        self.win_ravenue = win_ravenue
        self.lose_ravenue = lose_ravenue


    def investment_simulate(self, principal, num_trials):
        def revenue(position):
            def outcome(value):
                ravenue = self.win_ravenue if np.random.uniform() <= self.win_rate else self.lose_ravenue
                return value * (1 + ravenue)
            
            value = principal / position
            return sum(np.vectorize(outcome)(np.repeat(value, position))) / principal - 1
        
        return np.array([np.vectorize(revenue)(self.positions) for _ in range(num_trials)])


