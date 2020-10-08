# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 11:28:20 2020

@author: Achyut

Statement
Given five integers, print the least of them.

Example input
10
20
30
40
50

Example output
10
"""


a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

if(a<b and a<c and a<d and a<e):
  print(a)
elif(b<a and b<c and b<d and b<e):
  print(b)
elif(c<a and c<b and c<d and c<e):
  print(c)
elif(d<a and d<b and d<c and d<e):
  print(d)
else:
  print(e)
