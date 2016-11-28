'''
Created on Nov 27, 2016

These are the user-defined errors for this program.

@author: ShashaLin

'''

class Errors(Exception):
    pass

class InputError(Errors):
    def __init__(self, message):
        self.message = message
        print(self.message)
        