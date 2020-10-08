# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 11:18:53 2020

@author: Achyut

The text is given in a single line. For each word of the text count the number of its occurrences before it.
"""

a = [i for i in input().split()]
temp = []
for i in a:
  print(temp.count(i))
  temp.append(i)
  


