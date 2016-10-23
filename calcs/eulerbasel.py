# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 15:35:23 2016

https://en.wikipedia.org/wiki/Basel_problem

Computes Pi as follows:
Pi = sqrt(6 * S)
Where
S is the sum of inverse squares of natural numbers from 1 to infinity

The squaring requires a lot of computation and so this is an extremely
slow calculator and takes many more iterations to even get past 7 decimal
digit accuracy

@author: Nikhil
"""
import multiprocessing
import numpy as np

from math import sqrt
from base import BaseCalculator

def _compute(t):
    '''
    This function is here to allow Pickling
    cPickle.PicklingError: Can't pickle <type 'function'>: attribute lookup __builtin__.function failed
    '''
    s, n = t[0], t[1]   # Python 2.7
    ans = 0.
    for x in xrange(s, n+1):
        ans += 1.0/(x*x)
    return ans

class EulerBasel(BaseCalculator):
    
    def __init__(self, execType='multiprocess'):
        super(EulerBasel, self).__init__()
        self.setCompute(execType)
    
    def setCompute(self, execType):
        if execType == 'multiprocess':
            self.compute = self._compute_multiprocess
        elif execType == 'single':
            self.compute = self._compute_single
        else:
            raise ValueError('Invalid execution type: %s', execType)
    
    def _compute_single(self, N=20000000):
        ans = 0.
        for x in xrange(1, N+1):
            ans += 1.0/(x*x)        #LESSON x**2 is very slow!
        return sqrt(6*ans)
    
    def _compute_multiprocess(self, N=20000000):
        nProcessors = multiprocessing.cpu_count()/2
        partitions = np.linspace(1, N, nProcessors + 1, dtype=np.int)
        starts = [1] + [i+1 for i in partitions[1:]]
        
        pool = multiprocessing.Pool(nProcessors)
        
        return sqrt(6*sum(pool.map(_compute, zip(starts, partitions[1:]))))

def main():
    from calcs.util import runCalc
    runCalc(EulerBasel())

if __name__ == '__main__':
    main()