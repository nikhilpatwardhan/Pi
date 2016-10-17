# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 17:26:43 2016

http://web.mit.edu/uma/www/notes/pi_or_not.pdf

pi/2 = 1 + 1/3 (1 + 2/5(1 + 3/7(1 + 4/9(1 + ...))))

@author: Nikhil
"""

import time
import numpy as np

from base import BaseCalculator

# TODO Compute and show arbitrary precision
# TODO Comment that default N is for a specific accuracy

class Beeler1972(BaseCalculator):
    def compute(self, N=39):
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
    start = time.clock()
    print 'Computed:\t%.64f\nReference:\t%.64f' % (Beeler1972().compute(), np.pi)
    print 'Time:\t %.8f' % (time.clock() - start)

if __name__ == '__main__':
    main()