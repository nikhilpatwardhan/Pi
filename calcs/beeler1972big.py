# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 10:14:56 2016

Ref: https://crypto.stanford.edu/pbc/notes/pi/code.html

@author: Nikhil
"""
import logging

from decimal import Decimal, getcontext
from cStringIO import StringIO

from base import BaseCalculator

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class Beeler1972Big(BaseCalculator):
    
    def __init__(self):
        super(BaseCalculator, self).__init__()
    
    def compute(self, N=250):
        N, res = N*14, 0.
        getcontext().prec = N*4
        s = None
        
        try:
            s = StringIO()
            s.write('.')
            r = [2000] * (N+1)
            c = 0
            
            for k in xrange(N, 1, -14):
                d = 0
                i = k
                while True:
                    d += r[i] * 10000
                    b = 2 * i - 1
                    r[i] = d % b
                    d /= b
                    i -= 1
                    if not i:
                        break
                    d *= i
                    
                    logger.debug(r)
                    logger.debug('d=%d, b=%d, i=%d, c=%d', d, b, i, c)
                
                _s = '%04d' % (c + d/10000)
                s.write(_s)
                logger.debug('DIGITS:%s', _s)                
                c = d % 10000
        
        finally:
            if s:
                res = Decimal(s.getvalue()) * 10
                s.close()
        return res

def main():
    from calcs.util import runCalc
    runCalc(Beeler1972Big())

if __name__ == '__main__':
    main()