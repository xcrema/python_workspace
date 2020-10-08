# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 11:30:23 2020

@author: Achyut

Statement
Given a list of distinct numbers, swap the minimum and the maximum and print the resulting list.

Example input
3 4 5 2 1

Example output
3 4 1 2 5
"""
# Read a list of integers:
a = [int(s) for s in input().split()]

ind1 = a.index(max(a))
ind2 = a.index(min(a))

tmp = a[ind1]
a[ind1] = a[ind2]
a[ind2] = tmp

# Print a value:
print(a)


