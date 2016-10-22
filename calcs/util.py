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
    res = calc.compute()
    t = time.clock() - start
    if isinstance(res, float):
        print 'Computed:\t%.64f\nReference:\t%.64f' % (res, math.pi)
    else:
        print 'Computed:\t%s' % res
        print 'Reference:\t3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067982148086513282306647093844609550582231725359408128481117450284102701938521105559644622948954930381964428810975665933446128475648233786783165271201909145648566923460348610454326648213393607260249141273724587006606315588174881520920962829254091715364367892590360011330530548820466521384146951941511609433057270365759591953092186117381932611793105118548074462379962749567351885752724891227938183011949129833673362440656643086021394946395224737190'
    print 'Time:\t %.8f' % t

if __name__ == '__main__':
    pprint.pprint(list(getCalcs()))