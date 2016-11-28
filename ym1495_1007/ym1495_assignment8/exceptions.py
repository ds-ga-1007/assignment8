'''
Created on Nov 28, 2016

@author: muriel820
'''

class input_bound_exception(Exception):
    def __str__(self):
        return 'please unput with [ ] as bound brackets'

class input_value_exception(Exception):
    def __str__(self):
        return 'please input integers seperated by , '

class input_trial_number_exception(Exception):
    def __str__(self):
        return 'please input a positive integer'
        