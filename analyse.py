# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 20:54:07 2016

@author: Nikhil
"""
import time
import matplotlib.pyplot as plt

from calcs.util import getCalcs

class CalcAnalyser(object):
    
    def __init__(self):
        self.calculators = getCalcs()
    
    def _measureDefaultTimings(self):
        timings = []
        names = []
        
        for name, calculator in self.calculators:
            obj = calculator()
            start = time.clock()
            obj.compute()
            timings.append(time.clock() - start)
            names.append(obj.__class__.__name__)
        
        return names, timings
    
    def showDefaultTimings(self):
        x, y = self._measureDefaultTimings()
        index = range(len(y))
        plt.bar(index, y, 0.5, alpha=0.4)
        plt.xticks([i + 0.25 for i in index], x, ha='center')
        plt.xlabel('Algorithms')
        plt.ylabel('Timings (seconds)')
        plt.title('Default timings for Pi computation')
        plt.show()

def main():
    a = CalcAnalyser()
    a.showDefaultTimings()

if __name__ == '__main__':
    main()