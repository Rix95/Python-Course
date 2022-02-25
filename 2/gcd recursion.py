# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 13:12:56 2022

@author: Rical
"""

def gcdRecur(a, b):
    remainder = b
    if remainder == 0:
       return a
    else:
       return gcdRecur(b, a % b)        
    
    
    



print(gcdRecur(1071,462))
    