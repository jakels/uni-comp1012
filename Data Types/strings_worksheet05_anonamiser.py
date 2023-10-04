#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 12:33:32 2023

@author: ll22jls@leeds.ac.uk
"""

print("===String Input Anonamiser===")
sentenceToAnonamise = input("Please enter a sentence to anonamise: ")
sentencePostAnonamisation = ""

for character in sentenceToAnonamise:
    if character.lower().isalpha():
        if character.isupper():
            sentencePostAnonamisation += "X"
        else:
            sentencePostAnonamisation += "x"
    else:
        sentencePostAnonamisation += character

print(sentencePostAnonamisation)
