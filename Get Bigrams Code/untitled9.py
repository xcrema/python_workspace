# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 11:16:51 2020

@author: Achyut

Write a function(get_bigrams(text)) to do the following:
1. Takes each sentence (a sentence is terminated by a period or ? or !) and creates bigrams (pairs of words)
2. Returns unique bigrams

Example
Input:  This is a test. This is another test, along with another Final Test.
output: 
 
[ "this is", 
"is a",
"a test",
"is another",
"another test",
"test along",
"along with",
"with another",
"another final",
"final test"]
"""
import re

def get_bigrams(texts):
  text = texts.replace(",", "")
  text = text.replace(". ", ".")
  text = text.lower()
  text = re.split('\.|\?|!',text)
  res = list()
  print(text)
  for line in text:
      tmp = line.split()
      
      for x in range(0, len(tmp)-1):
          st = ""
          for y in range(x, x+2):
              st = st+tmp[y]+" "
          st = st.strip()
          if st not in res:
            res.append(st)
  
  return res

