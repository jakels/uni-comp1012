#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 11:42:52 2023

@author: ll22jls@leeds.ac.uk
"""

print("===Celcius to farenheit calculator===")
temperatureInCelcius: float = int(input("Temperature (ºC): "))
temperatureInFarenheit: float = (temperatureInCelcius * (9/5)) + 32


print("The temperature in farenheit will be: ",
      str(temperatureInFarenheit), "ºF")
