# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 11:16:04 2020

@author: Achyut

Write a function(get_top_filtered_words(text,filter_words)) to do the following:
1. cleans "text" - removes punctuation
2. lower cases all text
3. removes filter words
4. returns the top 3 most frequently occurring words in a list

Note: Copy/Paste functions from your previous answer(s).
"""
#from collections import Counter
def get_top_filtered_words(text,filter_words):
  filt = filter_words.split()
  punct = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
  st = ""
  for char in text:
    if char not in punct:
      st = st+char
  Str = st.lower()
  temp = " ".join(Str.split())

  lis = temp.split()
      
  dic = {}
  for i in lis:
    if i in dic:
      dic[i]+=1
    else:
      dic[i] = 1
  
  for x in filt:
    if x in dic.keys():
      dic.pop(x)
  
  counts = sorted(dic.items(), key = lambda x: x[1], reverse=True)
  res = list()
  count = 0
  for key in counts:
    if count == 3:
      break
    else:
      res.append(key[0])
    count = count+1
  
  return res

