# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 15:43:38 2016

@author: Nikhil
"""
import time
import unittest
import numpy as np

from calcs.beeler1972 import Beeler1972

# TODO make a generic test case / test suite

class Beeler1972Test(unittest.TestCase):
    def test_accuracy(self):
        start = time.clock()
        ans = Beeler1972().compute()
        self.assertTrue(abs(ans - np.pi) < 1e-6)
        self.assertTrue((time.clock() - start) < 5.0)

if __name__ == '__main__':
    unittest.main(exit=False)