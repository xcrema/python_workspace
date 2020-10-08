# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 11:29:09 2020

@author: Achyut

Statement
Given a sequence of non-negative integers, where each number is written in a separate line. The sequence ends with 0. Print the average of the sequence. 

Example input
10
30
0

Example output
20.0
"""

sum = 0
n = 0
i = int(input())
while i != 0:
  n=n+1
  sum=sum+i
  i = int(input())

print(sum/n)
