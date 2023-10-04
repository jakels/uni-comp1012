#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 11:34:14 2023

@author: ll22jls@leeds.ac.uk
"""

print("===Car refuelling calculator===")
tankCapacity: float = float(input("Car tank capacity (litres): "))
kmPerLitre: float = float(input("Car km/litre (km): "))

distanceBeforeRefuel: float = tankCapacity * kmPerLitre

print("The car with the specified values should be able to travel : ",
      str(distanceBeforeRefuel), "km before refuelling")
