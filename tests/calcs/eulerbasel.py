# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 15:43:38 2016

@author: Nikhil
"""
import time
import unittest
import numpy as np

from calcs.eulerbasel import EulerBasel

class EulerBaselTest(unittest.TestCase):
    def test_accuracy(self):
        start = time.clock()
        ans = EulerBasel().compute()
        self.assertTrue(abs(ans - np.pi) < 1e-6)
        self.assertTrue((time.clock() - start) < 5.0)

if __name__ == '__main__':
    unittest.main(exit=False)