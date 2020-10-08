# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 11:27:49 2020

@author: Achyut

Statement
Given a three-digit number. Find the sum of its digits.

Example input
123

Example output
6
"""
# Read an integer:
a = int(input())
sum = 0
while a>0:
  sum = sum+a%10
  a = int(a/10)

print(sum)


