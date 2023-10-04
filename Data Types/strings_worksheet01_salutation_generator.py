#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 11:47:15 2023

@author: ll22jls@leeds.ac.uk
"""

print("===Salutations Generator===")
usersName: str = input("Please enter your name: ")

usersNameLowerCap: str = usersName.lower()
usersNameFormalised: str = []

for i in range(len(usersNameLowerCap)):
    isFirstname = i == 0
    isSurname = usersNameLowerCap[i-1] == " " or usersNameLowerCap[i-1] == "-"

    if isFirstname or isSurname:
        usersNameFormalised.append(usersNameLowerCap[i].capitalize())
    else:
        usersNameFormalised.append(usersNameLowerCap[i])

print("Salutations ", str.join("", usersNameFormalised))
