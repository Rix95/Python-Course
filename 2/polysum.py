# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 16:53:45 2022

@author: Rix
"""

import math

def polysum(n, s):
    def area(n,s):
        return ((0.25 * n * s**2) / math.tan(math.pi / n))
    def perimeter(n, s):
        return n * s
    return round(area(n, s) + (perimeter(n, s)**2), 4) 

#optional test
print(polysum(3,4))
print(area(4,3))







