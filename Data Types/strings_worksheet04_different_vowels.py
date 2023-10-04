#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 12:26:33 2023

@author: ll22jls@leeds.ac.uk
"""

print("===Different Vowel Count Calculator===")

vowelCountDict: dict = {
        "a": 0,
        "e": 0,
        "i": 0,
        "o": 0,
        "u": 0
    }

searchSentence: str = input("Please enter a search sentence: ")

for character in searchSentence:
    if character in vowelCountDict.keys():
        vowelCountDict[character] += 1

for key in vowelCountDict.keys():
    if vowelCountDict[key] > 0:
        print("Vowel ", key, " occured ", str(vowelCountDict[key]), " times")
    else:
        print("Vowel ", key, " never occured")
