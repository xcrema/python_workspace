# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 11:22:12 2020

@author: Achyut

Statement
Given a list of countries and cities of each country, then given the names of the cities. For each city print the country in which it is located.

Example input
2
USA Boston Pittsburgh Washington Seattle
UK London Edinburgh Cardiff Belfast
3
Cardiff
Seattle
London

Example output
UK
USA
UK
"""

dic = {}
n = int(input())
for i in range(0, n):
  inp = [x for x in input().split()]
  dic[inp[0]] = inp[1:]

n = int(input())
for i in range(0, n):
  inp = input()
  for key, value in dic.items():
    for x in value:
      if x == inp:
        print(key)


