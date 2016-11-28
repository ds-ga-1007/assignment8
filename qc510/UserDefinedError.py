# -*- coding: utf-8 -*-
"""
This file includes user defined exceptions:

InputErrorPositions: when positions are in wrong format.

InputErrorTrials: when trials are negative number.

@author: Qianyu Cheng
"""


class InputErrorPositions(Exception):

    def __str__(self):
        return 'There is error in your input. Please enter another one follow the instructions. ' \
               '\n enter values from 1,10,100,1000 and include them in [].'


class InputErrorTrials(Exception):

    def __str__(self):
        return 'There is error in your input. Please enter a positive integer. e.g.: 100000'

