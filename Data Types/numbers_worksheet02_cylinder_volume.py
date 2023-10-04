#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 11:39:23 2023

@author: ll22jls@leeds.ac.uk
"""
import math

print("===Cylindrical Volume Calculator===")
cylinderRadius: float = int(input("Cylinder Radius (cm): "))
cylinderHeight: float = int(input("Cylinder Height (cm): "))
cylinderRadiusSquared = (cylinderRadius * cylinderRadius)


cylinderVolume: float = math.pi * cylinderRadiusSquared * cylinderHeight

print("The cylinder with the spciefied values will have a volume of: ",
      str(cylinderVolume), "cm^3")
