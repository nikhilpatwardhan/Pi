# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 15:35:23 2016

https://en.wikipedia.org/wiki/Basel_problem

@author: Nikhil
"""
import time
import math
import numpy as np

from base import BaseCalculator

class EulerBasel(BaseCalculator):
    
    def __init__(self, strategy='math'):
        self.compute = self.compute_math if strategy == 'math' else self.compute_np
        self.maxN = 100000000
        self.defaultN = 30000000
    
    def compute_np(self, N=None):
        N = N or self.defaultN
        def sq():
            for i in xrange(1, N+1):
                yield i*i
        
        x = np.fromiter(sq(), np.double)
        return np.sqrt(6*np.sum(1/x))
    
    def compute_math(self, N=None):
        N = N or self.defaultN
        ans = 0.0
        for x in xrange(1, N+1):
            ans += 1.0/(x*x)        #LESSON x**2 is very slow!
        return math.sqrt(6*ans)
    
    def compute_reduce(self, N=None):
        N = N or self.defaultN
        return math.sqrt(6*reduce(lambda x,y: x+y, [1.0/(a*a) for a in xrange(1,N+1)]))

def main():
    start = time.clock()
    print 'Computed:\t%.64f\nReference:\t%.64f' % (EulerBasel().compute(), np.pi)
    print 'Time:\t %.8f' % (time.clock() - start)

if __name__ == '__main__':
    main()