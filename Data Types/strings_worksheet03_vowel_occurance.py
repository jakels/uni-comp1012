#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 12:12:43 2023

@author: ll22jls@leeds.ac.uk
"""

print("===Vowel Count Calculator===")
vowelList: list = ["a", "e", "i", "o", "u"]
searchSentence: str = input("Enter a search sentence: ")
totalVowels: int = 0

for character in searchSentence.lower():
    if character in vowelList:
        totalVowels += 1

print(str(totalVowels))
