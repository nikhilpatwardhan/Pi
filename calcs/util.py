# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 20:37:35 2016

@author: Nikhil
"""
import os
import imp
import sys
import inspect
import pprint
import math
import time

def getCalcs():
    f, p, d = imp.find_module('calcs')
    calc_modules = ['calcs.' + os.path.splitext(m)[0]
                    for m in os.listdir(p) if m.endswith('.py')]
    
    for calc in calc_modules:
        if calc not in sys.modules:
            __import__(calc)
        
        for _, obj in inspect.getmembers(sys.modules[calc]):
            if inspect.isclass(obj) and obj.__module__ != 'calcs.base' \
                and hasattr(obj, 'compute'):
                yield calc.split('.')[1], obj

def runCalc(calc):
    start = time.clock()
    print 'Computed:\t%.64f\nReference:\t%.64f' % (calc.compute(), math.pi)
    print 'Time:\t %.8f' % (time.clock() - start)

if __name__ == '__main__':
    pprint.pprint(list(getCalcs()))