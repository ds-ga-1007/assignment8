'''
Created on 2016年12月4日

@author: bz866
'''


"""Handling excepetions by raising error """
class InvalidListError(Exception):
    def __str__(self):
        return 'Invalid position list. '

class PositionError(Exception):
    def __str__(self):
        return 'Invalid positions in your list. '

class IntegerError(Exception):
    def __str__(self):
        return 'Invalid Value. Trail number must be a integer.' 