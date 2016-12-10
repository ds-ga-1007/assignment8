'''
Created on Nov 22, 2016

@author: Caroline

I used the structure of the top answer in the stackoverflow thread below. I didn't borrow specific lines of code.
http://stackoverflow.com/questions/2825452/correct-approach-to-validate-attributes-of-an-instance-of-class
'''

class Investment():
    def __init__(self, position):
        self.position = position
        self.position_value = round(1000/self.position,2) #finds the denomination of each investment
        
    @property
    def position(self):
        return self._position
    
    #validates investment position
    @position.setter
    def position(self, p):
        if not (p in (1, 10, 100, 1000)): raise Exception('Investment position must be 1, 10, 100, or 1000. Invalid value: {0}'.format(p))
        self._position = p