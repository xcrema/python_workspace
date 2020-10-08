# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 11:17:50 2020

@author: Achyut

 Same as get_bigrams except that each term is a group of three words.

function - get_trigrams(text)

Example
input: This is a test? This is another test, along with another final test.
output: (serial order is not important)
 
['this is a', 'is a test', 'this is another', 'is another test',
"""

import re

def get_trigrams(texts):
  text = texts.replace(",", "")
  text = text.replace(". ", ".")
  text = text.lower()
  text = re.split('\.|\?|!',text)
  res = list()
  print(text)
  for line in text:
      tmp = line.split()
      
      for x in range(0, len(tmp)-2):
          st = ""
          for y in range(x, x+3):
              st = st+tmp[y]+" "
          st = st.strip()
          if st not in res:
            res.append(st)
  
  return res

