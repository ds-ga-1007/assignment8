import numpy as np
import re

class InvestmentPositions(object):
    
    def __init__(self, count, value):
        self.count = count
        self.value = value
        
    def simulate_one_share(self):
        success = np.random.random_sample() > 0.49
        return self.value * (2 if success else 0)
        
    def one_day_return(self):
        return sum(self.simulate_one_share() for i in range(self.count))
        
    def n_days_return(self, num_trials):
        return [self.one_day_return() for i in range(num_trials)]
        
    def __repr__(self):
        return "{} shares of ${}".format(self.count, self.value)
    
    @classmethod
    def parse_positions(cls, listAsString):
        if re.match(r"\[\d+, \d+, \d+, \d+\]", listAsString) is None:
            raise ValueError("Invalid list format")
        
        splits = [int(num.strip().strip("[]")) for num in listAsString.split(",")]
    
        position_vals = [int(1000 / position) for position in splits]
    
        return [cls(val, split) for (val, split) in zip(position_vals, splits)]