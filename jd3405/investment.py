# Solution for DS-GA 1007 Assignment#8
# Author: Jiaming Dong (jd3405@nyu.edu)
# NYU Center for Data Science

import numpy as np


class Investment:

    def __init__(self, position):
        """initialization function, set the position and position value"""
        self.position = position
        self.position_value = 1000 / position
        self.ret = 0

    def invest(self):
        """one investing operation, using numpy random values, and calculate the corresponding result"""
        rand_values = np.random.rand(self.position)
        self.ret = 0
        for rand_value in rand_values:
            # [0, 0.51) and [0.51, 1]
            if rand_value < 0.51:
                self.ret += self.position_value * 2
