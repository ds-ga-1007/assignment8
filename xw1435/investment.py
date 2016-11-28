import numpy as np

class investment:
    '''
    the investment class, that will give cumulative return based on its position and position value
    '''

    def __init__(self, position):
        
        if type(position) == int:
            pass
        if type(position) == float:
            pass
        if position in [1,10,100,1000]:
            pass    
        else:
            raise ValueError("Please select from one of the four options: 1, 10, 100, 1000!")
        
        self.position = position
        self.position_value = 1000/position
    
    def one_day_outcome(self):
        cumu_return = self.position_value
        coin_flip = np.random.rand(self.position)
        
        for i in range(self.position):
            if coin_flip[i] <= 0.49:
                cumu_return -= self.position_value
            else:
                cumu_return += self.position_value 
        return cumu_return          
            