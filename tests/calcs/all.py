# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 18:32:24 2016

@author: Nikhil
"""

import time
import numpy as np
import unittest
import logging

from calcs.util import getCalcs

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class CalcTestsMeta(type):
    def __new__(cls, name, bases, attrs):
        for calc, obj in getCalcs():
            attrs['test_pi_%s' % calc] = cls.generate_tc(obj)
        
        #LESSON Not returning the below can cause NoneType errors
        return super(CalcTestsMeta, cls).__new__(cls, name, bases, attrs)
    
    @classmethod
    def generate_tc(cls, calculator):
        def test_accuracy(self):
            start = time.clock()
            ans = calculator().compute()
            logger.info('%s -> %.32f', calculator, ans)            
            self.assertTrue(abs(ans - np.pi) < 1e-6)
            self.assertTrue((time.clock() - start) < 5.0)
        
        return test_accuracy

class CalcTests(unittest.TestCase):
    __metaclass__ = CalcTestsMeta

if __name__ == '__main__':
    unittest.main(exit=False)