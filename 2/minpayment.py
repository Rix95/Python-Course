# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 23:57:37 2022

@author: Rical
"""
balance = 3329
annualInterestRate = 0.2
minpayment = 0
while True:
    rightbalance = balance
    for i in range(12):
        rightbalance -= minpayment
        rightbalance += (0.2/12) * rightbalance
    if rightbalance <= 0:
        break
    minpayment += 10
    
print("Lowest Payment: " + str(round(minpayment, 2)))