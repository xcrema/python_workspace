# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 11:26:57 2020

@author: Achyut
Statement
Given a two-digit integer, swap its digits and print the result. 

Example input
79

Example output
97
"""

# Read an integer:
a = int(input())
b = ((a%10)*10)+int(a/10)
print(b)




