# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 17:26:43 2016

This is a simple and very fast implementation of Pi
pi/2 = 1 + 1/3 (1 + 2/5(1 + 3/7(1 + 4/9(1 + ...))))

The algorithm reaches maximum possible accuracy on a 64 bit OS with 49
iterations due to floating point precision limitations

@author: Nikhil
"""
from base import BaseCalculator

class Beeler1972(BaseCalculator):
    
    def __init__(self):
        super(Beeler1972, self).__init__()
    
    def compute(self, N=24):
        
        def nums():
            for i in xrange(N-1, 0, -1):
                yield i
        
        ans = N/(2*N+1.0) + 1.0
        g = nums()
        
        for j in xrange(N-1):
            numerator = g.next()
            ans *= (numerator/(2*numerator+1.0))
            ans += (numerator/(2*numerator+1.0))
        
        return 2*(ans+1)

def main():
    from calcs.util import runCalc
    runCalc(Beeler1972())

if __name__ == '__main__':
    main()