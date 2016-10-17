# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 18:32:24 2016

@author: Nikhil
"""

import os
import imp
import sys
import time
import numpy as np
import inspect
import unittest
import logging

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class CalcTestsMeta(type):
    def __new__(cls, name, bases, attrs):
        f, p, d = imp.find_module('calcs')
        calc_modules = ['calcs.' + os.path.splitext(m)[0]
                        for m in os.listdir(p) if m.endswith('.py')]
        
        for calc in calc_modules:
            if calc not in sys.modules:
                __import__(calc)
            
            for _, obj in inspect.getmembers(sys.modules[calc]):
                if inspect.isclass(obj):
                    if hasattr(obj, 'compute'):
                        attrs['test_pi_%s' % calc.replace('.','_')] = cls.generate_tc(obj)
        
        #LESSON Not returning the below can cause NoneType errors
        return super(CalcTestsMeta, cls).__new__(cls, name, bases, attrs)
    
    @classmethod
    def generate_tc(cls, calculator):
        def test_accuracy(self):
            start = time.clock()
            try:
                ans = calculator().compute()
                logger.info('%s -> %.32f', calculator, ans)
            except NotImplementedError:
                return
            
            self.assertTrue(abs(ans - np.pi) < 1e-6)
            self.assertTrue((time.clock() - start) < 5.0)
        
        return test_accuracy

class CalcTests(unittest.TestCase):
    __metaclass__ = CalcTestsMeta

if __name__ == '__main__':
    unittest.main(exit=False)