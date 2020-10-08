# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 11:08:17 2020

@author: Achyut

Write a program that prints the numbers from 1 to 100.
But for multiples of three print “World” instead of the number and for the multiples of five print “Peace”.
For numbers which are multiples of both three and five print “WorldPeace”.

"""

for i in range(1, 101):
  if i%3 == 0 and i%5 == 0:
    print('WorldPeace')
  
  elif i%3 ==0:
    print('World')
  elif i%5 == 0:
    print('Peace')
  
  else:
    print(i)
