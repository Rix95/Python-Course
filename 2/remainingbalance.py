# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 23:45:34 2022

@author: Rical
"""
balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

for i in range(12):
    balance -= balance * monthlyPaymentRate
    balance += (annualInterestRate / 12) * balance
    
print("Remaining balance: " + str(round(balance, 2)))