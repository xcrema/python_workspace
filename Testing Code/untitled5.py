# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 11:11:13 2020

@author: Achyut

Make your previous program work with the tests below

def test():
    assert is_multiples([1,2,3,4]) == [False,False,True,False]
    assert is_multiple(3) == "Graph"
    assert is_multiple(5) == "QL"
    assert is_multiple(15) == "GraphQL"
"""
def is_multiples(lis):
  res = list()
  for i in lis:
    if i%3 == 0 or i%5 == 0:
      res.append(True)
    else:
      res.append(False)
  
  return res
  
def is_multiple(i):
  if i%3 == 0 and i%5 == 0:
    return 'GraphQL'
  elif i%3 ==0:
    return 'Graph'
  elif i%5 == 0:
    return 'QL'
  else:
    print(i)
  
    


