# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 11:31:20 2020

@author: Achyut

Statement
Given two lists of numbers, find all the numbers that occur in both the first and the second list. Print them in ascending order.

Example input
1 3 2
4 3 2

Example output
2 3
"""

def intersection(list1, list2):
  list3 = [x for x in list1 if x in list2]
  return list3

list1 = [int(i) for i in input().split()]
list2 = [int(i) for i in input().split()]

list3 = intersection(list1, list2)

list3.sort()

print(list3)



