# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 14:46:34 2016

@author: Nikhil
"""

import unittest

from calcs.beeler1972big import Beeler1972Big
from calcs.util import PI999

class BigPiTest(unittest.TestCase):
    
    def test_999(self):
        pi = Beeler1972Big().compute(N=250)
        self.assertTrue(pi.to_eng_string() == PI999)

if __name__ == '__main__':
    unittest.main(exit=False)