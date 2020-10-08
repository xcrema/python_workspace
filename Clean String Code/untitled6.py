# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 11:13:30 2020

@author: Achyut

Given a string, strip punctuation, extra spaces and convert to lower case.
 Return the clean string.

NOTE: The changes you make should be done only on the clean_string function.
"""
def clean_string(inp_str):
  punct = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
  st = ""
  for char in inp_str:
    if char not in punct:
      st = st+char
  
  return (st.lower()).strip()
  
inp_str = input()
print(clean_string(inp_str))

