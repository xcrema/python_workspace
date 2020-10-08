# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 11:30:47 2020

@author: Achyut

Statement
Given a list of numbers, find and print the elements that appear in it only once. Such elements should be printed in the order in which they occur in the original list.

Example input
4 3 5 2 5 1 3 5

Example output
4 2 1

"""

# Read a list of integers:
a = [int(s) for s in input().split()]

for i in a:
  if a.count(i) == 1:
    print(i)




