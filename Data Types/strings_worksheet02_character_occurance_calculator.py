#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 12:06:48 2023

@author: ll22jls@leeds.ac.uk
"""

print("===Character occurance calculator===")
inputSentence: str = input("Please enter a input sentence: ")
searchCharacter: str = input("Please enter a search character: ")

print(str(inputSentence.lower().count(searchCharacter.lower())))