
"""
Created on Mon Nov 28 2016
@author: Yanan Shi/ys2506
@desc: handle exceptions
"""
#User defined exception(s) are employed for indicating error conditions
class InvalidInputException(Exception):
    def __str__(self):
        #the innput is not valid
        return 'Invalid input'
