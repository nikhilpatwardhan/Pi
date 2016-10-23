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
from decimal import Decimal

PI999 = '3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603486104543266482133936072602491412737245870066063155881748815209209628292540917153643678925903600113305305488204665213841469519415116094330572703657595919530921861173819326117931051185480744623799627495673518857527248912279381830119491298336733624406566430860213949463952247371907021798609437027705392171762931767523846748184676694051320005681271452635608277857713427577896091736371787214684409012249534301465495853710507922796892589235420199561121290219608640344181598136297747713099605187072113499999983729780499510597317328160963185950244594553469083026425223082533446850352619311881710100031378387528865875332083814206171776691473035982534904287554687311595628638823537875937519577818577805321712268066130019278766111959092164201980'

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
        print 'Reference:\t3.1415926535897932384626433832795028841971693993751'
    print 'Time:\t %.8f' % t

def getDecimalAccuracy(x):
    if isinstance(x, float):
        p = str('%.51f' % math.pi)
        q = str('%.51f' % x)
        for i,(a,b) in enumerate(zip(p,q)):
            if a != b:
                break
        return max(0, i-2)
    elif isinstance(x, Decimal):
        p = x.to_eng_string()
        L = min(len(p), len(PI999))
        q = PI999[:L]
        for i,(a,b) in enumerate(zip(p,q)):
            if a != b:
                break
        return max(0, i-2)
    else:
        raise ValueError('Invalid type: %s : %s', str(x), str(type(x)))
    
if __name__ == '__main__':
    pprint.pprint(list(getCalcs()))