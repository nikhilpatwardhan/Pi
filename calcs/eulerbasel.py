# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 15:35:23 2016

https://en.wikipedia.org/wiki/Basel_problem

@author: Nikhil
"""
import time
import numpy as np
import multiprocessing
import logging

from math import sqrt
from base import BaseCalculator

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def _compute(t):
    s, n = t[0], t[1]   # Python 2.7
    ans = 0.
    for x in xrange(s, n+1):
        ans += 1.0/(x*x)
    return ans

class EulerBasel(BaseCalculator):
    
    def __init__(self, strategy='multiprocess'):
        self.compute = self._getCompute(strategy)
        self.maxN = 100000000
        self.defaultN = 3000000
    
    def _getCompute(self, strategy):
        return self._compute_multiprocess if strategy == 'multiprocess' \
               else self._compute_single
    
#==============================================================================
#     def compute(self, s=1, N=None):
#         N = N or self.defaultN
#         def sq():
#             for i in xrange(s, N+1):
#                 yield i*i
#         
#         x = np.fromiter(sq(), np.double)
#         return np.sqrt(6*np.sum(1/x))
#==============================================================================
    
    def _compute_single(self, s=1, N=None):
        N = N or self.defaultN
        ans = 0.
        for x in xrange(s, N+1):
            ans += 1.0/(x*x)        #LESSON x**2 is very slow!
        return sqrt(6*ans)
    
#==============================================================================
#     def compute(self, s=1, N=None):
#         '''
#         Implemented just because it can be
#         Turns out to be slower than compute_math()
#         '''
#         N = N or self.defaultN
#         return math.sqrt(6*reduce(lambda x,y: x+y, [1.0/(a*a) for a in xrange(s,N+1)]))
#==============================================================================
    
    def _compute_multiprocess(self, N=None):
        N = N or self.defaultN
        
        nProcessors = multiprocessing.cpu_count()
        partitions = np.linspace(1, N, nProcessors + 1, dtype=np.int)
        starts = [1] + [i+1 for i in partitions[1:]]
        
        pool = multiprocessing.Pool(nProcessors)
        
        return sqrt(6*sum(pool.map(_compute, zip(starts, partitions[1:]))))

def main():
    start = time.clock()
    print 'Computed:\t%.64f\nReference:\t%.64f' % (EulerBasel().compute(), np.pi)
    print 'Time:\t %.8f' % (time.clock() - start)

if __name__ == '__main__':
    main()