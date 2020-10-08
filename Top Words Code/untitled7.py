# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 11:15:09 2020

@author: Achyut

Write a function(top_words()) that takes text, removes punctuation, converts it to lowercase and counts the frequency of words. 
Return the top 5 most frequently occurring words.

input: string
output: list of top 5 words

Note: Copy/Paste clean_string() from the previous answer and make all changes to the count_words function.
"""

def top_words(inp_str):
  punct = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
  st = ""
  for char in inp_str:
    if char not in punct:
      st = st+char
  
  st = (st.lower()).strip()
  lis = st.split()
  #print(lis)
  dic = {}
  for i in lis:
    if i in dic.keys():
      dic[i] = dic.get(i)+1
    else:
      dic[i] = 1
  counts = (sorted(dic.items(), key = lambda kv:(kv[1], kv[0]), reverse=True))
  res = list()
  count = 0
  for key in counts:
    if count == 5:
      break
    else:
      res.append(key[0])
    count = count+1

  return res
  

