# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 11:21:29 2020

@author: Achyut

Statement
Given the text: the first line contains the number of lines, then given the lines of words. Print the word in the text that occurs most often. If there are many such words, print the one that is less in the alphabetical order.

Example input
2
apple orange banana
banana orange

Example output
banana
"""

n = int(input())
dic = {}
for i in range(0, n):
  line = [x for x in input().split()]
  for x in line:
    if x in dic:
      dic[x] = dic.get(x)+1
    else:
      dic[x] = 1
temp = max(dic.items(), key = lambda x:x[1])
l = list()
for key, value in dic.items():
  if value == temp[1]:
    l.append(key)

l.sort()
print(l[0])


