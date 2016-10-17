# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 20:54:07 2016

@author: Nikhil
"""
import time
import numpy as np
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
        index = np.arange(len(y))
        
        fig, ax = plt.subplots()
        bar_width = 0.3
        ax.bar(index, y, bar_width, alpha=0.4)
        ax.set_xticks(index + bar_width/2)
        ax.set_xticklabels(x)
        
        for rect, label in zip(ax.patches, y):
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width()/2, height + .01, \
                    '%.6f' % label, ha='center', va='bottom', color='blue')

        plt.xlabel('Algorithms')
        plt.ylabel('Timings (seconds)')
        plt.title('Default timings for Pi computation')
        plt.show()

def main():
    a = CalcAnalyser()
    a.showDefaultTimings()

if __name__ == '__main__':
    main()