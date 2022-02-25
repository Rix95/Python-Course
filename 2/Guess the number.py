# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 18:52:43 2022

@author: Rical
"""
#lowest and highest value
l = 0
h = 100
#midpoint

print("Please think of a number between 0 and 100!")
while True:
    m = (h + l) // 2
    print("Is your secret number " + str(m))
    guess = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if guess == "h":
        h = m    
    elif guess == "l":
        l = m
    elif guess == "c":
        print("Game over. Your secret number was: " + str(m))
        break
    else:
        print("Sorry, I did not understand your input.")x