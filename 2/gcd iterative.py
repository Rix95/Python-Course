# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 12:05:01 2022

@author: Rical
"""

def gcdIter(a, b):
    temp = b
    if a > b:
        temp = a
        a = b
        b = temp
        
    while a > 1:
        if b % a == 0 and temp % a == 0:
            break
        else:
            a -= 1
    return a        

print(gcdIter(12,8))





#test
