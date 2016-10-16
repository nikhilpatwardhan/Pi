# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 15:35:23 2016

@author: Nikhil
"""
import math

from base import BaseCalculator

class EulerBasel(BaseCalculator):
    def compute(self, N=2000000):
        ans = 0.0
        for x in xrange(1, N+1):
            ans += 1.0/(x*x)        # x**2 is very slow!
        return math.sqrt(6*ans)

def main():
    print EulerBasel().compute()

if __name__ == '__main__':
    main()