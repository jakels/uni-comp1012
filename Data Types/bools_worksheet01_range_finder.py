# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 14:44:48 2023

@author: Jake
"""

print("===Valid Range Detector===")
checkValue: int = int(input("Please enter a value to be checked: "))
validValue: bool = checkValue >= 0 and checkValue <= 94

if validValue:
    print("Correct, in range")
else:
    print("Incorrect, outside of range")