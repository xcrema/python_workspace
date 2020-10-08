# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 11:29:34 2020

@author: Achyut

Statement
Given a list of numbers, print all its even elements. Use a for-loop that iterates over the list itself and not over its indices. That is, don't use range()

Example input
1 2 2 3 3 3 4

Example output
2 2 4
"""

a = [int(s) for s in input().split()]

for i in a:
  if i%2 == 0:
    print(i)




