# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 20:54:07 2016

@author: Nikhil
"""
import time
import logging
import numpy as np
import matplotlib.pyplot as plt

from calcs.util import getCalcs, getDecimalAccuracy

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

'''
Some arbitrary limits for analysis
'''
maxIterations = {
    'Beeler1972'    : 49,
    'Beeler1972Big' : 250,
    'EulerBasel'    : 200000000,
    'Ramanujan1'    : 3,
}

class CalcAnalyser(object):
    
    def analyzeRateOfGrowth(self):
        for i, (name, calculator) in enumerate(getCalcs()):
            if calculator.__name__ == 'EulerBasel': # Vastly slower, an outlier
                continue
            
            logger.info('Analysing: %s', calculator.__name__)
            calcObj = calculator()
            
            maxN = maxIterations.get(calculator.__name__, 20)
            nIterations = list(np.linspace(1, maxN, min(20, maxN), dtype=np.int))
            
            f, axes = plt.subplots(1, 2, sharex=True, sharey=False)
            
            timings = [] # LESSON: Do not do timings = accuracies = [], they are the same list!
            accuracies = []
            
            for k in nIterations:
                logger.info('Starting %s with %d iterations', calculator.__name__, k)
                start = time.clock()
                ans = calcObj.compute(N=k)
                timings.append(time.clock() - start)
                accuracies.append(getDecimalAccuracy(ans))
            
            logger.debug(nIterations)
            logger.debug(timings)
            logger.debug(accuracies)
            
            axes[0].plot(nIterations, timings, 'r')
            axes[0].set_xlabel('Iterations')
            axes[0].set_ylabel('Time (sec)')
            axes[0].set_title('Timing v/s iterations')
            
            axes[1].plot(nIterations, accuracies, 'b')
            axes[1].set_xlabel('Iterations')
            axes[1].set_ylabel('Num. accurate digits')
            axes[1].set_title('Accuracy v/s iterations')
            
            f.suptitle(calculator.__name__)
            plt.tight_layout()
            f.savefig('figs/%s.png' % calculator.__name__)
        
         # plt.show()
    
    def measureTimings(self):
        timings = []
        names = []
        
        for name, calculator in getCalcs():
            if calculator.__name__ == 'EulerBasel': # Vastly slower, an outlier
                continue
            
            _timings = []
            
            obj = calculator()
            for i in xrange(5):
                start = time.clock()
                obj.compute()
                _timings.append(time.clock() - start)
            
            timings.append(sum(_timings)/float(len(_timings)))
            names.append(obj.__class__.__name__)
        
        return names, timings
    
    def showTimings(self, x, y):
        index = np.arange(len(y))
        
        fig, ax = plt.subplots()
        bar_width = 0.3
        h = 0.0001        
        
        ax.bar(index, y, bar_width, alpha=0.4)
        ax.set_xticks(index + bar_width/2)
        ax.set_xticklabels(x)
        ax.set_ylim([0, max(y) + max(h, max(y)/10)])
        
        for rect, label in zip(ax.patches, y):
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width()/2, height + h/2, \
                    '%.6f' % label, ha='center', va='bottom', color='blue')

        plt.xlabel('Algorithms')
        plt.ylabel('Timings (seconds)')
        plt.title('Timings for Pi computation upto 7 decimal places')
        plt.show()
    
    def run(self):
        x, y = self.measureTimings()
        self.showTimings(x, y)
    
    def run2(self):
        self.analyzeRateOfGrowth()

def main():
    CalcAnalyser().run2()

if __name__ == '__main__':
    main()