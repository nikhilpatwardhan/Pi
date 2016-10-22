# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 15:26:48 2016

@author: Nikhil
"""

class BaseCalculator(object):
    '''
    Base class of all iterative Pi calculators
    '''
    def __init__(self):
        self.maxN = 100000
        self.defaultN = 5000
    
    def compute(self, N=None):
        '''
        Returns a Decimal value of pi, defaults to precision of 7 decimal places
        :param N: Number of iterations
        :type N: int
        '''
        raise NotImplementedError()