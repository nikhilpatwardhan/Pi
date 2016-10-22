# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 08:55:46 2016

@author: Nikhil
"""
import math

from base import BaseCalculator

class Ramanujan1(BaseCalculator):
    
    def __init__(self):
        super(BaseCalculator, self).__init__()

    def compute(self, N=3):
        ans = 0.
        for i in xrange(N):
            ans += (math.factorial(4*i)/math.pow(math.factorial(i),4)) * \
                   ((1103 + 26390 * i)/math.pow(396, 4*i))
        
        return 9801/(math.sqrt(8) * ans)

def main():
    from calcs.util import runCalc
    runCalc(Ramanujan1())

if __name__ == '__main__':
    main()