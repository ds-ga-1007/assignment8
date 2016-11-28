import numpy as np
from decimal import Decimal


class investment():
    '''
    input a list of postions and return a dict that contains the all the result
    '''
    def __init__(self, positions, num_trails):
        self.positions = positions
        self.num_trails = num_trails
        self.pos_daily_ret = dict()
        # loop through each poisition
        for position in self.positions:
            init_value = 1000
            # try to get the position value. handle error for input like 33, which can not devide 10000.
            try:
                position_value = int(init_value/position)
            except:
                raise ValueError("Input position can not be divided by 1000")

            cumu_ret = dict()
            daily_ret = dict()
            # loop through every trails
            for trail in range(self.num_trails):
                # create a local list to record the result in each trail.
                # eg. if the position is 1000, then the list will be appended by the result of each time
                result_in_day = list()
                for buy_times in range(position):
                    # use numpy randome choice. if it wins, then the result should be 2 (1+1) or 0(1-1).
                    result_in_day.append((1+ np.random.choice([1,-1],p=[0.51,0.49])) * position_value)
                # append the total win or lose for the trail to the cumu_ret
                cumu_ret[trail] = sum(result_in_day)
                # append the total win or lose for the trail to the daily_ret
                daily_ret[trail] = float(round(Decimal((sum(result_in_day)/1000) - 1),6))
                #append the list of daily_ret to the pos_daily_ret dict. Key is the position, and the value is the list of daily_ret in each trail.
            self.pos_daily_ret[position] = daily_ret
    def result (self):
        return self.pos_daily_ret