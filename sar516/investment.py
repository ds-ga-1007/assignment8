import numpy as np


class investment:
    """This class will take a single value to build a model of an investment that will add up to $1000"""
    def __init__(self, position):
        if type(position) == int :
            pass
        elif type(position) == float :
            pass
        else :
            raise ValueError("Improper type for this class")
            
        self.position_value = 1000 / position
        self.position = position
        
        if self.position in [1, 10, 100, 1000] :
                pass
        else :
            raise ValueError("Improper values passed for this class")
    
    
    def day_instance(self) :
        """This function simulates a single day of this type of investment"""
        cumu_return = 1000
        number = 0
        flip_of_the_coin = (np.random.rand(self.position) > 0.49).astype(int)
        while number < self.position :
            if flip_of_the_coin[number] == 1 :
                cumu_return = cumu_return + self.position_value
            else :
                cumu_return = cumu_return - self.position_value
                
            number = number + 1
        else :
            return cumu_return