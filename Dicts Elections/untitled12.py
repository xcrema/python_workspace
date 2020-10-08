# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 11:20:43 2020

@author: Achyut

Statement
The first line contains the number of records. After that, each entry contains the name of the candidate and the number of votes they got in some state. Count the results of the elections: sum the number of votes for each candidate. Print candidates in the alphabetical order.

Example input
5
McCain 10
McCain 5
Obama 9
Obama 8
McCain 1

Example output
McCain 16
Obama 17
"""
import collections
n = int(input())
dic = {}
for i in range(0, n):
  inp = [x for x in input().split()]
  if dic.get(inp[0]) != None:
    dic[inp[0]] = dic.get(inp[0])+int(inp[1])
  else:
    dic[inp[0]] = int(inp[1])
dic = collections.OrderedDict(sorted(dic.items()))
for key in dic:
  print(key, dic[key])


