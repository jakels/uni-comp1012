# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 14:57:40 2023

@author: Jake
"""

print("===Alcohol Sale Validator===")
print("Please input the required information into this form and only commit"
      "The sale if the program says the sale is valid")
customerReportedAge: int = int(input("Age the customer says they are: "))
legalAgeOfSale: int = int(input("Please enter the legal age of alcohol sale: "))
paidByCard: bool = bool(input("Paid by card? Y/N: ").lower() == "y")
ageOnID: int = int(input("Age on customer ID: "))
estimatedAge: int = int(input("Enter the estimated age of customer: "))

saleValid: bool = False
if customerReportedAge == ageOnID:
    if ageOnID >= legalAgeOfSale:
        saleValid = True

if paidByCard == True:
    saleValid = True

if estimatedAge >= 21:
    saleValid = True
    
print("Should commit sale : " + str(saleValid))